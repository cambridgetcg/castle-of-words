# jsx-transform

A JSX transform is the step that turns React's HTML-like syntax (`<div>Hello</div>`) into plain JavaScript function calls (`React.createElement('div', null, 'Hello')`) before the browser can run it.

Different tools do this transform differently: Babel has one implementation, SWC (used by Turbopack) has another, TypeScript has its own. Most of the time they agree. When they don't, the difference is invisible to every tool that checks the source code — it only shows up in what the browser actually renders.

Links: [[html-entity]] [[the-space-eater]]
