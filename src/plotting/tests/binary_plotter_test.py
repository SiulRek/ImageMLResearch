import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt
import tensorflow as tf

from src.plotting.plotters.binary_plotter import BinaryPlotter
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase


class TestBinaryPlotter(BaseTestCase):
    """ Test suite for the BinaryPlotter class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        sample_num = 100
        dataset = cls.load_mnist_digits_dataset(
            sample_num=sample_num, labeled=True, binary=True
        )
        cls.class_names = ["Digit 0", "Digit 1"]
        y_true = cls._get_labels_array(dataset)
        y_pred = tf.random.uniform((sample_num,), minval=0, maxval=1, dtype=tf.float32)

        cls.binary_plotter = BinaryPlotter()
        research_attributes = ResearchAttributes(
            label_type="binary", class_names=cls.class_names
        )
        research_attributes._datasets_container["complete_dataset"] = dataset
        cls.binary_plotter.synchronize_research_attributes(research_attributes)
        cls.binary_plotter._retrieve_test_output_data = MagicMock(
            return_value=(y_true, y_pred)
        )
        cls.binary_plotter._retrieve_class_names = MagicMock(
            return_value=cls.class_names
        )

    def setUp(self):
        super().setUp()
        self.binary_plotter._figures = {}  # Reset figures before each test

    @classmethod
    def _get_labels_array(cls, dataset):
        labels_list = []
        for _, labels in dataset:
            labels_list.append(tf.expand_dims(labels, axis=0))

        labels_tensor = tf.concat(labels_list, axis=0)
        return labels_tensor

    def test_plot_confusion_matrix(self):
        """ Test the plot_confusion_matrix method. """
        fig = self.binary_plotter.plot_confusion_matrix(
            title="Test Confusion Matrix", show=False
        )
        self.assertEqual(
            len(self.binary_plotter._figures), 1, "The figure was not added."
        )
        self.assertIn(
            "test_confusion_matrix",
            self.binary_plotter._figures,
            "The figure name is incorrect.",
        )
        fig.savefig(
            os.path.join(self.results_dir, "binary_plotter_plot_confusion_matrix.png")
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    self.results_dir, "binary_plotter_plot_confusion_matrix.png"
                )
            ),
            "Confusion matrix figure was not saved.",
        )

    def test_plot_images(self):
        """ Test the plot_images method. """
        fig = self.binary_plotter.plot_images(grid_size=(2, 2))
        self.assertEqual(
            len(self.binary_plotter._figures), 1, "The figure was not added."
        )
        self.assertIn(
            "images",
            self.binary_plotter._figures,
            "The figure name is incorrect.",
        )
        fig.savefig(os.path.join(self.results_dir, "binary_plotter_plot_images.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "binary_plotter_plot_images.png")
            ),
            "Images figure was not saved.",
        )

    def test_plot_roc_curve(self):
        """ Test the plot_roc_curve method. """
        fig = self.binary_plotter.plot_roc_curve(title="Test ROC Curve", show=False)
        self.assertEqual(
            len(self.binary_plotter._figures), 1, "The figure was not added."
        )
        self.assertIn(
            "test_roc_curve",
            self.binary_plotter._figures,
            "The figure name is incorrect.",
        )
        fig.savefig(os.path.join(self.results_dir, "binary_plotter_plot_roc_curve.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "binary_plotter_plot_roc_curve.png")
            ),
            "ROC curve figure was not saved.",
        )

    def test_plot_pr_curve(self):
        """ Test the plot_pr_curve method. """
        fig = self.binary_plotter.plot_pr_curve(title="Test PR Curve", show=False)
        self.assertEqual(
            len(self.binary_plotter._figures), 1, "The figure was not added."
        )
        self.assertIn(
            "test_pr_curve",
            self.binary_plotter._figures,
            "The figure name is incorrect.",
        )
        fig.savefig(os.path.join(self.results_dir, "binary_plotter_plot_pr_curve.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "binary_plotter_plot_pr_curve.png")
            ),
            "PR curve figure was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
