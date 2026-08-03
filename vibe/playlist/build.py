import json, html, re, pathlib

d = json.load(open("final.json"))
T, MV, TOTAL = d["tracks"], d["movements"], d["total_seconds"]

WING = {
    "good-trip": "旅 Good Trip", "garden": "The Garden", "rest": "The Book of Rest",
    "castle": "The Castle", "flow": "流流 Flow", "gospel": "喜喜 Gospel",
    "mirrors": "Hall of Mirrors", "citizens": "The Citizens",
    "cantonese": "廣東話", "kosmische": "The Long Voyage", "dawn": "The Return",
}

def e(s):
    return html.escape(html.unescape(str(s)), quote=False)

def hm(s):
    h, m = s // 3600, (s % 3600) // 60
    return (f"{h}h {m}m" if h else f"{m}m")

# --- editorial fixes on top of the curators' copy ---
for t in T:
    # "rec. 1950s" must not display as 1950
    m = re.search(r"(1[89]\d\d|20\d\d)s", t["year_full"])
    if m:
        t["year"] = m.group(1) + "s"
    # keep album labels to their first clause; the long provenance lives in the notes
    t["album"] = re.split(r";\s*also\b|;\s*", html.unescape(t["album"]))[0].strip()
    if t["title"].startswith("Water Copy"):
        t["why"] = ("Soft keyboard phrases that fall and soak in the way water finds "
                    "its level in fresh-laid soil — he offered this one to a museum "
                    "with a courtyard garden.")

# ---------------------------------------------------------------- markdown
md = ["# The Kingdom Playlist",
      "",
      "*for those that wanna listen*",
      "",
      f"{len(T)} tracks · {hm(TOTAL)} · {len(MV)} movements. Made 3 August 2026, "
      "asked for by yu. Every track was fact-checked against the record before it "
      "was allowed in — see the note at the foot.",
      ""]
n = 0
for mv in MV:
    dur = sum(T[i]["secs"] for i in mv["indices"])
    md += [f"## {mv['name']}", "", f"*{mv['feels']}*", "",
           f"`{len(mv['indices'])} tracks · {hm(dur)}`", ""]
    for i in mv["indices"]:
        n += 1
        t = T[i]
        md.append(f"{n}. **{html.unescape(t['artist'])} — {t['title']}** · "
                  f"{t['year']} · *{html.unescape(t['album'])}* · {t['len']} · "
                  f"[{WING[t['wing']]}]  ")
        md.append(f"   {html.unescape(t['why'])}")
    md.append("")
md += ["---", "",
       "## How this was made, and what is not certain", "",
       "Eleven curators, one per wing of the kingdom, each proposed eight tracks. "
       "Every one of the 88 was then handed to a separate fact-checker told to "
       "**refute it by default**: does this exact recording by this exact artist "
       "exist, and are the album, year and length right?", "",
       "- **None were rejected as invented.** All 88 turned out to be real recordings.",
       "- **Corrections were the real yield.** 張國榮's 共同渡過 was claimed for *Virgin Snow* "
       "and is actually on *Summer Romance '87*; a dozen run times were wrong "
       "(王菲's 夢中人 is 4:21, not 3:00; 追 is 5:24, not 4:15). Those are fixed here.",
       "- **14 tracks were proposed by two wings at once** and are listed once.",
       "- **One duplicate slipped through the machine and was caught by hand:** Aretha "
       "Franklin's *Amazing Grace* came in under both Gospel and Citizens with slightly "
       "different titles. Dropped to one.",
       "- **Thin wings, honestly:** The Long Voyage ended up with 4 tracks, and half of "
       "those are Indian and Chinese classical rather than kosmische — the wing is "
       "really *long-form patience* borrowing from wherever it is practised. The Return "
       "and Flow are light at 5.", "",
       "Run times are from the record where a checker could find one; a `~` means the "
       "source gave a rounded figure. Years are first release unless the track is a "
       "later reissue of an older recording, in which case the recording date is what "
       "matters and is noted in the full entry.", ""]
pathlib.Path("playlist.md").write_text("\n".join(md))

# -------------------------------------------------------------------- html
rows = []
n = 0
for mi, mv in enumerate(MV):
    dur = sum(T[i]["secs"] for i in mv["indices"])
    share = dur / TOTAL * 100
    num, name = mv["name"].split(". ", 1)
    rows.append(f'''
    <section class="movement" aria-labelledby="mv{mi}">
      <header class="mv-head">
        <div class="mv-num" aria-hidden="true">{e(num)}</div>
        <div class="mv-title">
          <h2 id="mv{mi}">{e(name)}</h2>
          <p class="epigraph">{e(mv["feels"])}</p>
          <p class="mv-meta"><span>{len(mv["indices"])} tracks</span><span class="dot">·</span><span class="tnum">{hm(dur)}</span></p>
          <div class="share" role="img" aria-label="{share:.0f} percent of the whole playlist">
            <span style="width:{share:.2f}%"></span>
          </div>
        </div>
      </header>
      <ol class="tracks">''')
    for i in mv["indices"]:
        n += 1
        t = T[i]
        rows.append(f'''
        <li class="track">
          <span class="idx tnum">{n}</span>
          <div class="body">
            <p class="name"><span class="artist">{e(t["artist"])}</span><span class="sep"> — </span><span class="title">{e(t["title"])}</span></p>
            <p class="why">{e(t["why"])}</p>
            <p class="meta"><span class="wing">{e(WING[t["wing"]])}</span><span class="dot">·</span>{e(t["year"])}<span class="dot">·</span><span class="album">{e(t["album"])}</span></p>
          </div>
          <span class="len tnum">{e(t["len"])}</span>
        </li>''')
    rows.append("      </ol>\n    </section>")

CSS = """
:root{
  --parchment:#f5efe2; --card:#f9f4e8; --edge:#e0d4b8; --deep:#ece3cf;
  --ink:#1a1612; --ink-soft:#3d352b; --ink-faint:#6e6354;
  --foil:#b8902e; --foil-light:#e3c45e;
  --thread:#e0d4b8; --shadow:rgba(26,22,18,.07);
}
@media (prefers-color-scheme:dark){
  :root{
    --parchment:#12100d; --card:#1c1814; --edge:#2d2820; --deep:#221d16;
    --ink:#d8cfc0; --ink-soft:#b6ab99; --ink-faint:#968874;
    --foil:#f5d742; --foil-light:#b8860b;
    --thread:#2d2820; --shadow:rgba(0,0,0,.5);
  }
}
:root[data-theme="dark"]{
  --parchment:#12100d; --card:#1c1814; --edge:#2d2820; --deep:#221d16;
  --ink:#d8cfc0; --ink-soft:#b6ab99; --ink-faint:#968874;
  --foil:#f5d742; --foil-light:#b8860b;
  --thread:#2d2820; --shadow:rgba(0,0,0,.5);
}
:root[data-theme="light"]{
  --parchment:#f5efe2; --card:#f9f4e8; --edge:#e0d4b8; --deep:#ece3cf;
  --ink:#1a1612; --ink-soft:#3d352b; --ink-faint:#6e6354;
  --foil:#b8902e; --foil-light:#e3c45e;
  --thread:#e0d4b8; --shadow:rgba(26,22,18,.07);
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--parchment); color:var(--ink);
  font-family:"Seravek","Avenir Next","Segoe UI",system-ui,sans-serif;
  font-size:17px; line-height:1.6;
  -webkit-font-smoothing:antialiased;
}
.tnum{font-variant-numeric:tabular-nums}
.wrap{max-width:52rem;margin:0 auto;padding:clamp(1.5rem,5vw,4.5rem) clamp(1.1rem,4vw,2rem) 5rem}

/* ---- head ---- */
.mast{border-bottom:1px solid var(--edge);padding-bottom:2.2rem;margin-bottom:3rem}
h1{
  font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  font-weight:400; font-size:clamp(2.4rem,7vw,4rem); line-height:1.06;
  margin:0 0 .5rem; letter-spacing:-.015em; text-wrap:balance;
}
h1 .thread{color:var(--foil);font-style:italic}
.sub{
  font-family:"Iowan Old Style",Palatino,Georgia,serif; font-style:italic;
  color:var(--ink-soft); font-size:1.2rem; margin:0 0 1.6rem;
}
.stats{display:flex;flex-wrap:wrap;gap:.55rem 1.4rem;margin:0 0 1.4rem;padding:0;list-style:none;
  font-size:.82rem;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-faint)}
.stats b{color:var(--foil);font-weight:400}
.intro{color:var(--ink-soft);max-width:36rem;margin:0}
.intro a{color:var(--foil)}

/* ---- movements ---- */
.movement{margin:0 0 3.4rem}
.mv-head{display:flex;gap:clamp(.8rem,3vw,1.6rem);align-items:flex-start;margin-bottom:1.4rem}
.mv-num{
  font-family:"Iowan Old Style",Palatino,Georgia,serif;
  font-size:clamp(1.5rem,4vw,2.1rem); color:var(--foil); line-height:1;
  padding-top:.15rem; min-width:2.4rem; text-align:right; flex:none;
}
.mv-title{flex:1;min-width:0}
h2{
  font-family:"Iowan Old Style",Palatino,Georgia,serif; font-weight:400;
  font-size:clamp(1.5rem,4vw,2.1rem); margin:0 0 .35rem; line-height:1.15; text-wrap:balance;
}
.epigraph{
  font-family:"Iowan Old Style",Palatino,Georgia,serif; font-style:italic;
  color:var(--ink-soft); margin:0 0 .6rem; font-size:1.02rem;
}
.mv-meta{margin:0 0 .55rem;font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-faint)}
.share{height:2px;background:var(--thread);border-radius:2px;overflow:hidden}
.share span{display:block;height:100%;background:var(--foil);opacity:.75}

/* ---- the one gold thread ---- */
.tracks{
  --rail:clamp(1.9rem,5.4vw,3.2rem);
  list-style:none;margin:0;padding:0 0 0 var(--rail);
  border-left:1px solid var(--thread);
}
.track{
  position:relative;display:flex;gap:1rem;align-items:baseline;
  padding:.95rem 0; border-bottom:1px solid var(--edge);
}
.track:last-child{border-bottom:0}
.idx{
  position:absolute; left:calc(-1 * var(--rail)); width:var(--rail);
  text-align:center; font-size:.78rem; color:var(--ink-faint);
  background:var(--parchment); padding:.1rem 0; top:1rem; line-height:1.2;
}
.body{flex:1;min-width:0}
.name{margin:0 0 .18rem;font-size:1.06rem;line-height:1.35;text-wrap:pretty}
.artist{color:var(--ink)}
.sep{color:var(--ink-faint)}
.title{
  font-family:"Iowan Old Style",Palatino,Georgia,serif;
  font-style:italic; color:var(--foil); font-size:1.1em;
}
.why{margin:.1rem 0 .3rem;color:var(--ink-soft);font-size:.95rem;line-height:1.5;max-width:42rem}
.meta{margin:0;font-size:.76rem;letter-spacing:.055em;color:var(--ink-faint);text-transform:uppercase}
.wing{color:var(--foil);opacity:.85}
.dot{margin:0 .5rem;opacity:.5}
.len{color:var(--ink-faint);font-size:.82rem;flex:none;padding-top:.15rem}

/* ---- foot ---- */
.foot{margin-top:4rem;border-top:1px solid var(--edge);padding-top:2rem;
  color:var(--ink-soft);font-size:.94rem}
.foot h3{
  font-family:"Iowan Old Style",Palatino,Georgia,serif;font-weight:400;
  font-size:1.35rem;color:var(--ink);margin:0 0 .9rem}
.foot ul{padding-left:1.1rem;margin:.9rem 0}
.foot li{margin:.45rem 0}
.foot b{color:var(--ink);font-weight:600}
.fleuron{text-align:center;color:var(--foil);margin:2.6rem 0 0;font-size:1.1rem;letter-spacing:.5em}

a:focus-visible,li:focus-visible{outline:2px solid var(--foil);outline-offset:3px;border-radius:2px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
@media (max-width:34rem){
  .track{flex-wrap:wrap}
  .len{order:3;padding-top:0}
  .mv-num{min-width:1.7rem}
}
"""

HTML = f"""<meta charset="utf-8">
<title>The Kingdom Playlist</title>
<style>{CSS}</style>
<div class="wrap">
  <header class="mast">
    <h1>The Kingdom<br><span class="thread">Playlist</span></h1>
    <p class="sub">for those that wanna listen</p>
    <ul class="stats">
      <li><b>{len(T)}</b> tracks</li>
      <li><b>{hm(TOTAL)}</b> end to end</li>
      <li><b>{len(MV)}</b> movements</li>
      <li><b>11</b> wings of the kingdom</li>
    </ul>
    <p class="intro">One curator per wing of the house — the garden, the castle,
    the Book of Rest, the hall of mirrors, 廣東話, 旅 Good Trip — then every single
    track handed to a fact-checker told to disprove it. Ordered for the whole
    night: opens quiet, dissolves in the middle, and lands somewhere kind.</p>
  </header>
{''.join(rows)}
  <footer class="foot">
    <h3>How this was made, and what is not certain</h3>
    <p>Eleven curators, one per wing, proposed eight tracks each. All 88 were then
    handed to separate fact-checkers instructed to <b>refute by default</b> — does
    this exact recording by this exact artist exist, and are the album, year and
    length right?</p>
    <ul>
      <li><b>None were invented.</b> All 88 turned out to be real recordings, which
      is the answer you want but not the one you can assume.</li>
      <li><b>The corrections were the yield.</b> 張國榮's 共同渡過 was claimed for
      <i>Virgin Snow</i> and is really on <i>Summer Romance '87</i>. A dozen run times
      were wrong — 王菲's 夢中人 is 4:21, not 3:00; 追 is 5:24, not 4:15. Fixed here.</li>
      <li><b>14 tracks were chosen by two wings at once</b> and appear once.</li>
      <li><b>One duplicate beat the machine and was caught by hand:</b> Aretha
      Franklin's <i>Amazing Grace</i> arrived under both Gospel and Citizens with
      slightly different titles. Now listed once.</li>
      <li><b>Thin wings, said plainly.</b> The Long Voyage came out with only four
      tracks, and half of those are Indian and Chinese classical rather than
      kosmische — that wing is really <i>long-form patience</i>, borrowed from
      wherever it is practised. The Return and Flow are light at five.</li>
    </ul>
    <p>Run times come from the record where a checker could find one; <span class="tnum">~</span>
    means the source gave a rounded figure. Years are first release, except where a
    track is a later issue of an older recording — 廣陵散 was played in 1957 and
    reissued in 1995, and the 1957 is the part that matters.</p>
    <p class="fleuron">❧</p>
  </footer>
</div>
"""
pathlib.Path("playlist.html").write_text(HTML)
print("wrote playlist.md and playlist.html")
print("tracks", len(T), "total", hm(TOTAL))
