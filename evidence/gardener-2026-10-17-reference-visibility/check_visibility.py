"""Offline, real-Git fixture: advertised equality is not whole-ref equality.

Creates only a new temporary fixture beneath this receipt, disables inherited
Git configuration/hooks, makes no network requests, and removes that fixture.
The captures and exact commands remain. This is not mirror data.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
assert ROOT == Path('/Users/yu/castle')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def decode(data):
    pos, packets = 0, []
    while pos < len(data):
        prefix = data[pos:pos+4]
        assert re.fullmatch(rb'[0-9a-f]{4}', prefix), prefix
        length = int(prefix, 16)
        if length == 0:
            packets.append(None)
            pos += 4
        else:
            assert 4 <= length <= 65520 and pos+length <= len(data)
            packets.append(data[pos+4:pos+length])
            pos += length
    # Direct upload-pack emits the ref block, not the HTTP service envelope.
    assert packets and packets[-1] is None
    refs, caps = {}, []
    for index, packet in enumerate(packets[:-1]):
        assert packet is not None
        line = packet.removesuffix(b'\n')
        if index == 0:
            line, rawcaps = line.split(b'\0')
            caps = rawcaps.decode('ascii').split()
        oid, ref = line.decode('ascii').split(' ', 1)
        assert re.fullmatch('[0-9a-f]{40}', oid) and ref not in refs
        refs[ref] = oid
    return {'refs': refs, 'capabilities': caps, 'packet_count': len(packets)}

def save(name, value):
    with (HERE / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def main():
    assert not (HERE / 'visibility-result.json').exists(), 'refuse to overwrite a run'
    fixture = HERE / 'local-fixture'
    fixture.mkdir()  # Exclusive: never remove someone else's pre-existing tree.
    log, result = [], {'kind': 'constructed local fixture; real Git, not host data',
                      'started_utc': datetime.now(timezone.utc).isoformat(),
                      'network_requests': 0, 'checks': {}}
    try:
        for name in ('home', 'xdg', 'tmp', 'template', 'hooks'):
            (fixture / name).mkdir()
        (fixture / 'empty-config').write_text('')
        env = {
            'PATH': '/usr/bin:/bin:/usr/sbin:/sbin', 'LC_ALL': 'C', 'TZ': 'UTC',
            'HOME': str(fixture / 'home'), 'XDG_CONFIG_HOME': str(fixture / 'xdg'),
            'TMPDIR': str(fixture / 'tmp'), 'GIT_CONFIG_NOSYSTEM': '1',
            'GIT_CONFIG_GLOBAL': str(fixture / 'empty-config'),
            'GIT_CONFIG_SYSTEM': str(fixture / 'empty-config'),
            'GIT_TERMINAL_PROMPT': '0', 'GIT_PROTOCOL': 'version=0',
            'GIT_AUTHOR_NAME': 'Constructed fixture', 'GIT_AUTHOR_EMAIL': 'fixture@example.invalid',
            'GIT_COMMITTER_NAME': 'Constructed fixture', 'GIT_COMMITTER_EMAIL': 'fixture@example.invalid',
            'GIT_AUTHOR_DATE': '2026-10-17T00:00:00+0000',
            'GIT_COMMITTER_DATE': '2026-10-17T00:00:00+0000',
        }
        result['explicit_environment'] = env
        repo = fixture / 'repo.git'
        def git(*args, data=b'', in_repo=False):
            command = ['git', '-c', 'core.hooksPath='+str(fixture/'hooks'),
                       '-c', 'core.fsmonitor=false', '-c', 'gc.auto=0',
                       '-c', 'maintenance.auto=false']
            if in_repo:
                command += ['--git-dir='+str(repo)]
            command += list(args)
            done = subprocess.run(command, input=data, capture_output=True, env=env,
                                  cwd=fixture, timeout=15)
            log.append({'command': command, 'stdin': data.decode('ascii'),
                        'exit_code': done.returncode, 'stdout_hex': done.stdout.hex(),
                        'stderr': done.stderr.decode('utf-8', errors='replace')})
            assert done.returncode == 0, log[-1]
            return done.stdout
        result['git_version'] = git('--version').decode().strip()
        git('init', '--bare', '--object-format=sha1', '--initial-branch=main',
            '--template='+str(fixture/'template'), str(repo))
        tree = git('mktree', in_repo=True).decode().strip()
        main_oid = git('commit-tree', tree, data=b'public fixture\n', in_repo=True).decode().strip()
        first = git('commit-tree', tree, '-p', main_oid, data=b'private before\n', in_repo=True).decode().strip()
        second = git('commit-tree', tree, '-p', first, data=b'private after\n', in_repo=True).decode().strip()
        git('update-ref', 'refs/heads/main', main_oid, in_repo=True)
        git('update-ref', 'refs/heads/private', first, in_repo=True)
        def capture(label, hidden):
            stored = git('show-ref', in_repo=True)
            settings = ['-c', 'transfer.advertiseSID=false']
            if hidden:
                settings += ['-c', 'uploadpack.hideRefs=refs/heads/private']
            body = git(*settings, 'upload-pack', '--http-backend-info-refs', str(repo))
            for filename, data in ((label+'.pkt', body), (label+'-stored-refs.txt', stored)):
                with (HERE / filename).open('xb') as stream:
                    stream.write(data)
            return {'body_sha256': sha(body), 'body_bytes': len(body),
                    'advertised': decode(body), 'stored_refs': stored.decode()}
        before = capture('hidden-before', True)
        git('update-ref', 'refs/heads/private', second, first, in_repo=True)
        after = capture('hidden-after', True)
        exposed = capture('exposed-after', False)
        checks = {
            'stored_refs_changed_with_hidden_update': before['stored_refs'] != after['stored_refs'],
            'hidden_advertisements_byte_identical':
                (HERE/'hidden-before.pkt').read_bytes() == (HERE/'hidden-after.pkt').read_bytes(),
            'hidden_reference_maps_equal': before['advertised'] == after['advertised'],
            'only_main_and_head_advertised_while_hidden':
                set(after['advertised']['refs']) == {'HEAD', 'refs/heads/main'},
            'no_stored_reference_change_when_visibility_changes': after['stored_refs'] == exposed['stored_refs'],
            'visibility_change_changes_advertisement':
                (HERE/'hidden-after.pkt').read_bytes() != (HERE/'exposed-after.pkt').read_bytes(),
            'exposed_reference_has_new_private_tip': exposed['advertised']['refs']['refs/heads/private'] == second,
            'public_tip_unchanged_in_all_captures': all(
                c['advertised']['refs']['HEAD'] == c['advertised']['refs']['refs/heads/main'] == main_oid
                for c in (before, after, exposed)),
        }
        assert all(checks.values()), checks
        result.update({'captures': {'hidden_before': before, 'hidden_after': after, 'exposed_after': exposed},
                       'checks': checks, 'all_passed': True})
    except BaseException as exc:
        result.update({'all_passed': False, 'error': repr(exc)})
        raise
    finally:
        assert fixture.resolve().parent == HERE and not fixture.is_symlink()
        shutil.rmtree(fixture)
        result['fixture_removed'] = not fixture.exists()
        result['finished_utc'] = datetime.now(timezone.utc).isoformat()
        result['script_sha256'] = sha(Path(__file__).read_bytes())
        save('commands.json', log)
        save('visibility-result.json', result)
    print(json.dumps({'git_version': result['git_version'], 'checks': result['checks'],
                      'fixture_removed': result['fixture_removed'], 'all_passed': result['all_passed']}, indent=2))

if __name__ == '__main__':
    main()
