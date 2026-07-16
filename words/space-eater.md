# space-eater

A space-eater is a compiler or tool that silently removes a space character from text, changing meaning without leaving a trace in the source code.

The name comes from a specific bug in SWC/Turbopack's JSX transform, where a leading space before an HTML entity in a multi-line JSX text node was dropped — turning "A. The" into "A.The". The space between words is the smallest word; when a tool eats it, the meaning collapses and no lint rule catches it, because the source still looks right.

Links: [[jsx-transform]] [[html-entity]] [[the-space-eater]]
