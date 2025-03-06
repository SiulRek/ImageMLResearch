import unittest
from unittest.mock import MagicMock

import tensorflow as tf

from imlresearch.src.plotting.plotters.binary_plotter import BinaryPlotter
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)


class TestBinaryPlotter(PlottingTestCase):
    """
    Test suite for the BinaryPlotter class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class by initializing a BinaryPlotter instance
        with sample binary classification data.
        """
        super().setUpClass()
        sample_num = 100
        dataset = cls.load_mnist_digits_dataset(
            sample_num=sample_num, labeled=True, binary=True
        )
        cls.class_names = ["Digit 0", "Digit 1"]
        x, y_true = cls._get_images_and_labels_array(dataset)
        y_pred = tf.random.uniform(
            (sample_num,), minval=0, maxval=1, dtype=tf.float32
        )

        cls.binary_plotter = BinaryPlotter()
        research_attributes = ResearchAttributes(
            label_type="binary", class_names=cls.class_names
        )
        research_attributes._datasets_container["complete_dataset"] = dataset
        cls.binary_plotter.synchronize_research_attributes(research_attributes)
        cls.binary_plotter._retrieve_test_output_data = MagicMock(
            return_value=(y_true, y_pred)
        )
        cls.binary_plotter._retrieve_test_input_output_data = MagicMock(
            return_value=(x, y_true, y_pred)
        )
        cls.binary_plotter._retrieve_class_names = MagicMock(
            return_value=cls.class_names
        )

    def setUp(self):
        """
        Resets figures before each test to ensure test isolation.
        """
        super().setUp()
        self.binary_plotter._figures = {}

    @classmethod
    def _get_images_and_labels_array(cls, dataset):
        """
        Extracts images and labels from the dataset and converts them
        into tensors.

        Parameters
        ----------
        dataset : tf.data.Dataset
            The dataset containing image-label pairs.

        Returns
        -------
        tuple
            A tuple containing image and label tensors.
        """
        images_list = []
        labels_list = []
        for image, label in dataset:
            images_list.append(tf.expand_dims(image, axis=0))
            labels_list.append(tf.expand_dims(label, axis=0))
        images_tensor = tf.concat(images_list, axis=0)
        labels_tensor = tf.concat(labels_list, axis=0)
        return images_tensor, labels_tensor

    def test_plot_confusion_matrix(self):
        """
        Tests the plot_confusion_matrix method.
        """
        fig = self.binary_plotter.plot_confusion_matrix(
            title="Test Confusion Matrix", show=False
        )
        self.assertEqual(len(self.binary_plotter._figures), 1)
        self.assertIn("test_confusion_matrix", self.binary_plotter._figures)
        self._save_and_close_figure(
            fig, "binary_plotter_plot_confusion_matrix.png"
        )

    def test_plot_images(self):
        """
        Tests the plot_images method.
        """
        fig = self.binary_plotter.plot_images(grid_size=(2, 2))
        self.assertEqual(len(self.binary_plotter._figures), 1)
        self.assertIn("images", self.binary_plotter._figures)
        self._save_and_close_figure(fig, "binary_plotter_plot_images.png")

    def test_plot_roc_curve(self):
        """
        Tests the plot_roc_curve method.
        """
        fig = self.binary_plotter.plot_roc_curve(
            title="Test ROC Curve", show=False
        )
        self.assertEqual(len(self.binary_plotter._figures), 1)
        self.assertIn("test_roc_curve", self.binary_plotter._figures)
        self._save_and_close_figure(fig, "binary_plotter_plot_roc_curve.png")

    def test_plot_pr_curve(self):
        """
        Tests the plot_pr_curve method.
        """
        fig = self.binary_plotter.plot_pr_curve(
            title="Test PR Curve", show=False
        )
        self.assertEqual(len(self.binary_plotter._figures), 1)
        self.assertIn("test_pr_curve", self.binary_plotter._figures)
        self._save_and_close_figure(fig, "binary_plotter_plot_pr_curve.png")

    def test_plot_results(self):
        """
        Tests the plot_results method.
        """
        fig = self.binary_plotter.plot_results(grid_size=(2, 2))
        self.assertEqual(len(self.binary_plotter._figures), 1)
        self.assertIn("results", self.binary_plotter._figures)
        self._save_and_close_figure(fig, "binary_plotter_plot_results.png")


if __name__ == "__main__":
    unittest.main()
