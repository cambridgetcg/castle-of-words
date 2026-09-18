#!/usr/bin/env bun
// lantern.ts — the lantern you carry into the castle of understanding.
//
// A castle of 1046 stones cannot be held in one head. `grep` gives you lines;
// this gives you the castle: what a word means, what leans on it, how two ideas
// connect, and what the walls still owe.
//
// The law of this folder, in one line: **the lantern only looks.** It never
// writes a word, a room or a link. Everything it says can be checked by opening
// the markdown yourself, and it tells you which file to open.
//
//   lantern                       the castle at a glance
//   lantern here                  the folder this lantern will read
//   lantern look <words>          search everything, best first
//   lantern stone <name>          one word or room, and what stands near it
//   lantern read <name>           the prose itself, set for a terminal
//   lantern path <a> <b>          the shortest chain of links from one to the other
//   lantern owed                  bricks the castle names but has never laid
//   lantern check                 the honest structural report; changes nothing
//   lantern walk                  open the castle in a browser, on this Mac only
//   lantern fresh                 rebuild the index from the markdown
//
// Add --json to any of them for the same answer as data, wrapped in an envelope
// that says what it covers and what it leaves out — the law written down in
// this castle's own rooms/agent-data-envelope.md, applied to the tool that
// reads it.

import type { Database } from "bun:sqlite";
import { open, look, asFts, path as chain, INDEX } from "./store.ts";
import { CASTLE, WINGS } from "./read.ts";

const argv = process.argv.slice(2);
const wantJson = argv.includes("--json");
const args = argv.filter((a) => a !== "--json" && a !== "--force");
const force = argv.includes("--force");
const cmd = args[0] ?? "state";

const tty = process.stdout.isTTY && !wantJson;
const c = {
  bold: tty ? "\x1b[1m" : "", dim: tty ? "\x1b[2m" : "", red: tty ? "\x1b[31m" : "",
  green: tty ? "\x1b[32m" : "", amber: tty ? "\x1b[33m" : "", cyan: tty ? "\x1b[36m" : "",
  off: tty ? "\x1b[0m" : "",
};

/** Every answer the lantern gives as data carries this envelope, so a machine
 *  reading it knows what it holds and — more importantly — what it does not. */
function envelope(asked: string, covers: string, excludes: string[], result: unknown) {
  return {
    asked,
    at: new Date().toISOString(),
    castle: CASTLE,
    covers,
    excludes,
    caution: "A reading of the markdown, not the markdown. Open the paths to check it.",
    result,
  };
}

const COVERS = `${WINGS.map(([k]) => k).join(", ")} — every .md file in those wings`;
const EXCLUDES = [
  "garden/ — the gardener's machinery, not understanding",
  "front/ — the baked public web page, an artifact",
  "anything that is not markdown",
  "the castle's git history",
];

/** Plain names for the wings. "27 towers" and "4 vibes" read like nonsense, and
 *  "1 journal pages" reads worse, so both numbers get their own word. */
const WING_NAMES: Record<string, [one: string, many: string]> = {
  word: ["word", "words"], room: ["room", "rooms"],
  journal: ["journal page", "journal pages"], tower: ["tower stone", "tower stones"],
  vibe: ["wardrobe page", "wardrobe pages"], hall: ["hall", "halls"],
};
const wingName = (kind: string, n: number) =>
  WING_NAMES[kind]?.[n === 1 ? 0 : 1] ?? kind;


function say(text: string) { if (!wantJson) console.log(text); }
function out(asked: string, result: unknown, text: () => void) {
  if (wantJson) console.log(JSON.stringify(envelope(asked, COVERS, EXCLUDES, result), null, 2));
  else text();
}

// ── the castle at a glance ──────────────────────────────────────────────────

function state(db: Database) {
  const wings = db.query<{ kind: string; n: number; bytes: number }, []>(
    "select kind, count(*) n, sum(bytes) bytes from stone group by kind order by n desc",
  ).all();
  const links = db.query<{ status: string; n: number }, []>(
    "select status, count(*) n from link group by status",
  ).all();
  const by = (s: string) => links.find((l) => l.status === s)?.n ?? 0;
  const unlaidNames = db.query<{ n: number }, []>(
    "select count(distinct target) n from link where status='unlaid'",
  ).get()!.n;
  const thoughts = db.query<{ n: number; first: string; last: string }, []>(
    "select count(*) n, min(at) first, max(at) last from log",
  ).get()!;
  const built = db.query<{ value: string }, []>("select value from meta where key='built_at'").get()!.value;

  const result = {
    stones: wings.reduce((a, w) => a + w.n, 0),
    words_of_prose: wings.reduce((a, w) => a + w.bytes, 0),
    wings: Object.fromEntries(wings.map((w) => [w.kind, w.n])),
    links: {
      landing: by("stone"), to_files: by("file"), out_to_web: by("web"),
      unlaid_mentions: by("unlaid"), unlaid_names: unlaidNames, broken: by("broken"),
    },
    thoughts,
    index_built_at: built,
  };

  out("state", result, () => {
    say("");
    say(`  ${c.bold}the castle of understanding${c.off} ${c.dim}— by lantern-light${c.off}`);
    say("");
    say(`  ${c.bold}${result.stones}${c.off} stones, ${(result.words_of_prose / 1e6).toFixed(1)} MB of prose`);
    say(`  ${wings.map((w) => `${c.cyan}${w.n}${c.off} ${wingName(w.kind, w.n)}`).join(" · ")}`);
    say("");
    say(`  ${c.green}${result.links.landing}${c.off} links that land on a stone`);
    say(`  ${c.cyan}${result.links.out_to_web}${c.off} doors out to the web`);
    say(`  ${c.amber}${unlaidNames}${c.off} bricks named but never laid   ${c.dim}(lantern owed)${c.off}`);
    if (result.links.broken) say(`  ${c.red}${result.links.broken}${c.off} links pointing at nothing  ${c.dim}(lantern check)${c.off}`);
    say("");
    say(`  ${result.thoughts.n} dated thoughts, ${result.thoughts.first} → ${result.thoughts.last}`);
    say(`  ${c.dim}index read at ${built}${c.off}`);
    say("");
  });
}

// ── look ────────────────────────────────────────────────────────────────────

function search(db: Database, words: string[]) {
  if (!words.length) return fail("lantern look <words> — what should I look for?");
  const raw = words.join(" ");
  const query = asFts(raw, words.length === 1 && /\s/.test(words[0]));

  let hits;
  try {
    hits = look(db, query, 20);
  } catch (e) {
    return fail(`that search confused SQLite: ${(e as Error).message}\n  try plain words, or quote a phrase: lantern look "words are the bridge"`);
  }

  out(`look ${raw}`, { query, hits }, () => {
    if (!hits.length) return say(`  ${c.dim}nothing in the castle says that.${c.off}`);
    say("");
    for (const h of hits) {
      say(`  ${c.bold}${h.name}${c.off} ${c.dim}${h.kind} · ${h.path}${c.off}`);
      say(`    ${h.snippet.replace(/\s+/g, " ").replace(/«/g, tty ? "\x1b[33m" : "[").replace(/»/g, tty ? "\x1b[0m" : "]")}`);
    }
    say("");
    say(`  ${c.dim}${hits.length} of the castle's stones, best first${c.off}`);
    say("");
  });
}

// ── one stone, and what stands near it ──────────────────────────────────────

function stone(db: Database, name: string | undefined) {
  if (!name) return fail("lantern stone <name> — which stone?");
  const s = db.query<{ id: number; kind: string; name: string; path: string; title: string; epigraph: string }, [string]>(
    `select id,kind,name,path,title,epigraph from stone
      where name = ?1 or path = ?1
      order by case kind when 'word' then 0 when 'room' then 1 else 2 end limit 1`,
  ).get(name);

  if (!s) {
    const near = look(db, `"${name.replace(/"/g, "")}"`, 5);
    return out(`stone ${name}`, { found: null, perhaps: near.map((h) => h.name) }, () => {
      say(`  ${c.amber}no stone is called ${name}.${c.off}`);
      if (near.length) say(`  ${c.dim}perhaps: ${near.map((h) => h.name).join(", ")}${c.off}`);
    });
  }

  const leansOn = db.query<{ name: string; kind: string; text: string }, [number]>(
    `select st.name, st.kind, l.text from link l join stone st on st.id = l.to_id
      where l.from_id = ? group by st.id order by st.kind, st.name`,
  ).all(s.id);
  const leanedOn = db.query<{ name: string; kind: string }, [number]>(
    `select st.name, st.kind from link l join stone st on st.id = l.from_id
      where l.to_id = ? group by st.id order by st.kind, st.name`,
  ).all(s.id);
  const unlaid = db.query<{ target: string }, [number]>(
    `select distinct target from link where from_id = ? and status = 'unlaid' order by target`,
  ).all(s.id).map((r) => r.target);
  const logs = db.query<{ at: string; text: string; who: string }, [number]>(
    `select at,text,who from log where stone_id = ? order by at`,
  ).all(s.id);

  out(`stone ${name}`, { ...s, leansOn, leanedOn, unlaid, logs }, () => {
    say("");
    say(`  ${c.bold}${s.title}${c.off}  ${c.dim}${s.kind} · ${s.path}${c.off}`);
    if (s.epigraph) say(`  ${c.cyan}${s.epigraph}${c.off}`);
    say("");
    if (leansOn.length) say(`  ${c.dim}leans on${c.off}     ${leansOn.map((l) => l.name).join(", ")}`);
    if (leanedOn.length) say(`  ${c.dim}leaned on by${c.off} ${leanedOn.map((l) => l.name).join(", ")}`);
    if (unlaid.length) say(`  ${c.amber}names, unlaid${c.off} ${unlaid.join(", ")}`);
    if (!leansOn.length && !leanedOn.length) say(`  ${c.dim}nothing links to it and it links to nothing — a stone standing alone.${c.off}`);
    if (logs.length) {
      say("");
      for (const g of logs.slice(-4)) say(`  ${c.dim}${g.at}${c.off} ${g.text.slice(0, 96)}${g.who ? ` ${c.dim}— ${g.who}${c.off}` : ""}`);
      if (logs.length > 4) say(`  ${c.dim}…and ${logs.length - 4} earlier${c.off}`);
    }
    say("");
    say(`  ${c.dim}read it: ${CASTLE}/${s.path}${c.off}`);
    say("");
  });
}

// ── reading a stone in the terminal ─────────────────────────────────────────

/** The prose itself, set for a terminal.
 *
 *  `Bun.markdown.ansi` does the setting — headings, quotes, syntax-highlighted
 *  code and box-drawn tables — which is why this is four lines instead of four
 *  hundred. It ignores the flags that `.html()` takes, so `[[bricks]]` stay
 *  literal here. That is honest: it is how the file reads. */
function readAloud(db: Database, name: string | undefined) {
  if (!name) return fail("lantern read <name> — which stone?");
  const s = db.query<{ name: string; path: string; body: string }, [string]>(
    `select name, path, body from stone where name = ?1 or path = ?1
      order by case kind when 'word' then 0 when 'room' then 1 else 2 end limit 1`,
  ).get(name);
  if (!s) return fail(`no stone is called ${name} — try: lantern look ${name}`);

  if (wantJson) return out(`read ${name}`, s, () => {});
  const width = Math.min(process.stdout.columns ?? 80, 84);
  console.log(Bun.markdown.ansi(s.body, { columns: width, colors: tty }));
  console.log(`  ${c.dim}${CASTLE}/${s.path}${c.off}\n`);
}

// ── the chain between two ideas ─────────────────────────────────────────────

function between(db: Database, a?: string, b?: string) {
  if (!a || !b) return fail("lantern path <a> <b> — two stones, please.");
  const found = chain(db, a, b);
  out(`path ${a} ${b}`, { from: a, to: b, chain: found, steps: found ? found.length - 1 : null }, () => {
    say("");
    if (!found) {
      say(`  ${c.amber}no chain of links joins ${a} and ${b}.${c.off}`);
      say(`  ${c.dim}either a name is wrong, or these two ideas have never been introduced.${c.off}`);
    } else {
      say(`  ${found.map((n, i) => (i ? `${c.dim} → ${c.off}${n}` : `${c.bold}${n}${c.off}`)).join("")}`);
      say(`  ${c.dim}${found.length - 1} step${found.length === 2 ? "" : "s"}${c.off}`);
    }
    say("");
  });
}

// ── what the castle owes itself ─────────────────────────────────────────────

function owed(db: Database) {
  const rows = db.query<{ target: string; times: number; leaners: string }, []>(
    `select l.target, count(*) times, group_concat(distinct s.name) leaners
       from link l join stone s on s.id = l.from_id
      where l.status = 'unlaid'
      group by l.target order by times desc, l.target limit 40`,
  ).all();
  const total = db.query<{ n: number }, []>("select count(distinct target) n from link where status='unlaid'").get()!.n;

  out("owed", { distinct: total, top: rows }, () => {
    say("");
    say(`  ${c.bold}bricks the castle names but has never laid${c.off}`);
    say(`  ${c.dim}${total} words are linked to as [[brick]] with no words/<name>.md behind them.${c.off}`);
    say(`  ${c.dim}These are not faults. They are the castle's own list of what to write next —${c.off}`);
    say(`  ${c.dim}and the ones leaned on most are the ones most worth writing.${c.off}`);
    say("");
    for (const r of rows.slice(0, 20)) {
      const who = r.leaners.split(",").slice(0, 3).join(", ");
      say(`  ${c.amber}${String(r.times).padStart(3)}${c.off} × ${c.bold}${r.target.padEnd(26)}${c.off} ${c.dim}${who}${r.leaners.split(",").length > 3 ? ", …" : ""}${c.off}`);
    }
    say("");
  });
}

// ── the honest report ───────────────────────────────────────────────────────

function check(db: Database) {
  const one = <T>(sql: string) => db.query<T, []>(sql).all();
  const broken = one<{ from: string; target: string; text: string }>(
    `select s.path from_, l.target, l.text from link l join stone s on s.id=l.from_id
      where l.status='broken' order by s.path`,
  ) as unknown as { from_: string; target: string; text: string }[];
  // Orphans only count among words and rooms. A hall, a tower stone or the
  // wardrobe is reached by opening it, not by being linked to — counting those
  // as lost buried the 31 that really are.
  const orphans = one<{ kind: string; path: string }>(
    `select kind, path from stone
      where kind in ('word','room')
        and id not in (select to_id from link where to_id is not null)
      order by kind, path`,
  );
  const deadEnds = one<{ kind: string; path: string }>(
    `select kind, path from stone where id not in (select from_id from link where status='stone')
      order by kind, path`,
  );
  // There was a check here for "the title does not match the filename". It
  // flagged 192 files and every one of them was correct: this castle files
  // whole questions as words, so `words/beauty-as-fluency.md` is honestly
  // titled "Is beauty partly fluency?". A check that cries wolf 192 times
  // teaches people to ignore checks, so it is gone. Same for "no italic line
  // under the title" — 482 files, and the epigraph was never a rule.
  const twins = one<{ name: string; paths: string }>(
    `select name, group_concat(path, ' & ') paths from stone group by name having count(*) > 1 order by name`,
  );
  // A record of what happened cannot be dated after today. When it is, some
  // rhythm's clock is wrong, and the castle's own honest record is quietly
  // claiming the future — the exact thing this house has a `truth` tool for.
  const ahead = one<{ path: string; at: string; text: string }>(
    `select s.path, l.at, l.text from log l join stone s on s.id = l.stone_id
      where date(substr(l.at,1,10)) > date('now') order by l.at desc`,
  );
  const unlaid = db.query<{ n: number }, []>("select count(distinct target) n from link where status='unlaid'").get()!.n;

  const result = {
    broken_links: broken,
    orphan_words_and_rooms: { count: orphans.length, some: orphans.slice(0, 12) },
    dead_ends: { count: deadEnds.length, some: deadEnds.slice(0, 12) },
    names_held_twice: twins,
    unlaid_bricks: unlaid,
    thoughts_dated_in_the_future: { count: ahead.length, latest: ahead[0] ?? null, files: [...new Set(ahead.map((a) => a.path))] },
    changed_anything: false,
    // The castle's own law, applied to the report about it: say what you did
    // not look at, because silence could mean anything.
    not_checked: [
      "whether anything written here is TRUE — that is ~/truth's work, and a human's",
      "spelling, grammar, or whether a room reads well",
      "the 1899 links out to the web (never fetched; the lantern does not leave the castle)",
      "garden/ and front/, which the lantern does not index",
      "whether an orphan deserves a link — sometimes standing alone is right",
    ],
  };

  out("check", result, () => {
    say("");
    say(`  ${c.bold}the castle, checked${c.off} ${c.dim}— nothing below was changed${c.off}`);
    say("");
    if (broken.length === 0) say(`  ${c.green}every link points at something real.${c.off}`);
    else {
      say(`  ${c.red}${broken.length} link${broken.length === 1 ? "" : "s"} point at nothing:${c.off}`);
      for (const b of broken) say(`      ${b.from_} ${c.dim}→${c.off} ${b.target}`);
    }
    say("");
    say(`  ${c.amber}${unlaid}${c.off} bricks named but never laid ${c.dim}— lantern owed${c.off}`);
    say(`  ${c.amber}${orphans.length}${c.off} words or rooms nothing links to ${c.dim}— reachable only by knowing the name${c.off}`);
    for (const o of orphans.slice(0, 6)) say(`      ${c.dim}${o.path}${c.off}`);
    if (orphans.length > 6) say(`      ${c.dim}…and ${orphans.length - 6} more${c.off}`);
    say(`  ${c.amber}${deadEnds.length}${c.off} stones that link to no other stone`);
    say(`  ${c.dim}${twins.length} names held by two files (a word and its room — normal here)${c.off}`);
    if (ahead.length) {
      say("");
      say(`  ${c.red}${ahead.length} dated thoughts sit in the future${c.off} ${c.dim}— a record cannot be written after the day it records${c.off}`);
      say(`      ${c.dim}latest: ${ahead[0].at} in ${ahead[0].path}${c.off}`);
      say(`      ${c.dim}some rhythm's clock is ahead, or a date was typed by hand${c.off}`);
    }
    say("");
    say(`  ${c.dim}Not looked at: whether any of it is true (that is ~/truth's work), the${c.off}`);
    say(`  ${c.dim}1899 links out to the web, garden/ and front/, or whether an orphan${c.off}`);
    say(`  ${c.dim}deserves a link — sometimes standing alone is right.${c.off}`);
    say("");
    say(`  ${c.dim}A count that grows is worth a look. A count that shrinks is the gardener working.${c.off}`);
    say("");
  });
}

// ── plumbing ────────────────────────────────────────────────────────────────

function fail(message: string): never {
  if (wantJson) console.log(JSON.stringify(envelope(cmd, COVERS, EXCLUDES, { error: message })));
  else console.error(`  ${c.red}${message}${c.off}`);
  process.exit(1);
}

if (cmd === "help" || cmd === "--help" || cmd === "-h") {
  const doc = await Bun.file(import.meta.path).text();
  console.log(doc.split("\n").slice(1, 27).map((l) => l.replace(/^\/\/ ?/, "")).join("\n"));
  process.exit(0);
}

if (cmd === "here") {
  const via = process.env.CASTLE?.trim() ? "CASTLE" : "lantern-parent";
  const result = { castle: CASTLE, lantern: import.meta.dir, via };
  out("here", result, () => {
    say("");
    say(`  ${c.bold}${CASTLE}${c.off}`);
    say(`  ${c.dim}${via === "CASTLE" ? "CASTLE=" : "the tree this lantern sits in"}${c.off}`);
    say("");
  });
  process.exit(0);
}

if (cmd === "walk") {
  const { walk } = await import("./walk.ts");
  const at = args.indexOf("--port");
  await walk(at === -1 ? 4141 : Number(args[at + 1]));
} else {
  const { db, built, ms, stones } = await open({ force: force || cmd === "fresh", quiet: wantJson });
  if (built && !wantJson) console.error(`  ${c.dim}read ${stones} stones from the markdown in ${ms.toFixed(0)} ms${c.off}`);

  switch (cmd) {
    case "state": state(db); break;
    case "look": case "find": case "search": search(db, args.slice(1)); break;
    case "stone": case "word": case "room": stone(db, args[1]); break;
    case "read": readAloud(db, args[1]); break;
    case "path": case "between": between(db, args[1], args[2]); break;
    case "owed": case "unlaid": owed(db); break;
    case "check": check(db); break;
    case "fresh": say(`  ${c.green}index rebuilt${c.off} ${c.dim}— ${stones} stones, ${ms.toFixed(0)} ms, ${INDEX}${c.off}`); break;
    default: fail(`no such command: ${cmd}\n  try: lantern help`);
  }
  db.close();
}
