import os
import unittest

import tensorflow as tf

from imlresearch.src.plotting.functions.plot_training_history import (
    plot_training_history,
)
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotTrainingHistory(PlottingTestCase):
    """
    Test suite for the plot_training_history function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class by creating a dummy Keras model and generating
        training history with and without validation data.
        """
        super().setUpClass()
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_training_history_test.png"
        )

        # Create a dummy Keras model for generating training history
        cls.model = tf.keras.models.Sequential(
            [
                tf.keras.layers.Flatten(input_shape=(28, 28, 3)),
                tf.keras.layers.Rescaling(1.0 / 255),
                tf.keras.layers.Dense(10, activation="relu"),
                tf.keras.layers.Dense(10, activation="softmax"),
            ]
        )
        cls.model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy"],
        )

        # Load MNIST data for generating training history
        cls.train_dataset, cls.val_dataset = cls.load_mnist_data()

        # Generate training history with and without validation data
        cls.history_with_val = cls.model.fit(
            cls.train_dataset,
            epochs=5,
            validation_data=cls.val_dataset,
            verbose=0,
        ).history
        cls.history_without_val = cls.model.fit(
            cls.train_dataset,
            epochs=5,
            verbose=0,
        ).history

    @classmethod
    def load_mnist_data(cls):
        """
        Loads MNIST data for generating training history.

        Returns
        -------
        tuple
            A tuple containing training and validation datasets.
        """
        dataset = cls.load_mnist_digits_dataset(sample_num=1000, labeled=True)
        dataset = dataset.shuffle(10000)

        train_size = int(0.8 * len(list(dataset)))
        train_dataset = dataset.take(train_size).batch(32)
        val_dataset = dataset.skip(train_size).batch(32)

        return train_dataset, val_dataset

    def test_plot_training_history_with_validation(self):
        """
        Tests plotting training history with validation data.
        """
        fig = plot_training_history(self.history_with_val)
        self._save_and_close_figure(fig, "plot_training_history_with_val.png")

    def test_plot_training_history_without_validation(self):
        """
        Tests plotting training history without validation data.
        """
        fig = plot_training_history(self.history_without_val)
        self._save_and_close_figure(
            fig, "plot_training_history_without_val.png"
        )

    def test_plot_training_history_with_multiple_metrics(self):
        """
        Tests plotting training history with multiple metrics.
        """
        # Add another metric to the model
        self.model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy", "mae"],
        )
        history_multiple_metrics = self.model.fit(
            self.train_dataset,
            epochs=5,
            validation_data=self.val_dataset,
            verbose=0,
        ).history

        fig = plot_training_history(history_multiple_metrics)
        self._save_and_close_figure(
            fig, "plot_training_history_multiple_metrics.png"
        )


if __name__ == "__main__":
    unittest.main()
