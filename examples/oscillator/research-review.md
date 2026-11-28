# Worked review: from a physical question to a defensible caption

This teaching walkthrough reuses the public [oscillator calculation](README.md). It is an audit example, not a novelty claim.

## Frame the question

“Does the method conserve energy?” leaves the quantity ambiguous. For the unit oscillator, ask whether fixed-step velocity Verlet exactly preserves **physical energy** $H=(p^2+q^2)/2$ or whether the exact invariant is the **step-dependent** $H_h=(p^2+(1-h^2/4)q^2)/2$. The smallest distinguishing test is one step at $h=1/2$ from $(q,p)=(1,0)$. The first quantity changes by $-15/2048$; the second stays fixed. The derivation in the [calculation notes](README.md) establishes the invariant beyond that single test for the stated linear map with constant step size.

## Calibrate the citation

[Loup Verlet, *Computer “Experiments” on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules* (1967)](https://doi.org/10.1103/PhysRev.159.98) is historical context for the integration-method family. It is not the evidence cited here for exact conservation of the oscillator's physical energy; the direct update map and counterexample settle the narrower question. This is a citation-scope check, not an exhaustive priority search.

## Specify the plot and test the caption

For a figure, put discrete step index on the horizontal axis, and plot $H_n-H_0$ and $H_{h,n}-H_{h,0}$ with distinct markers at fixed $h=1/2$. State the initial condition, the unit conventions and the exact-rational arithmetic. Keep a readable zero reference; use separate panels or a visible baseline if marks overlap. An exported figure is not included here. Before claiming a finished figure, render it and check the actual plotted source rows and labels at publication size.

| Proposed manuscript sentence | Decision | Evidence |
|---|---|---|
| “Velocity Verlet exactly conserves the oscillator's physical energy.” | Reject as written. | A nonzero first-step energy change at the stated input. |
| “For the unit linear oscillator at fixed step size, the map preserves the quadratic form $H_h$ exactly.” | Supported in this scope. | Algebraic invariance of the update matrix; finite exact-rational check as a separate cross-check. |
| “The same conservation law holds for all nonlinear oscillators and varying step sizes.” | Remove or test separately. | Neither the linear-map algebra nor the registered grid addresses that extension. |

Replay the existing fixture and tests from the repository root:

```sh
python3 examples/oscillator/check.py
python3 -B -m unittest discover -s tests -v
```
