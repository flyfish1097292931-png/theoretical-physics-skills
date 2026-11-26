"""Exact-arithmetic checks for the unit harmonic oscillator under velocity Verlet."""
import json
from fractions import Fraction as F

STEPS = 12
GRID = tuple((h, n) for h in (F(1, 2), F(1, 4), F(1, 8)) for n in range(STEPS + 1))
SPEC = {"model": "q''=-q", "initial": "q=1,p=0", "method": "velocity-verlet",
        "observable": "(p^2+(1-h^2/4)*q^2)/2", "arithmetic": "exact"}


def verlet(q, p, h):
    p_half = p - h * q / 2
    q_new = q + h * p_half
    return q_new, p_half - h * q_new / 2


def trajectory(h):
    q, p = F(1), F(0)
    for n in range(STEPS + 1):
        yield n, q, p
        q, p = verlet(q, p, h)


def invariant(q, p, h):
    return (p * p + (1 - h * h / 4) * q * q) / 2


def make_rows():
    return [(h, n, invariant(q, p, h))
            for h in (F(1, 2), F(1, 4), F(1, 8)) for n, q, p in trajectory(h)]


def audit(protocol, rows):
    if protocol != SPEC:
        return "observable_or_protocol_mismatch"
    keys = [(h, n) for h, n, _ in rows]
    if len(keys) != len(set(keys)) or set(keys) != set(GRID):
        return "grid_mismatch"
    # Analytic value from the matrix-invariance identity and initial conditions.
    if any(value != F(1, 2) - h * h / 8 for h, _, value in rows):
        return "value_mismatch"
    return "criteria_met"


def first_step_energy(h):
    q, p = verlet(F(1), F(0), h)
    return (q * q + p * p) / 2


def summary():
    rows = make_rows()
    wrong = dict(SPEC, observable="(p^2+q^2)/2")
    e1 = first_step_energy(F(1, 2))
    return {"rows": len(rows), "registered_invariant": audit(SPEC, rows),
            "wrong_observable_with_matching_values": audit(wrong, rows),
            "physical_energy_change_after_one_step_at_h_half": str(e1 - F(1, 2)),
            "scope": "declared unit oscillator; fixed-step velocity Verlet"}


if __name__ == "__main__":
    result = summary()
    print(json.dumps(result, indent=2, sort_keys=True))
    ok = (result["rows"] == 39 and result["registered_invariant"] == "criteria_met"
          and result["wrong_observable_with_matching_values"] == "observable_or_protocol_mismatch"
          and result["physical_energy_change_after_one_step_at_h_half"] == "-15/2048")
    raise SystemExit(0 if ok else 1)
