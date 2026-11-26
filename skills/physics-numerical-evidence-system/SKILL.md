---
name: physics-numerical-evidence-system
description: Build reproducible numerical evidence in physics.
version: 0.1.0
author: Feiyu Deng, with Hermes Agent assistance
license: MIT
---

# Physics numerical evidence system

## When to use

Use when a numerical result will support a consequential theoretical claim or must be reproducible by a collaborator. Scale the evidence packet to the decision. An exploratory calculation only needs an honest label and adequate local checks.

## Procedure

1. **Freeze the target.** Use a [pre-claim spec](../physics-preclaim-registration/SKILL.md). Keep raw inputs separate from scripts, outputs and report. List the formula-to-code mapping for every load-bearing quantity, including finite-size terms and units.
2. **Build two routes when warranted.** Compare a production method against an analytic special case or a separately implemented calculation. Ensure they do not silently share the same disputed formula or reduction. Check exact limits, sum rules or symmetry separately from floating-point comparisons.
3. **Expose numerical weaknesses.** Separate discretization, truncation, conditioning, sampling and regression error. Record how varying precision, grid and fit windows changes the result. If the claimed effect is of the order of the error budget, report it as unresolved. Do not stabilize the answer by changing the physical observable.
4. **Preserve the execution record.** Save command, source version, frozen input, runtime, exit status, and actual machine-readable output. Bind outputs and exact inputs if others will rely on them. Preserve negative and incomplete attempts. A timed-out run is not a counterexample; an old run at a different source version is not fresh evidence.
5. **Check detached reproducibility.** In a fresh directory, run the documented command on the deliverable and compare the full fixed input-key set and declared residuals. Include a negative control that fails for the intended reason rather than merely returning nonzero.

## Smallest useful packet

- A frozen spec with decision thresholds and forbidden extensions.
- A code/derivation map and portable commands.
- Raw values and diagnostics at each registered input, with a run record.
- A concise write-up separating software checks, numerical status and the inference the physics actually warrants.

## Pitfalls

Matching only the last row can hide a disagreement at intermediate scales. A hash binds bytes; it does not prove independence, valid scope, or correctness. A complete output directory is not proof that a run reached its registered endpoint.

## Verification

Replay the [oscillator lesson](../../examples/oscillator/README.md): `python3 examples/oscillator/check.py` from the repository root. Require exact coverage, the independently derived invariant check, and rejection of a mislabeled conserved quantity even when the supplied numbers are correct for the registered observable.
