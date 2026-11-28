---
name: physics-publication-figures
description: Make each physics figure support a stated claim.
version: 0.1.0
license: MIT
---

# Physics publication figures

Use when building or auditing a figure for a theoretical-physics paper. One figure should answer one question; each panel should supply a distinct part of the answer.

1. **Write the claim before plotting.** State what the reader should infer and the range where it holds. Name the observable, units or nondimensionalization, fixed parameters, scanned parameters, and which curves are exact, fitted, numerical, or schematic.
2. **Choose the comparison.** Overlay an independently justified baseline where it helps. If two curves nearly coincide, show a residual or give a bound; visual overlap can conceal a systematic error. Label fit ranges, excluded points, and cutoff or error conventions. Do not silently drop nonpositive values on a log axis.
3. **Audit plotted rows.** Bind panels to the inputs and generating command. From the underlying values check sign, units, numerical coverage, normalization and any claim such as “smaller at every sampled point.” One counterexample row requires a narrower claim or an explanation, not a crop that hides it.
4. **Read the export at final size.** Inspect the rendered page, not just the script. Check legends, ticks, labels, line/marker distinctions, and captions in grayscale where relevant. Keep behavioral or statistical uncertainty separate from a numerical tolerance or a residual.
5. **Write a self-contained caption.** Identify the measured quantity, baseline, methods represented, fixed conditions, and interval. Describe which conclusion the panels support. Mark extrapolation as such and avoid using a clean illustration as evidence.

Deliver the final figure, its source and data or replay recipe, and the caption. Keep the [worked review](../../examples/oscillator/research-review.md) distinction between a figure specification and an actually rendered figure.
