import os
import unittest

import numpy as np
import tensorflow as tf

from src.testing.base.base_test_case import BaseTestCase
from src.training.evaluating.evaluate_classification import evaluate_classification


class TestEvaluateClassification(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.log_file_path = os.path.join(cls.results_dir, "classification_reports.txt")
        if os.path.exists(cls.log_file_path):
            os.remove(cls.log_file_path)

    def log_classification_report(self, method_name, classification_report):
        """ Log the classification report to a file. """
        open_mode = "a" if os.path.exists(self.log_file_path) else "w"
        with open(self.log_file_path, open_mode, encoding="utf-8") as log_file:
            log_file.write(f"{method_name}\n" + classification_report + "\n\n")

    def _verify_metrics_dict(self, metrics):
        """ Verify that the metrics dictionary contains expected keys and types. """
        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
            "classification_report": str
        }
        
        for metric, expected_type in expected_metrics.items():
            self.assertIn(metric, metrics)
            self.assertIsInstance(metrics[metric], expected_type)

    def test_numpy_arrays(self):
        y_true = np.array([0, 1, 1, 0])
        y_pred = np.array([0, 1, 0, 0])
        class_names = ["class_0", "class_1"]
        metrics = evaluate_classification(y_true, y_pred, class_names)
        self._verify_metrics_dict(metrics)
        self.log_classification_report(
            "test_numpy_arrays", metrics["classification_report"]
        )

    def test_binary_classification(self):
        y_true = tf.constant([0, 1, 1, 0])
        y_pred = tf.constant([0, 1, 0, 0])
        class_names = ["class_0", "class_1"]
        metrics = evaluate_classification(y_true, y_pred, class_names)
        self._verify_metrics_dict(metrics)
        self.log_classification_report(
            "test_binary_classification", metrics["classification_report"]
        )

    def test_multi_class_classification(self):
        y_true = np.array(
            [[1, 0, 0], [0, 1, 0], [1, 0, 0]]
        )
        y_pred = np.array(
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        )
        class_names = ["class_0", "class_1", "class_2"]
        metrics = evaluate_classification(y_true, y_pred, class_names)
        self._verify_metrics_dict(metrics)
        self.log_classification_report(
            "test_multi_class_classification", metrics["classification_report"]
        )

    def test_multi_label_classification(self):
        y_true = tf.constant([[1, 0, 1], [0, 1, 0], [1, 1, 1]])
        y_pred = tf.constant([[1, 0, 0], [0, 1, 0], [1, 0, 1]])
        class_names = ["class_0", "class_1", "class_2"]
        metrics = evaluate_classification(y_true, y_pred, class_names)
        self._verify_metrics_dict(metrics)
        self.log_classification_report(
            "test_multi_label_classification", metrics["classification_report"]
        )


if __name__ == "__main__":
    unittest.main()
