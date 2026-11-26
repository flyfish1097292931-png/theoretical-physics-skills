---
name: physics-claim-scope-closure
description: Match physics claim scope to the evidence.
version: 0.1.0
author: Feiyu Deng, with Hermes Agent assistance
license: MIT
---

# Physics claim scope closure

## When to use

Use when a result in a special solution, sector, finite scan, or particular regulator is being turned into a general statement in a report or paper. Do not add a review layer for claims whose scope is already exactly the demonstrated result.

## Procedure

1. **Copy the target sentence verbatim.** Extract its quantifiers, observable, model family, sectors, fixed parameters, and regulator or limit statement.
2. **Map evidence to the target.** For each calculation state the representative, branch, observable and what it excludes. If symmetry is invoked, prove that the transformation preserves the operator domain, boundary conditions, constraints, and observable. Classify orbits or restrict the sentence; one solvable point is not an orbit classification.
3. **Keep branch evidence paired.** A maximum or bound in one branch does not combine with an extremum or existence claim from another unless the choices can be realized by the same admissible object. Distinguish a projected invariant-sector result from a full-operator result; an overlap test is needed before a field mode predicts a measured signal.
4. **Freeze the convergence domain.** Require fixed physical intervals or an explicitly specified regulator path. Pointwise convergence away from a moving boundary need not be uniform, and it need not justify integration, differentiation, or extrapolation across that boundary. Supply an appropriate bound or qualify the sentence.
5. **Try one decisive counterexample.** Probe the omitted sector, degenerate or singular endpoint, alternative branch, or regulator ordering most likely to break the extension. Keep unaffected results rather than throwing out the whole calculation.

## Pitfalls

- Agreement of moments with a reference is not a state-identity proof without the relevant reconstruction hypotheses.
- `Proved`, `numerical evidence`, `conditional`, `limitation`, `contradicted`, and `not assessed` are not interchangeable. A new premise belongs in the claim, not only in a footnote or a review log.

## Verification

Return the strongest supported sentence, its exact scope, the evidence for any extension, and one explicit forbidden inference. In the [oscillator lesson](../../examples/oscillator/README.md), exact conservation of a step-dependent invariant does not imply exact conservation of physical energy.
