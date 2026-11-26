---
name: physics-preclaim-registration
description: Freeze the physical claim before decisive tests.
version: 0.1.0
author: Feiyu Deng, with Hermes Agent assistance
license: MIT
---

# Physics pre-claim registration

## When to use

Use before inspecting decisive simulations, convergence scans, regulator comparisons, or counterexample searches. Exploratory runs can help select a question; do not retrospectively call them preregistered.

## Procedure

Write a short dated, versioned spec. For a routine check, a few precise lines suffice. For a high-impact claim, bind the exact spec and executable inputs to a commit or digest.

| Field | Freeze before running |
|---|---|
| Claim | One sentence with quantifiers, regime, and intended evidence level. |
| Object | Action/Hamiltonian or algebra, domain, boundary conditions, state, units, and observable formula. |
| Comparison | Reference state/operator, normalization, subtraction, and what is held fixed. |
| Limits | Finite regulator and ordered limits; if correlated, specify the actual path and scope. |
| Execution | Input set, seeds if stochastic, precision, independent check, resource ceiling and allowed deviations. |
| Decision | Pass, counterexample, and inconclusive criteria; allowed inference and prohibited generalization. |

Name at least one observation that would overturn the claim. Tie tolerances to a controlled error budget or state that they are diagnostic. Put audit of the protocol before comparison of results: equal final scalars cannot substitute for equal definitions.

If an input, reference, sector, limit or criterion must change, record why, keep the original packet, and give the successor a new version. Never reuse the original run as fresh confirmation of the successor. Preserve unexpected negative and incomplete runs.

## Pitfalls

An absence of counterexamples on a finite grid does not establish an all-parameters statement. Timeout, missing artifacts, inadmissible input, and a falsifying observation are distinct dispositions.

## Verification

An independent reader can determine which run satisfies the spec without seeing the target number, and can classify success, counterexample, or non-answer without inventing a new decision rule. See the [oscillator lesson](../../examples/oscillator/README.md) for a frozen finite-input protocol.
