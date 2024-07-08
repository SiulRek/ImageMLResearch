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
        dataset = cls.load_mnist_digits_dataset(sample_num=sample_num, labeled=True)
        dataset = dataset.map(lambda x, y: (x, cls._map_even_odd_label(y)))
        cls.class_names = ["Odd", "Even"]
        y_true = cls._get_labels_tensor(dataset)
        y_pred = tf.random.uniform((sample_num,), minval=0, maxval=2, dtype=tf.int32)

        cls.binary_plotter = BinaryPlotter()
        research_attributes = ResearchAttributes(
            label_type="binary", class_names=cls.class_names
        )
        research_attributes._datasets_container["complete_dataset"] = dataset
        cls.binary_plotter.synchronize_research_attributes(research_attributes)
        cls.binary_plotter._retrieve_output_data = MagicMock(
            return_value=(y_true, y_pred, cls.class_names)
        )

    def setUp(self):
        super().setUp()
        self.binary_plotter._figures = {}  # Reset figures before each test

    @classmethod
    def _get_labels_tensor(cls, dataset):
        labels_list = []
        for _, labels in dataset:
            labels_list.append(tf.expand_dims(labels, axis=0))
        labels_tensor = tf.concat(labels_list, axis=0)
        return labels_tensor

    @classmethod
    def _map_even_odd_label(cls, label):
        """ Process labels from one-hot to binary (even=0, odd=1). """
        label = tf.argmax(label, axis=0)
        label = tf.where(label % 2 == 0, 1, 0)  # Even=1, Odd=0
        return label

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


if __name__ == "__main__":
    unittest.main()
