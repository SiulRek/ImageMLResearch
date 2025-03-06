import unittest
import numpy as np

from imlresearch.src.testing.bases.base_test_case import BaseTestCase
from imlresearch.src.training.evaluating.evaluate import (
    evaluate_binary_classification,
    evaluate_multi_class_classification,
)


class TestEvaluate(BaseTestCase):
    """
    Tests for evaluation functions.
    """

    def _verify_metrics_dict(self, metrics, expected_metrics):
        """
        Verify that the metrics dictionary contains expected keys and types.

        Parameters
        ----------
        metrics : dict
            The computed metrics dictionary.
        expected_metrics : dict
            Expected keys and corresponding types.
        """
        for metric, expected_type in expected_metrics.items():
            self.assertIn(metric, metrics)
            self.assertIsInstance(metrics[metric], expected_type)

    def test_binary_classification(self):
        """
        Test binary classification evaluation.
        """
        y_true = np.array([0, 1, 0, 1, 0, 1, 1, 0])
        y_pred = np.array([0, 1, 0, 1, 1, 0, 1, 0])

        metrics = evaluate_binary_classification(y_true, y_pred)

        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
            "classification_report": dict,
        }
        self._verify_metrics_dict(metrics, expected_metrics)

    def test_binary_classification_with_class_names(self):
        """
        Test binary classification evaluation with class names.
        """
        y_true = np.array([0, 1, 0, 1, 0, 1, 1, 0])
        y_pred = np.array([0, 1, 0, 1, 1, 0, 1, 0])
        class_names = ["class1", "class2"]

        metrics = evaluate_binary_classification(y_true, y_pred, class_names)

        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
            "classification_report": dict,
        }
        self._verify_metrics_dict(metrics, expected_metrics)

        report = metrics["classification_report"]
        self.assertIn("class1", report)
        self.assertIn("class2", report)

    def test_multi_class_classification(self):
        """
        Test multi-class classification evaluation.
        """
        y_true = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0]])
        y_pred = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        metrics = evaluate_multi_class_classification(y_true, y_pred)

        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
            "classification_report": dict,
        }
        self._verify_metrics_dict(metrics, expected_metrics)

    def test_multi_class_classification_with_class_names(self):
        """
        Test multi-class classification evaluation with class names.
        """
        y_true = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0]])
        y_pred = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        class_names = ["class1", "class2", "class3"]

        metrics = evaluate_multi_class_classification(
            y_true, y_pred, class_names
        )

        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
            "classification_report": dict,
        }
        self._verify_metrics_dict(metrics, expected_metrics)

        report = metrics["classification_report"]
        self.assertIn("class1", report)
        self.assertIn("class2", report)
        self.assertIn("class3", report)


if __name__ == "__main__":
    unittest.main()
