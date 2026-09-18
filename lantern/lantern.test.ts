// lantern.test.ts — run with `bun test` from this folder.
//
// Two kinds of test, deliberately separated:
//
//  1. **The reading rules**, checked against a tiny castle built here in a
//     temporary folder. These are the tests that must never change quietly:
//     if the lantern starts reading `[[bricks]]` differently, something below
//     goes red.
//  2. **The real castle**, checked only for things that should be true of any
//     castle — it builds, it can be searched, the numbers agree with each
//     other. Nothing here asserts a *count*, because the gardener changes the
//     counts every three hours and a test that fails at 3 a.m. for being
//     correct is a test that gets deleted.
//
// No test writes anything into ~/castle. The temporary castle lives in bun's
// temp folder and the temporary index beside it.

import { test, expect, describe, beforeAll, afterAll } from "bun:test";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { readStone, readCastle, normalize, linkStatus, resolve, resolveCastle } from "./read.ts";
import { open, look, asFts, path as chainBetween } from "./store.ts";
import { toHtml } from "./page.ts";
import { walk } from "./walk.ts";

// ── a tiny castle, built for the test and thrown away ───────────────────────

let root: string;
let indexPath: string;

const FILES: Record<string, string> = {
  "words/honesty.md": `# honesty

*The gap between saying and proving is where honesty lives.*

Honesty leans on [[proof]] and on [[silence]], and lives in the [gate](../gate.md).
It has a [dead friend](../rooms/gone.md) and a door out to https://example.org/thing.

Links: [[proof]] · [[silence]]
`,
  "words/proof.md": `# proof

*What makes a claim more than a wish.*

- 2026-07-01 09:30 · a proof filed as a thought — yu
- 2026-07-02 · one without a time — the gardener

Proof answers to [[honesty]].
`,
  "rooms/the-hall.md": `# the-hall

*Where things gather.*

The hall holds [[honesty]] and the word [[proof]], and points at
[honesty itself](../words/honesty.md#anchor) with an anchor.

It also names [[a brick nobody laid]].
`,
  "gate.md": `# The gate

Come in. The [hall](rooms/the-hall.md) is through there, and so is the
[folder of words](words).
`,
};

beforeAll(() => {
  root = mkdtempSync(join(tmpdir(), "lantern-test-"));
  indexPath = join(root, "test-index.db");
  for (const [rel, text] of Object.entries(FILES)) {
    const at = join(root, rel);
    mkdirSync(join(at, ".."), { recursive: true });
    writeFileSync(at, text);
  }
});

afterAll(() => rmSync(root, { recursive: true, force: true }));

// ── the reading rules ───────────────────────────────────────────────────────

describe("reading one stone", () => {
  const stone = () => readStone("word", "words/honesty.md", FILES["words/honesty.md"], 100, 0);

  test("takes its title from the first heading and its name from the filename", () => {
    expect(stone().title).toBe("honesty");
    expect(stone().name).toBe("honesty");
  });

  test("takes the italic line under the title as the epigraph, without the stars", () => {
    expect(stone().epigraph).toBe("The gap between saying and proving is where honesty lives.");
  });

  test("finds every brick, and does not count the same one twice per mention", () => {
    const bricks = stone().links.filter((l) => l.form === "wiki").map((l) => l.target);
    expect(bricks).toEqual(["proof", "silence", "proof", "silence"]);
  });

  test("resolves a relative path against the folder the file sits in", () => {
    const paths = stone().links.filter((l) => l.form === "path").map((l) => l.target);
    expect(paths).toContain("gate.md");
    expect(paths).toContain("rooms/gone.md");
  });

  test("keeps a link out to the web as a web link, not a path", () => {
    const web = stone().links.filter((l) => l.form === "web");
    expect(web).toHaveLength(1);
    expect(web[0].target).toBe("https://example.org/thing");
  });

  test("strips an anchor from a path link, because the file is what matters", () => {
    const hall = readStone("room", "rooms/the-hall.md", FILES["rooms/the-hall.md"], 100, 0);
    expect(hall.links.filter((l) => l.form === "path").map((l) => l.target)).toContain("words/honesty.md");
  });

  test("reads a dated thought with or without a time, and the author after the last dash", () => {
    const logs = readStone("word", "words/proof.md", FILES["words/proof.md"], 100, 0).logs;
    expect(logs).toEqual([
      { at: "2026-07-01 09:30", text: "a proof filed as a thought", who: "yu" },
      { at: "2026-07-02", text: "one without a time", who: "the gardener" },
    ]);
  });

  test("an alias brick shows the alias and links the target", () => {
    const s = readStone("word", "words/x.md", "leaning on [[honesty|the honest thing]].", 1, 0);
    expect(s.links[0]).toMatchObject({ target: "honesty", text: "the honest thing" });
  });

  test("falls back to the filename when a file has no heading at all", () => {
    expect(readStone("word", "words/bare.md", "just prose, no title.\n", 1, 0).title).toBe("bare");
  });
});

describe("where the castle is", () => {
  test("CASTLE= wins when it is set", () => {
    expect(resolveCastle({ CASTLE: "/tmp/other-castle" })).toBe("/tmp/other-castle");
  });

  test("a blank CASTLE falls through to the tree this lantern sits in", () => {
    expect(resolveCastle({})).toBe(dirname(import.meta.dir));
    expect(resolveCastle({ CASTLE: "   " })).toBe(dirname(import.meta.dir));
  });

  test("the default is the folder that holds lantern/, so a clone is already home", () => {
    expect(resolveCastle({})).toBe(dirname(import.meta.dir));
  });

  test("the index records the root it actually read", async () => {
    const { db } = await open({ root, indexPath, force: true });
    const held = db.query<{ value: string }, []>("select value from meta where key='castle'").get()!.value;
    expect(held).toBe(root);
    db.close();
  });

  test("lantern here names the tree without opening the index", () => {
    const proc = Bun.spawnSync({
      cmd: ["bun", join(import.meta.dir, "lantern.ts"), "here", "--json"],
      env: { ...process.env, CASTLE: root },
      stdout: "pipe",
      stderr: "pipe",
    });
    expect(proc.exitCode).toBe(0);
    const body = JSON.parse(new TextDecoder().decode(proc.stdout));
    expect(body.result.castle).toBe(root);
    expect(body.result.via).toBe("CASTLE");
  });
});

describe("normalising a path", () => {
  test("climbs out of a folder with ..", () => expect(normalize("words", "../gate.md")).toBe("gate.md"));
  test("stays put with .", () => expect(normalize("words", "./joy.md")).toBe("words/joy.md"));
  test("handles a bare filename in the root", () => expect(normalize("", "gate.md")).toBe("gate.md"));
  test("does not climb above the castle", () => expect(normalize("", "../../etc/passwd")).toBe("etc/passwd"));
});

describe("judging a link honestly", () => {
  let castle: Awaited<ReturnType<typeof readCastle>>;
  beforeAll(async () => { castle = await readCastle(root); });

  const linkFrom = (path: string, target: string) =>
    castle.byPath.get(path)!.links.find((l) => l.target === target)!;

  test("a brick that names a real word lands on it", () => {
    expect(linkStatus(castle, linkFrom("words/honesty.md", "proof"))).toBe("stone");
  });

  test("a brick naming a word nobody wrote is unlaid, not broken", () => {
    expect(linkStatus(castle, linkFrom("words/honesty.md", "silence"))).toBe("unlaid");
  });

  test("a path pointing at a missing file is broken", () => {
    expect(linkStatus(castle, linkFrom("words/honesty.md", "rooms/gone.md"))).toBe("broken");
  });

  test("a path pointing at a real folder is fine, not broken", () => {
    // This is the fault that made five honest links look broken: `[words](words)`
    // points at a folder, and folders are real.
    expect(linkStatus(castle, linkFrom("gate.md", "words"))).toBe("file");
  });

  test("a web link is never followed", () => {
    expect(linkStatus(castle, linkFrom("words/honesty.md", "https://example.org/thing"))).toBe("web");
  });

  test("a brick prefers the word over a room of the same name", async () => {
    const twin = mkdtempSync(join(tmpdir(), "lantern-twin-"));
    mkdirSync(join(twin, "words")); mkdirSync(join(twin, "rooms"));
    writeFileSync(join(twin, "words/karma.md"), "# karma\n");
    writeFileSync(join(twin, "rooms/karma.md"), "# karma\n");
    const both = await readCastle(twin);
    expect(both.byName.get("karma")!.path).toBe("words/karma.md");
    expect(both.ambiguous.get("karma")).toEqual(["words/karma.md", "rooms/karma.md"]);
    rmSync(twin, { recursive: true, force: true });
  });
});

// ── the pages ───────────────────────────────────────────────────────────────

describe("turning markdown into a page", () => {
  const route = (t: string) => (t === "nowhere" || t === "rooms/gone.md" ? null : `/at/${t}`);
  const render = (md: string, dir = "words") => toHtml(md, dir, route);

  test("a laid brick becomes a link and an unlaid one becomes plain marked words", () => {
    const html = render("Leaning on [[joy]] and [[nowhere]].");
    expect(html).toContain('<a class="brick" href="/at/joy">joy</a>');
    expect(html).toContain('class="unlaid"');
    expect(html).not.toContain('href="/at/nowhere"');
    // The words of an unlaid brick must survive — this is the bug where
    // rewriting the tag with replace() silently ate the label.
    expect(html).toContain("nowhere</span>");
  });

  test("an alias brick shows the label and links the target", () => {
    expect(render("see [[joy|the good part]]")).toContain('<a class="brick" href="/at/joy">the good part</a>');
  });

  test("a relative link is resolved against the folder the stone lives in", () => {
    expect(render("the [gate](../gate.md)")).toContain('href="/at/gate.md"');
  });

  test("a relative link pointing at nothing keeps its words and loses its door", () => {
    const html = render("a [dead friend](../rooms/gone.md)");
    expect(html).toContain("dead friend");
    expect(html).toContain('class="blocked"');
    expect(html).not.toContain("href=");
    // The path it wanted is kept in the title, so a reader can see what is missing.
    expect(html).toContain("points at nothing: ../rooms/gone.md");
  });

  test("stars inside code and fences stay stars", () => {
    expect(render("try `a *b* c` here")).toContain("<code>a *b* c</code>");
    expect(render("```\nascii *art*\n```")).toContain("ascii *art*");
  });

  test("the three things the hand-written renderer could not do", () => {
    expect(render("| a | b |\n|---|---|\n| 1 | 2 |")).toContain("<table>");
    expect(render("- [x] done\n- [ ] not")).toContain("task-list-item");
    expect(render("~~struck~~")).toContain("<del>struck</del>");
  });

  // ── the safety net ────────────────────────────────────────────────────────
  // Each of these passed only because of something hand-written. bun's
  // markdown renderer does not do them, and its options fail silently if
  // misspelled, so these tests are the thing standing between the castle and
  // a page that can run code.

  test("raw HTML in the prose is shown as text, never live", () => {
    for (const evil of ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "<style>body{}</style>"]) {
      const html = render(evil);
      expect(html).not.toContain(evil);
      expect(html).toContain("&lt;");
    }
  });

  test("a javascript: or data: link keeps its words and loses its href", () => {
    for (const scheme of ["javascript:alert(1)", "JaVaScRiPt:alert(1)", "data:text/html;base64,PHM+", "vbscript:x"]) {
      const html = render(`[click](${scheme})`);
      expect(html).toContain("click");
      expect(html).not.toMatch(/href="(javascript|data|vbscript)/i);
      expect(html).toContain("blocked");
    }
  });

  test("a data: image is not loaded", () => {
    expect(render("![i](data:text/html;base64,PHM+)")).not.toContain("src=\"data:");
  });

  test("an ordinary http link is marked as leaving the castle", () => {
    const html = render("[out](https://example.org/x)");
    expect(html).toContain('href="https://example.org/x"');
    expect(html).toContain("away");
    expect(html).toContain('rel="noreferrer noopener"');
  });

  test("the markdown flags are really in force, not silently misspelled", () => {
    // Each of these is only true because one flag fired. If a flag name is ever
    // renamed or mistyped, bun ignores it without a word and this goes red.
    expect(render("[[brick]]")).toContain("brick"); // wikiLinks
    expect(render("<b>x</b>")).toContain("&lt;b&gt;"); // noHtmlSpans
    expect(render("<div>x</div>")).toContain("&lt;div&gt;"); // noHtmlBlocks
    expect(render("see https://example.org/bare")).toContain('href="https://example.org/bare"'); // autolinks
  });
});

// ── the index, over the tiny castle ─────────────────────────────────────────

describe("the index", () => {
  test("builds, is reused while nothing changes, and rebuilds when something does", async () => {
    const first = await open({ root, indexPath, force: true });
    expect(first.built).toBe(true);
    expect(first.stones).toBe(Object.keys(FILES).length);
    first.db.close();

    const again = await open({ root, indexPath });
    expect(again.built).toBe(false);
    again.db.close();

    writeFileSync(join(root, "words/new-word.md"), "# new-word\n\nAdded mid-test.\n");
    const third = await open({ root, indexPath });
    expect(third.built).toBe(true);
    expect(third.stones).toBe(Object.keys(FILES).length + 1);
    third.db.close();
    rmSync(join(root, "words/new-word.md"));
  });

  test("search finds a word by its prose and ranks the word itself first", async () => {
    const { db } = await open({ root, indexPath, force: true });
    const hits = look(db, '"honesty"');
    expect(hits.length).toBeGreaterThan(0);
    expect(hits[0].name).toBe("honesty");
    db.close();
  });

  test("search finds nothing when the castle says nothing", async () => {
    const { db } = await open({ root, indexPath });
    expect(look(db, '"pumpernickel"')).toHaveLength(0);
    db.close();
  });

  test("a chain is found in both directions and is the shortest one", async () => {
    const { db } = await open({ root, indexPath });
    expect(chainBetween(db, "honesty", "proof")).toEqual(["honesty", "proof"]);
    expect(chainBetween(db, "proof", "the-hall")).toEqual(["proof", "the-hall"]);
    expect(chainBetween(db, "honesty", "honesty")).toEqual(["honesty"]);
    expect(chainBetween(db, "honesty", "no-such-stone")).toBeNull();
    db.close();
  });
});

// ── reading what someone typed ──────────────────────────────────────────────

describe("turning a typed question into a search", () => {
  test("a handful of words means all of them", () => {
    expect(asFts("words bridge")).toBe('"words" "bridge"');
  });

  test("one quoted argument means a phrase", () => {
    // Otherwise `castle look \"words are the bridge\"` highlights every \"the\"
    // in the castle and ranks by accident.
    expect(asFts("words are the bridge", true)).toBe('"words are the bridge"');
  });

  test("a searcher who speaks FTS5 is left alone", () => {
    for (const q of ['joy AND safety', '"a phrase"', 'bridge*', 'NEAR(agent registry, 10)']) {
      expect(asFts(q)).toBe(q);
    }
  });

  test("a hyphen or an apostrophe is quoted, so FTS5 cannot read it as an operator", () => {
    expect(asFts("fail-closed")).toBe('"fail-closed"');
    expect(asFts("don't")).toBe('"don\'t"');
  });

  test("the quoting really does survive SQLite, not just look right", async () => {
    const { db } = await open({ root, indexPath });
    for (const typed of ["fail-closed", "don't", "a-b-c"]) {
      expect(() => look(db, asFts(typed))).not.toThrow();
    }
    db.close();
  });
});

// ── the walk, actually served ──────────────────────────────────────────────
//
// Every door, opened for real over HTTP. Four separate 500s during the building
// of this were found by hand exactly this way; now they would be found here.

describe("the walk view", () => {
  let server: Awaited<ReturnType<typeof walk>>;
  let base: string;

  beforeAll(async () => {
    server = await walk(0, { quiet: true }); // port 0 = whatever is free
    base = `http://127.0.0.1:${server.port}`;
  });
  afterAll(() => server.stop());

  test("it binds the loopback address only", () => {
    expect(server.hostname).toBe("127.0.0.1");
  });

  test("every door opens", async () => {
    const doors = ["/", "/lantern.css", "/owed", "/check", "/wander", "/wing/word", "/wing/room", "/look?q=honesty", "/stone/joy"];
    for (const door of doors) {
      const r = await fetch(base + door);
      expect({ door, status: r.status }).toEqual({ door, status: 200 });
      expect((await r.text()).length).toBeGreaterThan(200);
    }
  });

  test("a stone reached by its exact path opens too", async () => {
    const r = await fetch(`${base}/at/words/joy.md`);
    expect(r.status).toBe(200);
    expect(await r.text()).toContain("joy");
  });

  test("a door that is not there says so, and does not fall through", async () => {
    for (const door of ["/nope", "/at/nothing/here.md", "/stone/no-such-word", "/wing/nonsense"]) {
      expect((await fetch(base + door)).status).toBe(404);
    }
  });

  test("no path can be smuggled out of the castle", async () => {
    // The lantern never builds a filesystem path from a url — it looks names up
    // in the index — so traversal has nothing to traverse. Checked, not assumed.
    for (const attack of [
      "/at/../../etc/hosts",
      "/at/%2e%2e%2f%2e%2e%2fetc%2fhosts",
      "/at/%2fetc%2fpasswd",
      "/stone/%2e%2e%2f%2e%2e%2fetc%2fpasswd",
      "/at/words/../../../../etc/hosts",
    ]) {
      const r = await fetch(base + attack);
      expect(r.status).toBe(404);
      expect(await r.text()).not.toContain("root:");
    }
  });

  test("a search that SQLite cannot parse explains itself instead of failing", async () => {
    const r = await fetch(`${base}/look?q=${encodeURIComponent('"unclosed AND (')}`);
    expect(r.status).toBe(200);
    expect(await r.text()).toMatch(/could not read that search|Nothing in the castle/);
  });
});

// ── the one promise everything else rests on ────────────────────────────────

describe("the lantern only looks", () => {
  test("running every command changes nothing in the castle", async () => {
    // The whole folder's claim, checked the only way that means anything: take
    // the castle's fingerprint — every path, size and modification time — run
    // everything the lantern can do, and take it again.
    const fingerprint = async () => {
      const castle = await readCastle();
      return castle.stones
        .map((s) => `${s.path}:${s.bytes}:${Math.round(s.mtime)}`)
        .sort()
        .join("\n");
    };

    const before = await fingerprint();

    const { db } = await open({});
    look(db, '"honesty"');
    chainBetween(db, "joy", "safety");
    db.query("select count(*) from stone").get();
    db.query("select * from link limit 5").all();
    db.query("select * from log limit 5").all();
    db.close();

    const served = await walk(0, { quiet: true });
    for (const door of ["/", "/owed", "/check", "/wander", "/look?q=joy", "/at/words/joy.md"]) {
      await fetch(`http://127.0.0.1:${served.port}${door}`);
    }
    served.stop();

    expect(await fingerprint()).toBe(before);
  });

  test("the browser view binds the loopback address and nothing else", async () => {
    const source = await Bun.file(`${import.meta.dir}/walk.ts`).text();
    expect(source).toContain('hostname: "127.0.0.1"');
    // Looking for the string "0.0.0.0" would trip over the comment that warns
    // against it. What matters is that nothing ever *binds* to it.
    expect(source).not.toMatch(/hostname:\s*["'](?!127\.0\.0\.1)/);
    const served = await walk(0, { quiet: true });
    expect(served.hostname).toBe("127.0.0.1");
    served.stop();
  });
});

// ── the real castle ─────────────────────────────────────────────────────────
//
// These make no claim about how big the castle is or what it says. They only
// insist that whatever it says today, the lantern can read it without falling
// over and without contradicting itself.

describe("the castle as it stands today", () => {
  test("reads whole, and every stone has a name, a path and a title", async () => {
    const castle = await readCastle();
    expect(castle.stones.length).toBeGreaterThan(100);
    for (const s of castle.stones) {
      expect(s.name).not.toBe("");
      expect(s.path.endsWith(".md")).toBe(true);
      expect(s.title).not.toBe("");
    }
  });

  test("every link gets exactly one honest verdict", async () => {
    const castle = await readCastle();
    const kinds = new Set(castle.stones.flatMap((s) => s.links.map((l) => linkStatus(castle, l))));
    for (const k of kinds) expect(["stone", "file", "unlaid", "broken", "web"]).toContain(k);
  });

  test("a link that says it lands on a stone really does", async () => {
    const castle = await readCastle();
    for (const s of castle.stones) {
      for (const l of s.links) {
        if (linkStatus(castle, l) === "stone") expect(resolve(castle, l)).not.toBeNull();
      }
    }
  });

  test("the index agrees with the markdown about how many stones there are", async () => {
    const castle = await readCastle();
    const { db } = await open({ force: true });
    expect(db.query<{ n: number }, []>("select count(*) n from stone").get()!.n).toBe(castle.stones.length);
    db.close();
  });

  test("the castle can be searched for its own founding words", async () => {
    const { db } = await open({});
    for (const word of ['"understanding"', '"joy"', '"bridge"']) {
      expect(look(db, word).length).toBeGreaterThan(0);
    }
    db.close();
  });
});
