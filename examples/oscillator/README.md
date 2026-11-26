# Worked example: which energy is conserved?

For the unit classical oscillator, `q' = p`, `p' = -q`, the exact flow conserves the physical energy $H=(p^2+q^2)/2$. Does the fixed-step velocity Verlet map conserve that same quantity exactly?

## Freeze the test

- Initial data: $q=1,p=0$; fixed steps $h\in\{1/2,1/4,1/8\}$; sample step indices 0 through 12 inclusive for each $h$.
- Integration route: kick–drift–kick; all values are exact rationals. Two quantities must not be conflated: $H$ and $H_h=(p^2+(1-h^2/4)q^2)/2$.
- Require exact grid coverage and equality for the registered invariant $H_h$. A mismatched observable label fails before numerical comparison. A single nonzero exact change disproves exact conservation of $H$ for the stated input.

## Analytic check, separate from the trajectory loop

Write $A=1-h^2/2$ and $B=1-h^2/4$. Composing the kicks and drift yields the linear map $(q,p)\mapsto(Aq+hp,\,-hBq+Ap)$. In the quadratic form $Bq^2+p^2$, the cross terms cancel and the remaining terms multiply by $A^2+h^2B=1$. Thus $H_h$ is conserved for this fixed-step linear map and equals $1/2-h^2/8$ for the stated initial data. For $0<h<2$ it is positive definite.

But at $h=1/2$, the first step gives $q=7/8$, $p=-15/32$, so the true physical energy changes by $-15/2048$. No floating-point tolerance is involved. This does not rule out bounded energy error, approximate conservation, or convergence as the step goes to zero. It also does not establish an exactly conserved quadratic form for nonlinear or variable-step integrators.

```sh
python3 examples/oscillator/check.py
```

The command checks every registered row, evaluates the physical-energy counterexample, and rejects a synthetic packet that reuses correct $H_h$ values while labeling them as $H$. This last check validates a declared protocol, not the honesty of an external producer. See [the four workflows](../../README.md) for the general procedure.
