"""Small deterministic checks for denominator and input-integrity failures."""

import csv
import tempfile
import unittest
from pathlib import Path

from summarize_scorecard import FIELDS, read_rows, summarize


def example(**updates):
    row = {key: "0" for key in FIELDS}
    row.update(run_id="r1", task_id="t1", arm="baseline", run_status="complete",
               ground_truth_total="", ground_truth_validated="", elapsed_seconds="10")
    row.update({key: str(value) for key, value in updates.items()})
    return row


class ScorecardTests(unittest.TestCase):
    def load(self, rows):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.csv"
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            return read_rows(path)

    def test_zero_outcomes_are_undefined_with_cost_retained(self):
        data = summarize(self.load([example(run_status="failed", model_cost=7)]))["arms"]["baseline"]
        self.assertEqual(data["total_cost"], 7)
        self.assertIsNone(data["cost_per_accepted_outcome"])
        self.assertIsNone(data["useful_finding_precision"])
        self.assertEqual(data["initiated_runs"], 1)

    def test_failed_run_included_in_cost_and_success_denominator(self):
        rows = [example(accepted_outcomes=1, model_cost=3),
                example(run_id="r2", run_status="failed", rescued=1, model_cost=7,
                        human_cost=5, human_minutes=10, elapsed_seconds=30)]
        data = summarize(self.load(rows))["arms"]["baseline"]
        self.assertEqual(data["cost_per_accepted_outcome"], 15)
        self.assertEqual(data["completion_without_rescue_rate"], 0.5)
        self.assertEqual(data["rescue_rate"], 0.5)
        self.assertEqual(data["observed_run_seconds_median"], 20)
        self.assertEqual(data["observed_run_seconds_p95_nearest_rank"], 30)

    def test_precision_includes_unresolved_presented_findings(self):
        data = summarize(self.load([example(findings_presented=4, accepted_findings=1,
                                           rejected_findings=1, inconclusive_findings=2)]))["arms"]["baseline"]
        self.assertEqual(data["useful_finding_precision"], 0.25)

    def test_partial_ground_truth_does_not_become_recall(self):
        rows = [example(ground_truth_total=2, ground_truth_validated=1), example(run_id="r2")]
        data = summarize(self.load(rows))["arms"]["baseline"]
        self.assertEqual(data["ground_truth_known_runs"], 1)
        self.assertIsNone(data["ground_truth_recall"])
        self.assertIsNone(data["ground_truth_total"])

    def test_complete_ground_truth_and_fix_rate(self):
        data = summarize(self.load([example(ground_truth_total=4, ground_truth_validated=3,
                                           fixes_reviewed=2, correct_fixes=1)]))["arms"]["baseline"]
        self.assertEqual(data["ground_truth_recall"], 0.75)
        self.assertEqual(data["fix_correctness"], 0.5)

    def test_no_ground_truth_issues_is_undefined(self):
        data = summarize(self.load([example(ground_truth_total=0, ground_truth_validated=0)]))["arms"]["baseline"]
        self.assertIsNone(data["ground_truth_recall"])

    def test_duplicate_runs_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate run_id"):
            self.load([example(), example()])

    def test_invalid_observations_rejected(self):
        cases = [dict(model_cost="nan"), dict(model_cost="inf"), dict(human_minutes=-1),
                 dict(accepted_findings=1), dict(correct_fixes=1), dict(rescued=2),
                 dict(ground_truth_total=1), dict(ground_truth_total=1, ground_truth_validated=2),
                 dict(run_status="looks_good"), dict(accepted_outcomes="1.5")]
        for case in cases:
            with self.subTest(case=case), self.assertRaises(ValueError):
                self.load([example(**case)])

    def test_empty_dataset_rejected(self):
        with self.assertRaisesRegex(ValueError, "no run rows"):
            self.load([])

    def test_arms_remain_separate(self):
        data = summarize(self.load([example(), example(run_id="r2", arm="intervention")]))
        self.assertEqual(set(data["arms"]), {"baseline", "intervention"})
        self.assertEqual(data["arms"]["baseline"]["initiated_runs"], 1)


if __name__ == "__main__":
    unittest.main()
