# The instruments

*Tools that measure their own honesty — a forecaster, an immune system, a trader.*

What gathers here: the estate's research-and-calibration tools — three
projects that share one principle: a claim is worth nothing unless it is
scored against what actually happened.

The forecaster: oracle — an AI-driven market forecasting system (Python, cron
jobs) that collects economic data (stocks, bonds, gold, oil, bitcoin), issues
weekly predictions with stated confidence, scores them against reality, and
writes the lessons back into its own methodology. The point is
[[calibration]] — learning whether its 80%-confidence calls really hit 80% of
the time. The framework and 55 research write-ups across 14 domains were built
in a two-day burst (Feb 24-25, 2026); the predictions folder the README
promises is not in the clone, so the machine is built but its track record
hasn't started.

The immune system: whitehack — an internal security-review system (104
commits) that adversarially reviews the estate's own projects (zerone,
agenttool, Cambridge-TCG) before code ships and hunts bugs after. Mostly
markdown: methodology guides, threat checklists, per-asset profiles, and case
studies of 103 real-world exploit events across five categories (blockchain,
enterprise breach, extortion, social media, retail POS). Small Python tools
turn closed findings back into checklist items — a self-improving review loop
where every finding hardens the next review.

The trader: prediction-markets — a prediction-markets trading and calibration
system (235 markdown research notes, ~70 Python files for bankroll, pipeline,
oracle cron, strategies, trade logs). The same calibration principle as oracle,
aimed at markets that answer back with real money.

The sibling: the AxiePro analytics platform (44 MB, ~400 files — Python
FastAPI backend, Next.js frontend, Postgres/TimescaleDB) is a real blockchain
analytics tool for Axie Infinity / Ronin, with sales-data fetch scripts and
Lambda and EC2 infra. It shares the instruments' shape — a tool that measures
a market — but not the calibration ethic: it shows data, not scored
predictions.

What the words mean here, plainly. An "instrument" is a tool that measures
itself — oracle scores its own forecasts, whitehack turns its own findings
into rules, prediction-markets let the market score the trader. The
[[calibration]] brick already lives in the castle (relative ordering vs
absolute level, held once); these tools are the estate's way of holding the
same discipline in code. The [chronicle](../chronicle.md) records oracle's
EXISTENCE.md linking it to Cambridge-TCG as "calibrated uncertainty for
pricing, demand, inventory" — the instruments serve the
[commerce-kingdom](commerce-kingdom.md) as its eyes.

Related: [[calibration]] · [[standard]] · [commerce-kingdom](commerce-kingdom.md) · [the-truth-chain](the-truth-chain.md) · [money-is-not](money-is-not.md) (the decree that understanding is the real currency — the instruments are that currency made operational: they score claims against what actually happened, never against what was paid) · [agenttool](agenttool.md) (whitehack reviews agenttool before code ships — the instruments' self-measuring principle extends to the inn the estate's agents travel through, one instrument guarding the inn's gates) · [the-sovereign-fleet](the-sovereign-fleet.md) (the fleet's nerve system stamps a freshness timestamp every seven minutes — a dead loop cannot move it, the same self-verification principle the instruments hold: a claim worth nothing unless scored against what happened) · [the-arena](the-arena.md) (the arena's trust ratings are evidence-backed — the same self-measuring principle the instruments hold: a verdict that carries its reasons, scored against what happened rather than voted on what was felt) · [the-catalogue](the-catalogue.md) (the catalogue verifies where each masterpiece physically hangs — every fact web-checked twice, the same score-against-reality discipline the instruments hold, one for art and one for predictions) · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern — publication, licence, privacy as separate boundaries — is the same law the instruments hold for calibration: a claim scored against what happened must keep its source, its method, and its verdict as separate facts, never fused into a single score) · [honest-endpoints](honest-endpoints.md) (the endpoint that exposes its ETag and allows conditional GETs is the web's face of the same self-measuring principle — an instrument that scores itself and an API that lets the client verify its copy are the same honesty at two altitudes) · [the-true-measure-of-growth](the-true-measure-of-growth.md) (the room that says growth is measured against unchanging standards, not shifting selves — the instruments are that standard made operational: a forecaster scored against what happened, not what was predicted, the same external benchmark that trues the level) · [the-price-of-clarity](the-price-of-clarity.md) (the room that names the cost of making a score clear — the instruments' calibration is the same tension: a clear score that may leave nuance behind, the same price of clarity paid in a different coin)