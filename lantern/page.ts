// page.ts — turning the castle's markdown into a page you can read in a browser.
//
// This started as a hand-written renderer. It was replaced once I found that
// bun 1.3 ships one: `Bun.markdown.html`, which is not in `bun --help` and is
// not in the docs, but is real, fast (210 MB/s) and understands the three
// things the hand-written one could not — tables (7 rooms use them), task
// lists (5), and strikethrough (15). Those 27 stones used to come out as
// plain text.
//
// It is used with care, because it is not safe by default. Three things had to
// be checked by running them rather than trusting them:
//
//  1. `noHtmlBlocks` ALONE does not neutralise raw HTML — `<script>alert(1)</script>`
//     merely becomes `<p><script>alert(1)</script></p>`, still live. BOTH
//     `noHtmlBlocks` and `noHtmlSpans` are needed. With both, raw HTML comes out
//     escaped, as visible text. Verified on this machine, 2026-07-26.
//  2. Even with both, `[click](javascript:alert(1))` and a `data:` image are
//     emitted untouched. There is no option for it. The scheme allowlist below
//     is hand-written for exactly that reason, and it is tested.
//  3. Option names are case-sensitive and a misspelling is silently ignored —
//     `wikilinks` does nothing, `wikiLinks` works. So the flags below are
//     covered by a test that would fail if a rename ever made them do nothing.
//
// Footnotes are the one thing to know about: bun does not support them and
// silently renders `text[^1]` as a bogus link. No stone in the castle uses one
// today (checked: zero matches), and `lantern check` would not catch it, so if
// footnotes ever arrive this comment is where to start.

import { normalize } from "./read.ts";

/** Where a link should point, decided by the caller who holds the index.
 *  `target` is a castle-relative path for `path` links and a bare name for
 *  `wiki` bricks. Returning null means "nothing is there": an unlaid brick is
 *  shown as marked plain words rather than a link to nowhere. */
export type Router = (target: string, form: "wiki" | "path") => string | null;

/** The flags. Named once, used once, and checked by a test. */
const MARKDOWN = {
  noHtmlBlocks: true, // with noHtmlSpans: raw HTML becomes visible text, never live
  noHtmlSpans: true,
  wikiLinks: true, // [[brick]] → <x-wikilink data-target="brick">brick</x-wikilink>
  autolinks: true, // a url written plainly becomes a link, as the reader counts it
} as const;

// Which links may keep their door. bun emits `javascript:` and `data:`
// unfiltered, and a castle read in a browser must not be a place where prose
// can run — so this is hand-written and tested.
//
// The rule is stated the safe way round: a link with NO scheme is an ordinary
// relative path and is fine; a link WITH a scheme must name one of three.
// Writing it as a list of bad schemes would need to be right about every
// scheme that will ever exist.
const HAS_SCHEME = /^[a-z][a-z0-9+.-]*:/i;
const GOOD_SCHEME = /^(https?|mailto):/i;

/** Browsers ignore whitespace and control characters inside a url, so
 *  `java\nscript:` would run. They are stripped before the scheme is judged. */
function allowed(href: string): boolean {
  const bare = href.replace(/[\u0000-\u0020\u007f]/g, "");
  return !HAS_SCHEME.test(bare) || GOOD_SCHEME.test(bare);
}

const esc = (s: string) => Bun.escapeHTML(s);

/** Markdown → HTML for one stone.
 *  `dir` is the folder the stone lives in, because a relative link means
 *  something different depending on who wrote it. */
export function toHtml(markdown: string, dir: string, route: Router): string {
  const html = Bun.markdown.html(markdown, MARKDOWN);

  return new HTMLRewriter()
    // A brick. `replace()` would drop the label and never close the anchor, so
    // the tag is rewritten around its contents instead: open before, close
    // after, and let the words through.
    .on("x-wikilink", {
      element(el) {
        const target = (el.getAttribute("data-target") ?? "").trim();
        const href = target ? route(target, "wiki") : null;
        if (href) {
          el.before(`<a class="brick" href="${esc(href)}">`, { html: true });
          el.onEndTag((end) => end.after("</a>", { html: true }));
        } else {
          el.before(
            `<span class="unlaid" title="named, but this word is not written yet">`,
            { html: true },
          );
          el.onEndTag((end) => end.after("</span>", { html: true }));
        }
        el.removeAndKeepContent();
      },
    })
    // Every link: check the scheme, then send links between stones to the
    // right page.
    .on("a[href]", {
      element(el) {
        const href = (el.getAttribute("href") ?? "").trim();

        if (!allowed(href)) {
          el.removeAttribute("href");
          el.setAttribute("class", "blocked");
          el.setAttribute("title", `a link the lantern will not follow: ${href.slice(0, 60)}`);
          return;
        }
        if (/^(https?:|mailto:)/i.test(href)) {
          el.setAttribute("class", "away");
          el.setAttribute("rel", "noreferrer noopener");
          return;
        }
        if (href.startsWith("#")) return; // a jump inside this page

        const to = route(normalize(dir, href.split("#")[0]), "path");
        if (to) el.setAttribute("href", to);
        else {
          el.removeAttribute("href");
          el.setAttribute("class", "blocked");
          el.setAttribute("title", `this link points at nothing: ${href}`);
        }
      },
    })
    // bun tags a fenced block `class="language-json"`. Nothing here highlights
    // syntax, but naming the language costs nothing — and CSS cannot strip the
    // prefix, so the clean name is put where a stylesheet can reach it.
    .on("pre code[class]", {
      element(el) {
        const lang = /language-([a-z0-9+#-]+)/i.exec(el.getAttribute("class") ?? "")?.[1];
        if (lang) el.setAttribute("data-lang", lang);
      },
    })
    .on("img[src]", {
      element(el) {
        const src = (el.getAttribute("src") ?? "").trim();
        if (!allowed(src)) el.replace(`<span class="blocked">[an image the lantern will not load]</span>`, { html: true });
      },
    })
    .transform(html);
}
