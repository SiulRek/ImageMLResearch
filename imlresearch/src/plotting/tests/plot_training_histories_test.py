import os
import unittest

import tensorflow as tf

from imlresearch.src.plotting.functions.plot_training_histories import (
    plot_training_histories,
)
from imlresearch.src.plotting.tests.plotting_test_case import PlottingTestCase


class TestPlotTrainingHistories(PlottingTestCase):
    """
    Test suite for the plot_training_histories function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test class by creating a dummy Keras model and generating
        training histories for multiple models.
        """
        super().setUpClass()
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_training_histories_test.png"
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

        # Generate training histories for multiple models
        cls.history1 = cls.model.fit(
            cls.train_dataset,
            epochs=5,
            validation_data=cls.val_dataset,
            verbose=0,
        ).history
        cls.history2 = cls.model.fit(
            cls.train_dataset,
            epochs=5,
            validation_data=cls.val_dataset,
            verbose=0,
        ).history

        cls.histories = {"Model 1": cls.history1, "Model 2": cls.history2}

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

    def test_plot_training_histories(self):
        """
        Tests plotting training histories for multiple models.
        """
        fig = plot_training_histories(self.histories)
        self._save_and_close_figure(fig, "plot_training_histories.png")

    def test_plot_training_histories_with_title(self):
        """
        Tests plotting training histories with a title.
        """
        fig = plot_training_histories(
            self.histories, title="Training Histories"
        )
        self._save_and_close_figure(
            fig, "plot_training_histories_with_title.png"
        )

    def test_plot_training_histories_with_missing_metrics(self):
        """
        Tests plotting training histories with missing metrics.
        """
        # Remove a metric from the history of one model
        self.histories["Model 1"].pop("accuracy")
        self.histories["Model 1"].pop("val_accuracy")

        fig = plot_training_histories(self.histories)
        self._save_and_close_figure(
            fig, "plot_training_histories_missing_metrics.png"
        )

    def test_plot_training_histories_with_different_epoch_lengths(self):
        """
        Tests plotting training histories with different epoch lengths.
        """
        # Create a new history with a different epoch length
        history3 = self.model.fit(
            self.train_dataset,
            epochs=7,
            validation_data=self.val_dataset,
            verbose=0,
        ).history
        histories = self.histories.copy()
        histories["Model 3"] = history3

        fig = plot_training_histories(histories)
        self._save_and_close_figure(
            fig, "plot_training_histories_different_epoch_lengths.png"
        )


if __name__ == "__main__":
    unittest.main()
