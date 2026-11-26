---
name: physics-anomaly-investigation
description: Trace disagreements between physics diagnostics.
version: 0.1.0
author: Feiyu Deng, with Hermes Agent assistance
license: MIT
---

# Physics anomaly investigation

## When to use

Use when analytic and numerical routes disagree, agree suspiciously well, or change under a regulator path. For a routine coding fault with a known single definition, use ordinary debugging instead.

## Procedure

1. **Preserve the discrepancy.** Record the two signed values, units, sizes and regime, the expected relation, and the smallest input that reproduces the discrepancy. Preserve the original output before an attempted repair.
2. **Compare definitions before outputs.** For each route write the action or Hamiltonian, operator or algebra, domain and boundary conditions, state, normalization/reference, and ordered limits. Mark each field `same`, `mapped`, `different`, or `not checked`. An explicit map is necessary for `mapped`; a similar formula is insufficient.
3. **Find the first divergent layer.** Compare finite-input operators, then spectra/constraints and special sectors, then raw observables, then subtracted or fitted values and limit extrapolation. Check zero modes, endpoint ownership, mode counting, quadrature near singular endpoints, and conditioning where relevant. Stop at the first mismatch that can explain the observed scale.
4. **Change one cause at a time.** Prestate the direction or invariant signature expected from each hypothesis. Use a known limit or a small independent computation. A deliberately misnormalized control should fail the relevant check; choose a nonzero coupling or nontrivial state so the mistake cannot cancel vacuously.
5. **Separate diagnosis from repair.** If the observable or protocol changed, register a new comparison and keep the old result. If only the implementation changed, rerun the original inputs and show that positive and negative controls separate.

## Pitfalls

- Do not tune fitting windows, cutoff paths, normalization, or subtraction references after seeing the target and then count the result as independent confirmation.
- A symbolic identity does not prove its numerical implementation. A small number near zero does not prove a symmetry-enforced zero. Report precision, conditioning and an independent identity or bound if the distinction matters.
- Keep viable alternatives open when the data cannot distinguish them; list the test that would distinguish them.

## Verification

Return a definition comparison, earliest divergence, one discriminating check, and one disposition: `explained within scope`, `partially localized`, `different observables`, or `unresolved`. State the effect on the original claim. The [oscillator lesson](../../examples/oscillator/README.md) distinguishes two conserved-quantity claims for the same integrator.
