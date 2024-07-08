import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt
import tensorflow as tf

from src.plotting.plotters.multi_class_plotter import MultiClassPlotter
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase


class TestMultiClassPlotter(BaseTestCase):
    """ Test suite for the MultiClassPlotter class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        sample_num = 100
        dataset = cls.load_mnist_digits_dataset(sample_num=sample_num, labeled=True)
        cls.class_names = ["Digit " + str(i) for i in range(10)]
        y_true = cls._get_labels_tensor(dataset)
        y_pred = cls._get_random_preds_tensor(sample_num)
        cls.multi_class_plotter = MultiClassPlotter()
        research_attributes = ResearchAttributes(
            label_type="multi_class", class_names=cls.class_names
        )
        research_attributes._datasets_container["complete_dataset"] = dataset
        cls.multi_class_plotter.synchronize_research_attributes(research_attributes)
        cls.multi_class_plotter._retrieve_output_data = MagicMock(
            return_value=(y_true, y_pred, cls.class_names)
        )

    def setUp(self):
        super().setUp()
        self.multi_class_plotter._figures = {}  # Reset figures before each test

    @classmethod
    def _get_labels_tensor(cls, dataset):
        labels_list = []
        for _, labels in dataset:
            labels_list.append(tf.expand_dims(labels, axis=0))

        labels_tensor = tf.concat(labels_list, axis=0)
        return labels_tensor

    @classmethod
    def _get_random_preds_tensor(cls, sample_num):
        preds = tf.random.uniform((sample_num,), minval=0, maxval=10, dtype=tf.int32)
        preds = tf.one_hot(preds, depth=10)
        return preds

    def test_plot_images(self):
        """ Test the plot_images method. """
        fig = self.multi_class_plotter.plot_images(grid_size=(2, 2))
        self.assertEqual(
            len(self.multi_class_plotter.figures), 1, "The figure was not added."
        )
        self.assertIn(
            "images",
            self.multi_class_plotter.figures,
            "The figure name is incorrect.",
        )
        fig.savefig(
            os.path.join(self.results_dir, "multi_class_plotter_plot_images.png")
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "multi_class_plotter_plot_images.png")
            ),
            "Images figure was not saved.",
        )

    def test_plot_confusion_matrix(self):
        """ Test the plot_confusion_matrix method. """
        fig = self.multi_class_plotter.plot_confusion_matrix(
            title="Test Confusion Matrix", show=False
        )
        self.assertEqual(
            len(self.multi_class_plotter.figures), 1, "The figure was not added."
        )
        self.assertIn(
            "test_confusion_matrix",
            self.multi_class_plotter.figures,
            "The figure name is incorrect.",
        )
        fig.savefig(
            os.path.join(
                self.results_dir, "multi_class_plotter_plot_confusion_matrix.png"
            )
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    self.results_dir, "multi_class_plotter_plot_confusion_matrix.png"
                )
            ),
            "Confusion matrix figure was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
