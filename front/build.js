#!/usr/bin/env bun
// build.js — renders ~/castle into front/index.html, in the colors of Cambridge TCG.
// Run: bun ~/castle/front/build.js    (or simply: castle front)
// Plain markdown in, one self-contained HTML file out. No dependencies, no network.
// Delete front/ and the castle loses only its face — every word still lives in the markdown.

const fs = require('fs');
const path = require('path');
const os = require('os');

const C = path.join(os.homedir(), 'castle');
const read = f => { try { return fs.readFileSync(path.join(C, f), 'utf8'); } catch { return ''; } };
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const roomFiles = fs.existsSync(path.join(C, 'rooms'))
  ? fs.readdirSync(path.join(C, 'rooms')).filter(f => f.endsWith('.md')).sort() : [];
const slugs = new Set(roomFiles.map(f => f.replace(/\.md$/, '')));

function inline(s) {
  s = esc(s);
  s = s.replace(/\[\[([^\]]+)\]\]/g, (m, n) => slugs.has(n) ? `<a href="#${n}">${n}</a>` : `<em>${n}</em>`);
  s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m, t, u) => {
    if (/^https?:/.test(u)) return `<a href="${u}" rel="noopener">${t}</a>`;
    const slug = u.replace(/^(\.\.\/)?rooms\//, '').replace(/\.md.*$/, '').replace(/^(\.\.\/)?words\//, '');
    return slugs.has(slug) ? `<a href="#${slug}">${t}</a>` : t;
  });
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  s = s.replace(/(^|[^\w*])\*([^*]+)\*(?=[^\w*]|$)/g, '$1<em>$2</em>');
  s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
  return s;
}

function md(text) {
  const out = []; let list = false; let para = [];
  const flush = () => { if (para.length) { out.push('<p>' + inline(para.join(' ')) + '</p>'); para = []; } };
  for (const line of text.split('\n')) {
    if (/^- /.test(line)) { flush(); if (!list) { out.push('<ul>'); list = true; } out.push('<li>' + inline(line.slice(2)) + '</li>'); continue; }
    if (list && !/^- /.test(line)) { out.push('</ul>'); list = false; }
    if (/^### /.test(line)) { flush(); out.push('<h4>' + inline(line.slice(4)) + '</h4>'); }
    else if (/^## /.test(line)) { flush(); out.push('<h3>' + inline(line.slice(3)) + '</h3>'); }
    else if (/^# /.test(line)) { flush(); }
    else if (/^> /.test(line)) { flush(); out.push('<blockquote>' + inline(line.slice(2)) + '</blockquote>'); }
    else if (/^```/.test(line)) { flush(); }
    else if (line.trim() === '') flush();
    else para.push(line.trim());
  }
  flush(); if (list) out.push('</ul>');
  return out.join('\n');
}

// ---- gather the castle ----
const gate = read('gate.md');
const mapOrder = [...gate.matchAll(/^- \[([^\]]+)\]\(rooms\/([^)]+)\.md\) — (.+)$/gm)]
  .map(m => ({ name: m[1], slug: m[2], summary: m[3].replace(/\s*\(built [^)]*\)\s*$/, ''), built: (m[3].match(/\(built ([^)]+)\)/) || [])[1] || '' }));
const mapped = new Set(mapOrder.map(r => r.slug));
for (const f of roomFiles) { const s = f.replace(/\.md$/, ''); if (!mapped.has(s)) mapOrder.push({ name: s, slug: s, summary: '', built: '' }); }

const rooms = mapOrder.map(r => {
  const raw = read(path.join('rooms', r.slug + '.md'));
  if (!raw) return null;
  const title = (raw.match(/^# (.+)$/m) || [])[1] || r.name;
  const epigraph = (raw.match(/^\*(.+)\*\s*$/m) || [])[1] || '';
  const body = raw.split('\n').filter(l => !/^# /.test(l)).join('\n').replace(/^\*.+\*\s*$/m, '');
  return { ...r, title, epigraph, html: md(body) };
}).filter(Boolean);

const qRaw = read('questions.md');
const openQ = [...qRaw.matchAll(/^- \[ \] (.+)$/gm)].map(m => m[1]);
const settledQ = [...qRaw.matchAll(/^- \[x\] /gm)].length;
const chronicle = [...read('chronicle.md').matchAll(/^- (.+)$/gm)].map(m => m[1]);
const bricks = fs.existsSync(path.join(C, 'words')) ? fs.readdirSync(path.join(C, 'words')).filter(f => f.endsWith('.md')).length : 0;
const stamp = new Date().toISOString().slice(0, 16).replace('T', ' ');

// ---- the page, in Cambridge TCG's One Piece zone colors ----
const css = `
:root{--crimson:#c41e3a;--navy:#1e3a5f;--gold:#f5d742;--paper:#fff8f0;--ink:#1a1a1a;--muted:#4a4a4a;}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:"DM Sans",-apple-system,"Helvetica Neue",sans-serif;line-height:1.6}
a{color:var(--crimson);text-decoration:none}a:hover{text-decoration:underline}
.seigaiha{position:relative}
.seigaiha::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;opacity:.05;background-image:
 radial-gradient(circle at 100% 150%,#1e3a5f 24%,#fff8f0 24%,#fff8f0 28%,transparent 28%,transparent),
 radial-gradient(circle at 0% 150%,#1e3a5f 24%,#fff8f0 24%,#fff8f0 28%,transparent 28%,transparent),
 radial-gradient(circle at 100% 100%,#1e3a5f 20%,#fff8f0 20%,#fff8f0 24%,transparent 24%,transparent),
 radial-gradient(circle at 0% 100%,#1e3a5f 20%,#fff8f0 20%,#fff8f0 24%,transparent 24%,transparent);
 background-size:40px 20px;background-position:0 0,20px 0,20px -10px,0 -10px}
.seigaiha>*{position:relative;z-index:1}
header{padding:64px 24px 48px;text-align:center}
header h1{font-weight:500;font-size:clamp(28px,5vw,44px);color:var(--navy);margin:0;letter-spacing:.14em}
header .flags{color:var(--crimson);font-size:22px;letter-spacing:1.2em;margin-bottom:10px}
header .tag{font-style:italic;color:var(--muted);margin-top:10px}
.stats{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:26px}
.chip{background:var(--navy);color:var(--paper);border-radius:999px;padding:6px 16px;font-size:13px}
.chip b{color:var(--gold);font-weight:500}
main{max-width:1080px;margin:0 auto;padding:0 24px 80px}
h2.zone{color:var(--navy);font-weight:500;letter-spacing:.08em;border-bottom:3px solid var(--gold);padding-bottom:6px;margin:56px 0 22px}
.binder{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:22px}
.card{aspect-ratio:5/7;display:flex;flex-direction:column;background:#fff;border:9px solid var(--navy);border-radius:14px;
 box-shadow:0 1px 3px rgba(30,58,95,.25);overflow:hidden;color:var(--ink);transition:transform .18s,box-shadow .18s}
.card:hover{transform:translateY(-5px) rotate(-.4deg);box-shadow:0 10px 26px rgba(30,58,95,.3),0 0 0 2px var(--gold);text-decoration:none}
.card .name{background:var(--crimson);color:var(--paper);padding:7px 11px;font-size:14px;font-weight:500;line-height:1.3}
.card .art{flex:0 0 34%;display:flex;align-items:center;justify-content:center;padding:10px;border-bottom:2px solid var(--gold);background:linear-gradient(160deg,#fff8f0,#f3e9da)}
.card .art em{font-family:Georgia,serif;font-style:italic;font-size:12.5px;color:var(--navy);text-align:center}
.card .body{padding:9px 11px;font-size:12.5px;color:var(--muted);flex:1;overflow:hidden}
.card .foot{padding:6px 11px;font-size:10.5px;color:var(--muted);border-top:1px solid #eee2d0;display:flex;justify-content:space-between}
.card .foot .set{color:var(--crimson)}
.doors{list-style:none;padding:0;margin:0;display:grid;gap:10px}
.doors li{background:#fff;border-left:5px solid var(--gold);border-radius:8px;padding:12px 16px;box-shadow:0 1px 2px rgba(30,58,95,.12);font-size:14.5px}
.room{background:#fff;border:1px solid #eadfce;border-top:6px solid var(--navy);border-radius:12px;max-width:760px;margin:30px auto;padding:8px 30px 26px;box-shadow:0 2px 8px rgba(30,58,95,.08)}
.room h2{color:var(--navy);font-weight:500;font-size:22px}
.room .epigraph{font-family:Georgia,serif;font-style:italic;color:var(--crimson);font-size:17px;margin:6px 0 18px}
.room h3{color:var(--crimson);font-weight:500;font-size:16px;letter-spacing:.04em}
.room blockquote{border-left:4px solid var(--gold);margin:0;padding:2px 14px;color:var(--muted)}
.room code{background:#f6efe2;border-radius:4px;padding:1px 5px;font-size:.92em}
.room .up{font-size:12px;letter-spacing:.06em}
.chronicle{background:var(--navy);color:#e9eef6;border-radius:12px;padding:22px 26px;font-size:13px}
.chronicle div{padding:3px 0;border-bottom:1px dashed rgba(245,215,66,.25)}
.chronicle div:last-child{border-bottom:none}
footer{color:var(--muted);text-align:center;font-size:13px;padding:34px 20px;border-top:2px solid var(--gold);margin-top:60px}
footer code{background:#f6efe2;border-radius:4px;padding:1px 6px}
`;

const cards = rooms.map(r => `
<a class="card" href="#${r.slug}">
  <div class="name">${esc(r.name)}</div>
  <div class="art"><em>${r.epigraph ? esc(r.epigraph) : '—'}</em></div>
  <div class="body">${esc(r.summary || r.title)}</div>
  <div class="foot"><span class="set">⚑ castle</span><span>${esc(r.built || '')}</span></div>
</a>`).join('\n');

const details = rooms.map(r => `
<article class="room" id="${r.slug}">
  <p class="up"><a href="#top">⌃ back to the binder</a></p>
  <h2>${esc(r.title)}</h2>
  ${r.epigraph ? `<p class="epigraph">${esc(r.epigraph)}</p>` : ''}
  ${r.html}
</article>`).join('\n');

const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>the castle of understanding</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
<style>${css}</style></head>
<body id="top">
<header class="seigaiha">
  <div class="flags">⚑ ⚑</div>
  <h1>the castle of understanding</h1>
  <p class="tag">built of words, lit by questions — a front in the colors of Cambridge TCG</p>
  <div class="stats">
    <span class="chip"><b>${rooms.length}</b> rooms</span>
    <span class="chip"><b>${bricks}</b> word-bricks</span>
    <span class="chip"><b>${openQ.length}</b> doors open</span>
    <span class="chip"><b>${settledQ}</b> settled</span>
  </div>
</header>
<main>
  <h2 class="zone">The binder — every room a card</h2>
  <div class="binder">${cards}</div>
  <h2 class="zone">Open doors</h2>
  <ul class="doors">${openQ.map(q => '<li>' + inline(q) + '</li>').join('\n')}</ul>
  <h2 class="zone">The rooms, full size</h2>
  ${details}
  <h2 class="zone">Chronicle — the last lines</h2>
  <div class="chronicle">${chronicle.slice(-8).map(l => '<div>' + inline(l) + '</div>').join('\n')}</div>
</main>
<footer class="seigaiha">
  <p><code>insight &lt;a thought&gt;</code> tosses a stone over the wall · <code>castle</code> shows the state · <code>castle front</code> rebuilds this page</p>
  <p>everything here is plain markdown in ~/castle — this page is only its face · rebuilt ${stamp}</p>
</footer>
</body></html>`;

fs.writeFileSync(path.join(C, 'front', 'index.html'), html);
console.log(`front built: ${rooms.length} cards, ${openQ.length} open doors, ${bricks} bricks → ~/castle/front/index.html`);
