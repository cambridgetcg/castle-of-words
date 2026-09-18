// read.ts — reading the castle exactly as it is.
//
// The castle is plain markdown and stays plain markdown. This file is the only
// place that knows how to turn those files into something a machine can query:
// a list of stones, and the links between them. Nothing here ever writes.
//
// The conventions it relies on were not invented here — they were counted in
// the castle as it stands on 2026-07-26 (576 words, 424 rooms). Where the
// castle is inconsistent, this file says so out loud rather than guessing.

import { dirname } from "node:path";
import { Glob } from "bun";

/** Decide which tree the lantern will read.
 *
 *  `CASTLE=` wins when it is set and not blank. Otherwise the castle is the
 *  folder that holds this `lantern/` directory — so a clone or a worktree is
 *  already home. `$HOME/castle` is not assumed; that path was a local habit,
 *  not a property of the castle.
 */
export function resolveCastle(env: { CASTLE?: string } = process.env): string {
  const fromEnv = env.CASTLE?.trim();
  if (fromEnv) return fromEnv;
  return dirname(import.meta.dir);
}

export const CASTLE = resolveCastle();

/** The six wings, and the glob that finds each one's files.
 *
 *  Deliberately NOT indexed:
 *  - `garden/`  — the gardener's machinery, not understanding.
 *  - `front/`   — a 2 MB baked web page; an artifact, not a source.
 *  - anything not ending in .md — the castle is words.
 */
export const WINGS = [
  ["word", "words/*.md"],
  ["room", "rooms/*.md"],
  ["journal", "journal/*.md"],
  ["tower", "tower/**/*.md"],
  ["vibe", "vibe/*.md"],
  ["hall", "*.md"],
] as const;

export type Kind = (typeof WINGS)[number][0];

export type Link = {
  /** `wiki` = [[brick]] · `path` = [text](room.md) · `web` = http(s) */
  form: "wiki" | "path" | "web";
  /** exactly as written, so a report can quote the real line */
  raw: string;
  /** wiki: the bare name · path: castle-relative path · web: the url */
  target: string;
  /** the words a reader actually sees */
  text: string;
};

/** A dated thought filed into a room, e.g.
 *  `- 2026-07-13 11:15 · A shared data resolver is not yet … — yu` */
export type Log = { at: string; text: string; who: string };

export type Stone = {
  kind: Kind;
  /** file basename without .md — the name links use */
  name: string;
  /** castle-relative path, e.g. `rooms/honesty.md` */
  path: string;
  title: string;
  /** the italic line under the title, if there is one */
  epigraph: string;
  body: string;
  bytes: number;
  mtime: number;
  links: Link[];
  logs: Log[];
};

// ── Finding the files ───────────────────────────────────────────────────────

/** Every markdown file in the six wings, with its wing. Order is stable so two
 *  runs of the lantern report the same thing in the same order. */
export async function findFiles(root = CASTLE): Promise<{ kind: Kind; path: string }[]> {
  const seen = new Set<string>();
  const out: { kind: Kind; path: string }[] = [];
  for (const [kind, pattern] of WINGS) {
    const found: string[] = [];
    for await (const p of new Glob(pattern).scan({ cwd: root, onlyFiles: true })) found.push(p);
    for (const p of found.sort()) {
      if (seen.has(p)) continue; // first wing wins; `*.md` is last, so it only gets the halls
      seen.add(p);
      out.push({ kind, path: p });
    }
  }
  return out;
}

// ── Reading one file ────────────────────────────────────────────────────────

const RE_WIKI = /\[\[([^\]|#]+?)(?:\|([^\]]+?))?\]\]/g;
const RE_MD_LINK = /\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g;
// A dated thought. Time is optional; the author is whatever follows the LAST
// em-dash, because thoughts themselves often contain em-dashes.
const RE_LOG = /^-\s+(\d{4}-\d{2}-\d{2}(?:\s+\d{2}:\d{2})?)\s*·\s*(.+)$/;

/** Turn one file's text into a stone. Pure — give it text, get a stone. */
export function readStone(
  kind: Kind,
  path: string,
  text: string,
  bytes: number,
  mtime: number,
): Stone {
  const name = path.split("/").pop()!.replace(/\.md$/, "");
  const lines = text.split("\n");

  // Title: the first `# ` heading. Files without one fall back to their name,
  // and `check` reports them — a stone should say what it is.
  let title = "";
  let titleAt = -1;
  for (let i = 0; i < lines.length; i++) {
    const m = /^#\s+(.+?)\s*$/.exec(lines[i]);
    if (m) {
      title = m[1];
      titleAt = i;
      break;
    }
  }
  if (!title) title = name;

  // Epigraph: the first non-empty line after the title, if it is wholly italic.
  let epigraph = "";
  for (let i = titleAt + 1; i < Math.min(lines.length, titleAt + 4); i++) {
    const l = lines[i].trim();
    if (!l) continue;
    const m = /^\*([^*].*[^*])\*$/.exec(l);
    if (m) epigraph = m[1];
    break;
  }

  // Links. Wiki-bricks and markdown links are collected separately because they
  // resolve differently: a brick names a stone anywhere in the castle, a
  // markdown path is relative to the file that wrote it.
  const links: Link[] = [];
  const dir = path.includes("/") ? path.slice(0, path.lastIndexOf("/")) : "";

  for (const m of text.matchAll(RE_WIKI)) {
    links.push({
      form: "wiki",
      raw: m[0],
      target: m[1].trim(),
      text: (m[2] ?? m[1]).trim(),
    });
  }

  for (const m of text.matchAll(RE_MD_LINK)) {
    const href = m[2].trim();
    if (/^(https?|mailto):/.test(href)) {
      links.push({ form: "web", raw: m[0], target: href, text: m[1] });
      continue;
    }
    if (href.startsWith("#")) continue; // a jump inside the same page, not a link between stones
    links.push({
      form: "path",
      raw: m[0],
      target: normalize(dir, href.split("#")[0]),
      text: m[1],
    });
  }

  // A url written plainly in the prose is still a door out of the castle, and
  // the browser view already turns it into one. Counting only the bracketed
  // kind made "doors out to the web" quietly too small, so both kinds count.
  //
  // Fenced blocks, code spans and already-bracketed links are blanked out
  // first, so nothing is counted twice and an example url inside backticks
  // stays an example.
  const bare = text
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/`[^`]*`/g, " ")
    .replace(RE_MD_LINK, " ");
  for (const m of bare.matchAll(/(?<![\w<("])(https?:\/\/[^\s<>)\]"']+)/g)) {
    // Trailing punctuation belongs to the sentence, not the address.
    const url = m[1].replace(/[.,;:!?·]+$/, "");
    links.push({ form: "web", raw: url, target: url, text: url });
  }

  // Dated thoughts.
  const logs: Log[] = [];
  for (const line of lines) {
    const m = RE_LOG.exec(line.trim());
    if (!m) continue;
    const rest = m[2];
    const cut = rest.lastIndexOf(" — ");
    logs.push(
      cut === -1
        ? { at: m[1], text: rest.trim(), who: "" }
        : { at: m[1], text: rest.slice(0, cut).trim(), who: rest.slice(cut + 3).trim() },
    );
  }

  return { kind, name, path, title, epigraph, body: text, bytes, mtime, links, logs };
}

/** Resolve a relative markdown href against the directory it was written in.
 *  Returns a castle-relative path with no `.` or `..` left in it. */
export function normalize(dir: string, href: string): string {
  const parts = (dir ? dir.split("/") : []).concat(href.split("/"));
  const out: string[] = [];
  for (const p of parts) {
    if (!p || p === ".") continue;
    if (p === "..") out.pop();
    else out.push(p);
  }
  return out.join("/");
}

// ── Reading the whole castle ────────────────────────────────────────────────

export type Castle = {
  stones: Stone[];
  /** name → stone. Wings are preferred in WINGS order, so a brick means the
   *  word first, then the room. Collisions are kept in `ambiguous`. */
  byName: Map<string, Stone>;
  byPath: Map<string, Stone>;
  ambiguous: Map<string, string[]>;
  /** Every path that really exists in the castle, files and folders both.
   *
   *  Needed because a link may legitimately point at something the lantern
   *  does not index: `README.md` links to the `rooms` folder, `vibe/arts.md`
   *  links to the baked `front/index.html`. Judging those by the index alone
   *  called five honest links broken. A link is only broken if nothing is
   *  there. */
  onDisk: Set<string>;
};

export async function readCastle(root = CASTLE): Promise<Castle> {
  const files = await findFiles(root);
  const onDisk = new Set<string>();
  for await (const p of new Glob("**/*").scan({ cwd: root, onlyFiles: false, dot: false })) {
    if (p.startsWith(".git/")) continue;
    onDisk.add(p);
  }

  // 1000 small files: read them all at once and let bun's io do the waiting.
  const stones = await Promise.all(
    files.map(async ({ kind, path }) => {
      const f = Bun.file(`${root}/${path}`);
      const [text, stat] = await Promise.all([f.text(), f.stat()]);
      return readStone(kind, path, text, stat.size, stat.mtimeMs);
    }),
  );

  const byName = new Map<string, Stone>();
  const byPath = new Map<string, Stone>();
  const ambiguous = new Map<string, string[]>();
  for (const s of stones) {
    byPath.set(s.path, s);
    const held = byName.get(s.name);
    if (!held) byName.set(s.name, s);
    else ambiguous.set(s.name, [held.path, s.path]);
  }

  return { stones, byName, byPath, ambiguous, onDisk };
}

/** Which stone a link lands on, or null if it lands on no *stone*.
 *  Null does not mean broken — see `linkStatus`. */
export function resolve(castle: Castle, link: Link): Stone | null {
  if (link.form === "web") return null;
  if (link.form === "wiki") return castle.byName.get(link.target) ?? null;
  return castle.byPath.get(link.target) ?? null;
}

/** The honest verdict on one link.
 *
 *  `stone`   — lands on an indexed stone.
 *  `file`    — lands on something real that the lantern does not index
 *              (a folder, the baked front page). Fine. Not a fault.
 *  `unlaid`  — a [[brick]] naming a word the castle has not written yet.
 *              These are not errors; they are the castle's own list of
 *              debts, and the most-leaned-on one is the best next word.
 *  `broken`  — a path link pointing at nothing at all. A real fault.
 *  `web`     — leaves the castle; the lantern does not follow it. */
export function linkStatus(
  castle: Castle,
  link: Link,
): "stone" | "file" | "unlaid" | "broken" | "web" {
  if (link.form === "web") return "web";
  if (resolve(castle, link)) return "stone";
  if (link.form === "wiki") return "unlaid";
  return castle.onDisk.has(link.target) ? "file" : "broken";
}
