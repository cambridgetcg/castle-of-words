// store.ts — the lantern's index: the castle, arranged so it can be asked things.
//
// The markdown is the truth. This is a *reading* of it, thrown away and rebuilt
// whenever the castle changes. Nothing in here is precious: delete index.db and
// the next command rebuilds it in under a second.
//
// Why a database at all, when reading the whole castle takes 40 ms? For one
// thing only: SQLite's FTS5 gives ranked search with stemming, phrases and
// snippets, and hand-writing that worse would be the opposite of simple.

import { Database } from "bun:sqlite";
import { CASTLE, readCastle, linkStatus, resolve, type Castle, type Kind } from "./read.ts";

/** Where the index lives by default. Tests pass their own path so a test run
 *  can never replace the real castle's index. */
export const DEFAULT_INDEX = `${import.meta.dir}/index.db`;
export const INDEX = DEFAULT_INDEX;

const SCHEMA = `
create table stone (
  id       integer primary key,
  kind     text not null,
  name     text not null,
  path     text not null unique,
  title    text not null,
  epigraph text not null,
  body     text not null,
  bytes    integer not null,
  mtime    integer not null
);
create index stone_name on stone(name);
create index stone_kind on stone(kind);

-- One row per link written in the castle. to_id is null unless the link lands
-- on an indexed stone; status says why (see linkStatus in read.ts).
create table link (
  from_id integer not null references stone(id),
  form    text not null,
  target  text not null,
  text    text not null,
  status  text not null,
  to_id   integer
);
create index link_from on link(from_id);
create index link_to on link(to_id);
create index link_status on link(status);

-- Every dated thought filed anywhere in the castle, in one place.
create table log (
  stone_id integer not null references stone(id),
  at       text not null,
  text     text not null,
  who      text not null
);
create index log_at on log(at);

create table meta (key text primary key, value text not null);

-- Ranked search. External content: the prose lives in the stone table and FTS5
-- keeps only its index, so the castle's 3 MB is not stored twice.
create virtual table search using fts5(
  name, title, epigraph, body,
  content='stone', content_rowid='id',
  tokenize='porter unicode61'
);
`;

/** A cheap, exact fingerprint of the castle on disk: if this is unchanged, the
 *  index cannot be stale. Built from every path, size and modification time. */
function signature(castle: Castle): string {
  const parts = castle.stones
    .map((s) => `${s.path}:${s.bytes}:${Math.round(s.mtime)}`)
    .sort();
  return `${castle.stones.length}-${Bun.hash(parts.join("\n")).toString(16)}`;
}

/** Open the index, rebuilding it first if the castle has moved on.
 *  `force` rebuilds regardless. Returns the db and what it had to do. */
export async function open(
  opts: { root?: string; force?: boolean; quiet?: boolean; indexPath?: string } = {},
): Promise<{ db: Database; built: boolean; ms: number; stones: number }> {
  const root = opts.root ?? CASTLE;
  const INDEX = opts.indexPath ?? DEFAULT_INDEX;
  const t0 = performance.now();

  if (!opts.force) {
    // A missing or half-written index must never look valid. Any surprise here
    // means "rebuild", never "carry on and hope".
    try {
      const db = new Database(INDEX, { readonly: true });
      const held = db.query<{ value: string }, []>("select value from meta where key='signature'").get();
      if (held) {
        const castle = await readCastle(root);
        if (held.value === signature(castle)) {
          const n = db.query<{ n: number }, []>("select count(*) n from stone").get()!.n;
          return { db, built: false, ms: performance.now() - t0, stones: n };
        }
      }
      db.close();
    } catch (e) {
      // A missing index is the normal first run and says nothing. Anything else
      // is a surprise, and a silent surprise here once hid a real bug for an
      // hour: it looked like the castle kept changing when the index was
      // simply unreadable. So surprises get said out loud.
      const why = (e as { code?: string }).code ?? String(e);
      if (why !== "SQLITE_CANTOPEN" || (await Bun.file(INDEX).exists())) {
        if (!opts.quiet) console.error(`lantern: could not read the index (${why}) — rebuilding it`);
      }
    }
  }

  const castle = await readCastle(root);
  const db = build(castle, INDEX);
  return { db, built: true, ms: performance.now() - t0, stones: castle.stones.length };
}

/** Write a fresh index. Builds into a temporary file and moves it into place,
 *  so a crash halfway through leaves the old index intact rather than a
 *  half-castle that answers questions wrongly. */
export function build(castle: Castle, INDEX = DEFAULT_INDEX): Database {
  const tmp = `${INDEX}.building`;
  for (const f of [tmp, `${tmp}-wal`, `${tmp}-shm`]) {
    try { require("node:fs").unlinkSync(f); } catch {}
  }

  const db = new Database(tmp, { create: true });
  // Journal off, not WAL. Two reasons, one of them a fault this cost an hour:
  //  - The whole build is one transaction into a throwaway file that is only
  //    moved into place once it is whole, so there is nothing to recover.
  //  - WAL mode is *written into the file header* and stays. A WAL database
  //    cannot be opened read-only unless its -shm companion exists, so every
  //    later `lantern look` failed with SQLITE_CANTOPEN — silently, because the
  //    staleness check swallowed it and rebuilt the index every single time.
  db.run("pragma journal_mode = off");
  db.run("pragma synchronous = off");
  db.run(SCHEMA);

  const putStone = db.prepare(
    `insert into stone (kind,name,path,title,epigraph,body,bytes,mtime)
     values (?,?,?,?,?,?,?,?)`,
  );
  const putLink = db.prepare(
    `insert into link (from_id,form,target,text,status,to_id) values (?,?,?,?,?,?)`,
  );
  const putLog = db.prepare(`insert into log (stone_id,at,text,who) values (?,?,?,?)`);

  // One transaction: 1046 stones and ~11,000 links in one write instead of
  // twelve thousand.
  const ids = new Map<string, number>();
  db.transaction(() => {
    for (const s of castle.stones) {
      const { lastInsertRowid } = putStone.run(
        s.kind, s.name, s.path, s.title, s.epigraph, s.body, s.bytes, Math.round(s.mtime),
      );
      ids.set(s.path, Number(lastInsertRowid));
    }
    for (const s of castle.stones) {
      const from = ids.get(s.path)!;
      for (const l of s.links) {
        const status = linkStatus(castle, l);
        // A brick names a stone; a path names a file. `resolve` knows which,
        // and `ids` is keyed by path, so go through the stone rather than
        // guessing which kind of name the target is.
        const landed = resolve(castle, l);
        putLink.run(from, l.form, l.target, l.text, status, landed ? ids.get(landed.path)! : null);
      }
      for (const g of s.logs) putLog.run(from, g.at, g.text, g.who);
    }
    db.run(
      `insert into search (rowid,name,title,epigraph,body)
       select id,name,title,epigraph,body from stone`,
    );
    const putMeta = db.prepare("insert into meta (key,value) values (?,?)");
    putMeta.run("signature", signature(castle));
    putMeta.run("built_at", new Date().toISOString());
    putMeta.run("castle", CASTLE);
    putMeta.run("stones", String(castle.stones.length));
  })();

  db.close();
  require("node:fs").renameSync(tmp, INDEX); // atomic: readers see the old index or the new one, never half
  return new Database(INDEX, { readonly: true });
}

// ── Asking the index things ─────────────────────────────────────────────────

/** Turn what someone typed into something FTS5 will accept.
 *
 *  Three readings, in order:
 *   - It already speaks FTS5 (quotes, `*`, AND/OR/NOT/NEAR) — leave it alone.
 *   - It arrived as ONE shell argument with spaces in it, which means the
 *     searcher quoted it: `castle look "words are the bridge"` is a phrase, and
 *     treating it as four separate words would highlight every "the" in the
 *     castle.
 *   - Otherwise it is a handful of words, each of which must appear. Each is
 *     quoted so that `fail-closed` or `don't` cannot be read as an operator. */
export function asFts(raw: string, wasQuoted = false): string {
  if (/["*():]|\b(AND|OR|NOT|NEAR)\b/.test(raw)) return raw;
  if (wasQuoted) return `"${raw.replace(/"/g, "")}"`;
  return raw.trim().split(/\s+/).map((t) => `"${t.replace(/"/g, "")}"`).join(" ");
}


export type Hit = {
  id: number;
  kind: Kind;
  name: string;
  path: string;
  title: string;
  snippet: string;
  score: number;
};

/** Ranked search. A name or title match outweighs a mention in the body,
 *  because someone searching "honesty" usually wants the word `honesty`
 *  before the forty rooms that mention it. */
export function look(db: Database, query: string, limit = 20): Hit[] {
  return db
    .query<Hit, [string, number]>(
      `select s.id, s.kind, s.name, s.path, s.title,
              snippet(search, 3, '«', '»', '…', 14) as snippet,
              -bm25(search, 0.0, 8.0, 4.0, 1.0) as score
         from search join stone s on s.id = search.rowid
        where search match ?
        order by score desc
        limit ?`,
    )
    .all(query, limit);
}

/** The shortest chain of links from one stone to another.
 *
 *  Plain breadth-first search over the link table, which is small enough
 *  (~9,000 edges) to hold in memory. Links are followed in both directions:
 *  in a castle of words, "leans on" and "is leaned on by" are both ways of
 *  saying two ideas are near each other. */
export function path(db: Database, fromName: string, toName: string): string[] | null {
  const idOf = (name: string) =>
    db.query<{ id: number }, [string]>(
      "select id from stone where name = ? order by case kind when 'word' then 0 when 'room' then 1 else 2 end limit 1",
    ).get(name)?.id ?? null;

  const a = idOf(fromName);
  const b = idOf(toName);
  if (a === null || b === null) return null;
  if (a === b) return [fromName];

  const near = new Map<number, number[]>();
  const join = (x: number, y: number) => {
    const held = near.get(x);
    if (held) held.push(y);
    else near.set(x, [y]);
  };
  for (const { f, t } of db.query<{ f: number; t: number }, []>(
    "select from_id f, to_id t from link where to_id is not null",
  ).all()) {
    join(f, t);
    join(t, f);
  }

  const cameFrom = new Map<number, number>([[a, -1]]);
  let edge = [a];
  while (edge.length) {
    const next: number[] = [];
    for (const id of edge) {
      for (const n of near.get(id) ?? []) {
        if (cameFrom.has(n)) continue;
        cameFrom.set(n, id);
        if (n === b) {
          const chain: number[] = [];
          for (let at: number = b; at !== -1; at = cameFrom.get(at)!) chain.push(at);
          chain.reverse();
          const nameOf = db.prepare<{ name: string }, [number]>("select name from stone where id = ?");
          return chain.map((id) => nameOf.get(id)!.name);
        }
        next.push(n);
      }
    }
    edge = next;
  }
  return null;
}
