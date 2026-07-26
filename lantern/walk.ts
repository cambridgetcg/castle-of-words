// walk.ts — the castle, in a browser, on this Mac only.
//
// `lantern walk` serves the castle at http://127.0.0.1:4141 so you can read it
// the way it is written: one stone per page, every brick a link you can follow.
//
// Three deliberate limits, each for a reason:
//
//  1. **127.0.0.1, never 0.0.0.0.** The raw castle holds private household
//     details — that is why the public site at castle-gate has a scrubbing
//     forge. This server does no scrubbing at all, so it must never be
//     reachable from another machine. Binding to the loopback address is the
//     whole of that protection, and it is not negotiable.
//  2. **No JavaScript on the page.** The search box is an ordinary HTML form.
//     Nothing to bundle, nothing to break, and it will still work in ten years.
//  3. **It lives only while you watch it.** No daemon, no scheduled job, no
//     background rhythm. Ctrl-C and it is gone — the plainest off-switch there
//     is.
//
// Nothing here writes to the castle.

import type { Database } from "bun:sqlite";
import { open, look, asFts, DEFAULT_INDEX } from "./store.ts";
import { CASTLE } from "./read.ts";
import { toHtml, type Router } from "./page.ts";

type Row = { id: number; kind: string; name: string; path: string; title: string; epigraph: string; body: string };

const WING_NAMES: Record<string, string> = {
  word: "words", room: "rooms", journal: "journal", tower: "tower", vibe: "wardrobe", hall: "halls",
};

// ── the dress ───────────────────────────────────────────────────────────────

/** The castle's own colors, read from the wardrobe at startup rather than
 *  copied here. Change vibe/palette.md, run `vibe bake`, restart the walk, and
 *  these pages change with the kingdom. */
async function dress(): Promise<string> {
  let tokens = "";
  const wardrobe = Bun.file(`${CASTLE}/vibe/tokens.css`);
  if (await wardrobe.exists()) tokens = await wardrobe.text();
  else tokens = ":root { --vibe-gate-ink:#1a1612; --vibe-gate-parchment:#f5efe2; --vibe-gate-foil:#b8902e; }";

  return `${tokens}
* { box-sizing: border-box }
:root {
  --ink: var(--vibe-gate-ink); --soft: var(--vibe-gate-ink-soft); --faint: var(--vibe-gate-ink-faint);
  --page: var(--vibe-gate-parchment); --card: var(--vibe-gate-card-paper);
  --edge: var(--vibe-gate-parchment-edge); --chip: var(--vibe-gate-parchment-deep);
  --gold: var(--vibe-gate-foil); --gold-deep: var(--vibe-gate-foil-dark);
  --alarm: var(--vibe-front-crimson);
}
@media (prefers-color-scheme: dark) {
  :root {
    --ink: var(--vibe-dark-text); --soft: var(--vibe-dark-text-muted); --faint: var(--vibe-dark-text-muted);
    --page: var(--vibe-dark-night); --card: var(--vibe-dark-panel);
    --edge: var(--vibe-dark-panel-edge); --chip: var(--vibe-dark-code-dim);
    --gold: var(--vibe-dark-gold); --gold-deep: var(--vibe-dark-gold-shadow);
    --alarm: var(--vibe-dark-crimson);
  }
}
body {
  margin: 0; background: var(--page); color: var(--ink);
  font: 17px/1.68 "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  -webkit-font-smoothing: antialiased;
}
header {
  border-bottom: 1px solid var(--edge); background: var(--card);
  padding: 1rem 1.25rem; display: flex; gap: 1rem; align-items: baseline; flex-wrap: wrap;
  position: sticky; top: 0; z-index: 2;
}
header .home { font-weight: 600; letter-spacing: .02em; text-decoration: none; color: var(--ink); white-space: nowrap }
header .home:hover { color: var(--gold-deep) }
header nav { display: flex; gap: .9rem; font-size: .84rem; letter-spacing: .06em; text-transform: uppercase }
header nav a { color: var(--faint); text-decoration: none }
header nav a:hover { color: var(--gold-deep); text-decoration: underline }
form.seek { margin-left: auto; display: flex; gap: .4rem }
form.seek input {
  font: inherit; font-size: .95rem; padding: .3rem .6rem; min-width: 15rem;
  background: var(--page); color: var(--ink); border: 1px solid var(--edge); border-radius: 3px;
}
form.seek input:focus { outline: 2px solid var(--gold); outline-offset: 1px }
form.seek button {
  font: inherit; font-size: .9rem; padding: .3rem .8rem; cursor: pointer;
  background: var(--chip); color: var(--ink); border: 1px solid var(--edge); border-radius: 3px;
}
form.seek button:hover { border-color: var(--gold) }
main { max-width: 42rem; margin: 0 auto; padding: 2.5rem 1.25rem 5rem }
main.wide { max-width: 56rem }
h1 { font-size: 1.9rem; line-height: 1.2; margin: 0 0 .3rem; font-weight: 600 }
h2 { font-size: 1.3rem; margin: 2.2rem 0 .6rem; font-weight: 600 }
h3 { font-size: 1.08rem; margin: 1.8rem 0 .5rem; font-weight: 600; color: var(--soft) }
p { margin: 0 0 1.1rem }
a { color: var(--gold-deep); text-decoration-color: var(--edge); text-underline-offset: 2px }
a:hover { text-decoration-color: var(--gold) }
a.away::after { content: " ↗"; font-size: .8em; color: var(--faint) }
/* A brick is a link to a word the castle has DEFINED — the vocabulary it builds
   with. It earns a gold underline; an ordinary link to a room keeps the faint
   one. Without this rule the two looked identical, which threw away the whole
   point of telling them apart. */
a.brick { text-decoration-color: var(--gold) }
a.brick:hover { background: var(--chip) }
/* A brick that was named but never written: the words stay, there is no door. */
.unlaid {
  color: var(--faint); border-bottom: 1px dotted var(--faint); cursor: help;
}
blockquote {
  margin: 1.2rem 0; padding: .2rem 0 .2rem 1.1rem;
  border-left: 2px solid var(--gold); color: var(--soft); font-style: italic;
}
code { background: var(--chip); padding: .1em .35em; border-radius: 3px; font-size: .88em;
  font-family: "SF Mono", ui-monospace, monospace }
pre { background: var(--chip); border: 1px solid var(--edge); border-radius: 4px;
  padding: .9rem 1rem; overflow-x: auto; line-height: 1.4 }
pre code { background: none; padding: 0; font-size: .82em }
/* bun's renderer tags a fenced block with the language it was given. Nothing
   here highlights syntax, but naming the language is free and useful. */
pre { position: relative }
pre code[data-lang]::before {
  content: attr(data-lang); position: absolute; top: .3rem; right: .5rem;
  font-size: .68rem; letter-spacing: .08em; text-transform: uppercase;
  color: var(--faint);
}
hr { border: 0; border-top: 1px solid var(--edge); margin: 2rem 0 }
ul, ol { padding-left: 1.3rem } li { margin: .3rem 0 }
del { color: var(--faint) }
/* Tables, task lists and strikethrough are why this view uses bun's markdown
   renderer rather than the hand-written one it began with. */
table { border-collapse: collapse; margin: 1.2rem 0; font-size: .95rem; display: block; overflow-x: auto }
th, td { border: 1px solid var(--edge); padding: .35rem .7rem; text-align: left }
th { background: var(--chip); font-weight: 600 }
li.task-list-item { list-style: none; margin-left: -1.1rem }
li.task-list-item input { margin-right: .45rem; accent-color: var(--gold) }
/* A link the lantern refused: the words stay, the door does not. */
.blocked { color: var(--faint); text-decoration: line-through wavy; cursor: help }
.kind { font-size: .78rem; text-transform: uppercase; letter-spacing: .1em; color: var(--faint) }
.epigraph { color: var(--soft); font-style: italic; margin: .6rem 0 2rem; font-size: 1.05rem }
.near { border-top: 1px solid var(--edge); margin-top: 3rem; padding-top: 1.4rem; font-size: .93rem }
.near h3 { margin: 0 0 .4rem; font-size: .78rem; text-transform: uppercase; letter-spacing: .1em; color: var(--faint) }
.near p { margin: 0 0 1.1rem; line-height: 1.9 }
.near a { margin-right: .1rem }
.hit { margin: 0 0 1.5rem }
.hit .name { font-weight: 600; font-size: 1.05rem }
.hit .where { font-size: .8rem; color: var(--faint); margin-left: .5rem }
.hit .snip { color: var(--soft); font-size: .95rem; margin-top: .15rem }
.hit mark { background: var(--gold); color: #1a1612; padding: 0 .1em; border-radius: 2px }
/* The counting tables at the gate are a layout, not prose — no rules, no ground.
   Without this they inherit the borders meant for a room's real table. */
table.tally { border-collapse: collapse; font-size: .95rem; margin: 1rem 0; display: table }
table.tally td { padding: .22rem .9rem .22rem 0; vertical-align: baseline; border: 0; background: none }
table.tally td.n { text-align: right; font-variant-numeric: tabular-nums; font-weight: 600 }
.alarm { color: var(--alarm) }
.quiet { color: var(--faint); font-size: .9rem }
footer { max-width: 42rem; margin: 0 auto; padding: 0 1.25rem 3rem; color: var(--faint); font-size: .85rem }
footer a { color: var(--faint) }
`;
}

// ── the shell every page wears ──────────────────────────────────────────────

const esc = (s: string) => Bun.escapeHTML(s);

function shell(title: string, body: string, opts: { wide?: boolean; seek?: string } = {}): Response {
  return new Response(
    `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)} · the castle by lantern-light</title>
<link rel="stylesheet" href="/lantern.css">
</head><body>
<header>
  <a class="home" href="/">the castle of understanding</a>
  <nav>
    <a href="/wing/word">words</a><a href="/wing/room">rooms</a>
    <a href="/owed">owed</a><a href="/check">check</a><a href="/wander">wander</a>
  </nav>
  <form class="seek" action="/look" method="get" role="search">
    <input type="search" name="q" placeholder="look for words…" value="${esc(opts.seek ?? "")}" aria-label="search the castle">
    <button type="submit">look</button>
  </form>
</header>
<main${opts.wide ? ' class="wide"' : ""}>${body}</main>
<footer>Read by lantern-light from ${esc(CASTLE)} — the markdown is the truth, this is only a reading of it.
Nothing here can change the castle.</footer>
</body></html>`,
    { headers: { "content-type": "text/html; charset=utf-8" } },
  );
}

/** Start the server, or say in plain words why it could not.
 *  A stack trace is not an explanation, and "the port is taken" almost always
 *  means the lantern is already lit in another window. */
function serveOrExplain(options: Parameters<typeof Bun.serve>[0]) {
  try {
    return Bun.serve(options as never);
  } catch (e) {
    const why = (e as { code?: string }).code ?? "";
    const port = (options as { port?: number }).port;
    if (why === "EADDRINUSE") {
      console.error(`
  Port ${port} is already taken — the lantern is probably lit in another window.

  Look there first: http://127.0.0.1:${port}
  Or light a second one somewhere else:  castle walk --port ${(port ?? 4141) + 1}
`);
      process.exit(1);
    }
    throw e;
  }
}

function status(code: number, title: string, body: string): Response {
  const page = shell(title, body);
  return new Response(page.body, { status: code, headers: page.headers });
}

const notFound = (what: string) =>
  status(404, "not here", `<h1>Not here</h1><p>${esc(what)}</p><p><a href="/">back to the gate</a></p>`);

// ── the walk ────────────────────────────────────────────────────────────────

/** Light the lantern. Returns the running server, so a test can open every
 *  door for real and then put it out again.
 *  `port: 0` means "whatever is free" — read `server.port` for the answer. */
export async function walk(port = 4141, opts: { quiet?: boolean } = {}) {
  const quiet = opts.quiet ?? false;
  const css = await dress();
  let held = await open({ quiet });
  if (held.built && !quiet) console.log(`  read ${held.stones} stones from the markdown in ${held.ms.toFixed(0)} ms`);
  let indexWrittenAt = Bun.file(DEFAULT_INDEX).lastModified;
  let lookedForNews = performance.now();

  /** The index, as it is right now.
   *
   *  Two things can move under a walk that stays open for hours, and both did
   *  during the building of this:
   *
   *   1. **Another process rebuilds the index.** A rebuild finishes with an
   *      atomic rename, which is what keeps a reader from ever seeing a
   *      half-built castle — but it also means this process's open handle now
   *      points at a file that has been replaced. SQLite notices and every
   *      query fails with SQLITE_IOERR_VNODE. Comparing the index file's
   *      timestamp catches it for the price of one stat.
   *   2. **The gardener writes a new room.** Nobody has rebuilt anything, so
   *      the timestamp is unchanged and only a full look at the markdown can
   *      tell. That costs ~40 ms, so it happens at most once every ten seconds
   *      — which means a walk left open quietly grows new rooms as the gardener
   *      files them.
   */
  async function fresh(): Promise<Database> {
    const written = Bun.file(DEFAULT_INDEX).lastModified;
    if (written !== indexWrittenAt) {
      try { held.db.close(); } catch {}
      held = await open({ quiet: true });
      indexWrittenAt = Bun.file(DEFAULT_INDEX).lastModified;
      lookedForNews = performance.now();
      console.log("  the index changed underneath — reopened it");
      return held.db;
    }
    if (performance.now() - lookedForNews > 10_000) {
      lookedForNews = performance.now();
      const next = await open({ quiet: true });
      if (next.built) {
        try { held.db.close(); } catch {}
        held = next;
        indexWrittenAt = Bun.file(DEFAULT_INDEX).lastModified;
        console.log(`  the castle moved on — ${next.stones} stones, read again in ${next.ms.toFixed(0)} ms`);
      } else {
        next.db.close(); // nothing had changed; keep the handle we already hold
      }
    }
    return held.db;
  }

  const byName = (db: Database, name: string) =>
    db.query<Row, [string]>(
      `select id,kind,name,path,title,epigraph,body from stone where name = ?
        order by case kind when 'word' then 0 when 'room' then 1 else 2 end limit 1`,
    ).get(name);
  const byPath = (db: Database, path: string) =>
    db.query<Row, [string]>(
      "select id,kind,name,path,title,epigraph,body from stone where path = ? limit 1",
    ).get(path);

  /** Where the links inside a stone lead. Wiki-bricks go by name; markdown
   *  paths go by exact path, because eighteen names are held by both a word
   *  and its room and a path link means the one it names. */
  const routeWith = (db: Database): Router => (target, form) => {
    if (form === "wiki") return byName(db, target) ? `/stone/${encodeURIComponent(target)}` : null;
    const hit = byPath(db, target);
    return hit ? `/at/${hit.path}` : null;
  };

  const stonePage = (db: Database, s: Row) => {
    const leansOn = db.query<{ name: string; path: string }, [number]>(
      `select st.name, st.path from link l join stone st on st.id=l.to_id
        where l.from_id=? group by st.id order by st.kind, st.name`,
    ).all(s.id);
    const leanedOn = db.query<{ name: string; path: string }, [number]>(
      `select st.name, st.path from link l join stone st on st.id=l.from_id
        where l.to_id=? group by st.id order by st.kind, st.name`,
    ).all(s.id);
    const logs = db.query<{ at: string; text: string; who: string }, [number]>(
      "select at,text,who from log where stone_id=? order by at",
    ).all(s.id);
    // The title and epigraph are shown by the shell, so they are dropped from
    // the body to avoid saying everything twice.
    const trimmed = s.body.replace(/^#\s+.*$/m, "").replace(/^\s*\*[^*].*\*\s*$/m, "");
    const dir = s.path.includes("/") ? s.path.slice(0, s.path.lastIndexOf("/")) : "";
    const links = (rows: { name: string; path: string }[]) =>
      rows.map((r) => `<a href="/at/${r.path}">${esc(r.name)}</a>`).join(" · ");

    return shell(s.title, `
<span class="kind">${esc(WING_NAMES[s.kind] ?? s.kind)}</span>
<h1>${esc(s.title)}</h1>
${s.epigraph ? `<p class="epigraph">${esc(s.epigraph)}</p>` : ""}
${toHtml(trimmed, dir, routeWith(db))}
<div class="near">
  ${leansOn.length ? `<h3>leans on</h3><p>${links(leansOn)}</p>` : ""}
  ${leanedOn.length ? `<h3>leaned on by</h3><p>${links(leanedOn)}</p>` : ""}
  ${logs.length ? `<h3>${logs.length} dated thought${logs.length === 1 ? "" : "s"}</h3><p class="quiet">first ${esc(logs[0].at)}, last ${esc(logs[logs.length - 1].at)}</p>` : ""}
  <h3>the file itself</h3><p class="quiet">${esc(CASTLE)}/${esc(s.path)}</p>
</div>`);
  };

  const server = serveOrExplain({
    hostname: "127.0.0.1", // never 0.0.0.0 — see the note at the top of this file
    port,
    // Said out loud rather than left to a default. With SO_REUSEPORT on, a
    // second `castle walk` binds the same port with no error and macOS hands it
    // all new connections — the first window goes silently dark. A lantern that
    // is on but lighting nothing is exactly the kind of lie this house does not
    // keep. bun 1.3.14 already refuses the second bind; this makes sure a
    // future default cannot change that quietly.
    reusePort: false,
    routes: {
      "/lantern.css": () => new Response(css, { headers: { "content-type": "text/css; charset=utf-8" } }),

      "/": async () => {
        const db = await fresh();
        const wings = db.query<{ kind: string; n: number }, []>(
          "select kind, count(*) n from stone group by kind order by n desc",
        ).all();
        const link = db.query<{ status: string; n: number }, []>(
          "select status, count(*) n from link group by status",
        ).all();
        const by = (s: string) => link.find((l) => l.status === s)?.n ?? 0;
        const unlaid = db.query<{ n: number }, []>(
          "select count(distinct target) n from link where status='unlaid'",
        ).get()!.n;
        const newest = db.query<{ name: string; path: string; kind: string }, []>(
          "select name, path, kind from stone where kind in ('word','room') order by mtime desc limit 8",
        ).all();

        return shell("the gate", `
<h1>The castle of understanding</h1>
<p class="epigraph">built of words, lit by questions — read here by lantern-light</p>
<table class="tally">
  ${wings.map((w) => `<tr><td class="n">${w.n}</td><td><a href="/wing/${w.kind}">${WING_NAMES[w.kind] ?? w.kind}</a></td></tr>`).join("")}
  <tr><td class="n">${by("stone")}</td><td>links that land on a stone</td></tr>
  <tr><td class="n">${unlaid}</td><td><a href="/owed">bricks named but never laid</a></td></tr>
  ${by("broken") ? `<tr><td class="n alarm">${by("broken")}</td><td><a href="/check">links pointing at nothing</a></td></tr>` : ""}
</table>
<h2>Newest stones</h2>
<p>${newest.map((s) => `<a href="/at/${s.path}">${esc(s.name)}</a>`).join(" · ")}</p>
<h2>Ways in</h2>
<ul>
  <li>Type words in the box above — it searches every stone, best first.</li>
  <li><a href="/wander">Wander</a> to a stone chosen at random.</li>
  <li><a href="/owed">What the castle owes itself</a> — words it leans on but has never written.</li>
  <li><a href="/check">The honest check</a> — what is broken, orphaned, or dated in the future.</li>
</ul>`);
      },

      "/stone/:name": async (req) => {
        const db = await fresh();
        const name = decodeURIComponent(req.params.name);
        const s = byName(db, name);
        return s ? stonePage(db, s) : notFound(`No stone is called “${name}”.`);
      },

      "/at/*": async (req) => {
        const db = await fresh();
        // bun 1.3.14 matches a `/at/*` route but leaves `req.params` empty for
        // the wildcard — verified, not assumed — so the path is taken from the
        // url itself.
        const path = decodeURIComponent(new URL(req.url).pathname.replace(/^\/at\//, ""));
        const s = byPath(db, path);
        return s ? stonePage(db, s) : notFound(`Nothing is filed at ${path}.`);
      },

      "/look": async (req) => {
        const db = await fresh();
        const asked = (new URL(req.url).searchParams.get("q") ?? "").trim();
        if (!asked) return shell("look", `<h1>Look</h1><p>Type words in the box above.</p>`, { seek: "" });
        // The box is one field, so whatever was typed is one phrase-or-terms
        // question — the same reading the terminal gives a quoted argument.
        const query = asFts(asked, /\s/.test(asked));
        let hits: ReturnType<typeof look> = [];
        let trouble = "";
        try {
          hits = look(db, query, 40);
        } catch (e) {
          trouble = (e as Error).message;
        }
        return shell(`look: ${asked}`, `
<h1>${esc(asked)}</h1>
${trouble ? `<p class="alarm">SQLite could not read that search: ${esc(trouble)}</p><p class="quiet">Plain words always work. So does a quoted phrase.</p>` : ""}
${!trouble && !hits.length ? `<p>Nothing in the castle says that.</p>` : ""}
${hits.map((h) => `<div class="hit">
  <a class="name" href="/at/${h.path}">${esc(h.name)}</a><span class="where">${WING_NAMES[h.kind] ?? h.kind}</span>
  <div class="snip">${esc(h.snippet).replace(/«/g, "<mark>").replace(/»/g, "</mark>")}</div>
</div>`).join("")}
${hits.length ? `<p class="quiet">${hits.length} stone${hits.length === 1 ? "" : "s"}, best first.</p>` : ""}`,
          { seek: asked, wide: true });
      },

      "/wing/:kind": async (req) => {
        const db = await fresh();
        const kind = req.params.kind;
        const rows = db.query<{ name: string; path: string; title: string; epigraph: string }, [string]>(
          "select name,path,title,epigraph from stone where kind=? order by name",
        ).all(kind);
        if (!rows.length) return notFound(`There is no wing called “${kind}”.`);
        return shell(WING_NAMES[kind] ?? kind, `
<h1>${esc(WING_NAMES[kind] ?? kind)}</h1>
<p class="quiet">${rows.length} stones, in the order the shelf keeps them.</p>
${rows.map((r) => `<div class="hit"><a class="name" href="/at/${r.path}">${esc(r.name)}</a>${r.epigraph ? `<div class="snip">${esc(r.epigraph)}</div>` : ""}</div>`).join("")}`,
          { wide: true });
      },

      "/owed": async () => {
        const db = await fresh();
        const rows = db.query<{ target: string; times: number; leaners: string }, []>(
          `select l.target, count(*) times, group_concat(distinct s.name) leaners
             from link l join stone s on s.id=l.from_id
            where l.status='unlaid' group by l.target order by times desc, l.target`,
        ).all();
        return shell("owed", `
<h1>What the castle owes itself</h1>
<p class="epigraph">words the walls lean on that nobody has written yet</p>
<p>${rows.length} names are linked to as bricks with no <code>words/&lt;name&gt;.md</code> behind them.
These are not faults. They are the castle's own list of what to write next, and the ones leaned on
hardest are the ones most worth writing.</p>
<table class="tally">${rows.map((r) => `<tr><td class="n">${r.times}</td><td><strong>${esc(r.target)}</strong>
  <div class="quiet">leaned on by ${r.leaners.split(",").slice(0, 6).map((n) => `<a href="/stone/${encodeURIComponent(n)}">${esc(n)}</a>`).join(", ")}${r.leaners.split(",").length > 6 ? ", …" : ""}</div></td></tr>`).join("")}</table>`,
          { wide: true });
      },

      "/check": async () => {
        const db = await fresh();
        const broken = db.query<{ from_: string; target: string }, []>(
          `select s.path from_, l.target from link l join stone s on s.id=l.from_id
            where l.status='broken' order by s.path`,
        ).all();
        const orphans = db.query<{ path: string; name: string }, []>(
          `select path, name from stone where kind in ('word','room')
             and id not in (select to_id from link where to_id is not null) order by path`,
        ).all();
        const ahead = db.query<{ path: string; at: string }, []>(
          `select s.path, l.at from log l join stone s on s.id=l.stone_id
            where date(substr(l.at,1,10)) > date('now') order by l.at desc`,
        ).all();
        return shell("check", `
<h1>The castle, checked</h1>
<p class="epigraph">nothing below was changed — this only looks</p>
<h2>${broken.length ? `<span class="alarm">${broken.length} links point at nothing</span>` : "Every link points at something real"}</h2>
${broken.length ? `<ul>${broken.map((b) => `<li><a href="/at/${b.from_}">${esc(b.from_)}</a> → <code>${esc(b.target)}</code></li>`).join("")}</ul>` : ""}
${ahead.length ? `<h2><span class="alarm">${ahead.length} dated thoughts sit in the future</span></h2>
<p>The latest is <code>${esc(ahead[0].at)}</code> in <a href="/at/${ahead[0].path}">${esc(ahead[0].path)}</a>.
A record cannot be written after the day it records, so some rhythm's clock is ahead
or a date was typed by hand.</p>` : ""}
<h2>${orphans.length} words or rooms nothing links to</h2>
<p>Reachable only by knowing the name. Sometimes standing alone is right.</p>
<p>${orphans.map((o) => `<a href="/at/${o.path}">${esc(o.name)}</a>`).join(" · ")}</p>
<h2>Not looked at</h2>
<ul>
  <li>Whether anything here is <em>true</em> — that is <code>~/truth</code>'s work, and a person's.</li>
  <li>The links out to the web. The lantern never leaves the castle.</li>
  <li><code>garden/</code> and <code>front/</code>, which are machinery and artifact.</li>
</ul>`,
          { wide: true });
      },

      "/wander": async () => {
        const db = await fresh();
        const s = db.query<Row, []>(
          `select id,kind,name,path,title,epigraph,body from stone
            where kind in ('word','room') order by random() limit 1`,
        ).get()!;
        return stonePage(db, s);
      },
    },
    fetch: (req) => notFound(`There is no door at ${esc(new URL(req.url).pathname)}.`),
  });

  if (!quiet) {
    console.log(`
  the castle is lit at http://127.0.0.1:${server.port}

  this Mac only — nothing outside can reach it
  nothing it shows can change the castle
  Ctrl-C puts the lantern out
`);

    // The off-switch. Nothing here outlives the window you started it in.
    const putOut = () => {
      server.stop();
      try { held.db.close(); } catch {}
      console.log("  the lantern is out.\n");
      process.exit(0);
    };
    process.on("SIGINT", putOut);
    process.on("SIGTERM", putOut);
  }

  return server;
}
