"""Regression checks for the teaching fixture; no external dependencies."""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest

source = Path(__file__).resolve().parents[1] / "examples" / "oscillator" / "check.py"
spec = spec_from_file_location("oscillator_check", source)
model = module_from_spec(spec)
spec.loader.exec_module(model)


class OscillatorAudit(unittest.TestCase):
    def setUp(self):
        self.rows = model.make_rows()

    def test_exact_grid_and_analytic_comparator(self):
        self.assertEqual(len(self.rows), 39)
        self.assertEqual(model.audit(model.SPEC, self.rows), "criteria_met")

    def test_mislabeled_object_rejected_despite_exact_values(self):
        wrong = dict(model.SPEC, observable="(p^2+q^2)/2")
        self.assertEqual(model.audit(wrong, self.rows), "observable_or_protocol_mismatch")

    def test_missing_and_duplicate_rows(self):
        self.assertEqual(model.audit(model.SPEC, self.rows[:-1]), "grid_mismatch")
        self.assertEqual(model.audit(model.SPEC, self.rows + self.rows[:1]), "grid_mismatch")

    def test_wrong_value_with_right_protocol(self):
        h, n, value = self.rows[-1]
        bad = self.rows[:-1] + [(h, n, value + F(1, 1000))]
        self.assertEqual(model.audit(model.SPEC, bad), "value_mismatch")

    def test_physical_energy_counterexample(self):
        self.assertEqual(model.verlet(F(1), F(0), F(1, 2)), (F(7, 8), -F(15, 32)))
        self.assertEqual(model.first_step_energy(F(1, 2)) - F(1, 2), -F(15, 2048))

    def test_quadratic_invariant_for_other_initial_conditions(self):
        for h in (F(1, 2), F(1, 4), F(1, 8)):
            for q, p in ((F(2), F(3)), (F(-1, 3), F(4, 5))):
                q2, p2 = model.verlet(q, p, h)
                self.assertEqual(model.invariant(q2, p2, h), model.invariant(q, p, h))
