---
name: physics-paper-integrity-gate
description: Audit what a physics manuscript can actually claim.
version: 0.1.0
license: MIT
---

# Physics paper integrity gate

Use on a specified manuscript revision before circulation or submission. This audit checks traceability and scope across the draft; it cannot replace a physicist's review or authorize submission.

1. **Start from the public-facing claims.** Copy the load-bearing sentences from the abstract, introduction, results, captions, and conclusion. Trace each to a derivation step, an exact numerical artifact, or a primary citation. Record revision and locations so the check can be repeated after edits.
2. **Check the physics and the handoffs.** Confirm definitions, dimensions, sign conventions, domains, special sectors, and order of limits in the chain that supports the main result. Check whether the proof assumes a condition that vanished from the abstract, or a figure uses a reference different from the formula in the text.
3. **Separate support types.** A finite scan supports a finite-grid observation; a proof needs its hypotheses; a citation must establish the actual sentence. Use [claim scope closure](../physics-claim-scope-closure/SKILL.md) for a proposed extension and [literature calibration](../hep-th-literature-workflow/SKILL.md) for a novelty claim. If evidence is missing, flag it as not assessed and state what would resolve it.
4. **Read the rendered draft.** Spot-check that equation and figure references point to the right objects, notation renders without semantic changes, and captions still match the plotted quantities. Do not substitute build success for content verification.
5. **Repair the weakest link first.** Request a calculation where the central result depends on it; otherwise narrow or remove the unsupported sentence wherever it is repeated. Recheck the edited revision and keep unaffected results intact.

Return a short ledger with `claim | exact support | scope | verdict | required change`. Distinguish release blockers, limitations and optional edits. The [worked review](../../examples/oscillator/research-review.md) shows how a single overclaim is narrowed without deleting the valid result.
