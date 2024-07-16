import unittest

import numpy as np

from src.testing.base.base_test_case import BaseTestCase
from src.training.evaluating.evaluate import evaluate_multi_class_classification


class TestEvaluate(BaseTestCase):

    def _verify_metrics_dict(self, metrics, expected_metrics):
        """ Verify that the Metrics dictionary contains expected keys and types. """

        for metric, expected_type in expected_metrics.items():
            self.assertIn(metric, metrics)
            self.assertIsInstance(metrics[metric], expected_type)

    def test_multi_class_classification(self):
        y_true = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0]])
        y_pred = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        metrics = evaluate_multi_class_classification(y_true, y_pred)
        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
        }
        self._verify_metrics_dict(metrics, expected_metrics)


if __name__ == "__main__":
    unittest.main()
