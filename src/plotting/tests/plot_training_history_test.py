import os
import unittest

import matplotlib.pyplot as plt
import tensorflow as tf

from src.plotting.functions.plot_training_history import plot_training_history
from src.testing.base.base_test_case import BaseTestCase


class TestPlotTrainingHistory(BaseTestCase):
    """ Test suite for the plot_training_history function. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_training_history_test.png"
        )

        # Create a dummy Keras model for generating training history
        cls.model = tf.keras.models.Sequential(
            [
                tf.keras.layers.Flatten(input_shape=(28, 28, 3)),
                tf.keras.layers.experimental.preprocessing.Rescaling(1.0 / 255),
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
            cls.train_dataset, epochs=5, validation_data=cls.val_dataset, verbose=0
        )
        cls.history_without_val = cls.model.fit(cls.train_dataset, epochs=5, verbose=0)

    @classmethod
    def load_mnist_data(cls):
        """ Load MNIST data for generating training history. """
        dataset = cls.load_mnist_digits_dataset(sample_num=1000, labeled=True)
        dataset = dataset.shuffle(10000)

        train_size = int(0.8 * len(list(dataset)))
        train_dataset = dataset.take(train_size).batch(32)
        val_dataset = dataset.skip(train_size).batch(32)

        return train_dataset, val_dataset

    def test_plot_training_history_with_validation(self):
        """ Test plotting training history with validation data. """
        fig = plot_training_history(self.history_with_val)
        fig.savefig(
            os.path.join(self.results_dir, "plot_training_history_with_val.png")
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "plot_training_history_with_val.png")
            ),
            "Plot with validation data was not saved.",
        )

    def test_plot_training_history_without_validation(self):
        """ Test plotting training history without validation data. """
        fig = plot_training_history(self.history_without_val)
        fig.savefig(
            os.path.join(self.results_dir, "plot_training_history_without_val.png")
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "plot_training_history_without_val.png")
            ),
            "Plot without validation data was not saved.",
        )

    def test_plot_training_history_with_multiple_metrics(self):
        """ Test plotting training history with multiple metrics. """
        # Add another metric to the model
        self.model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy", "mae"],
        )
        history_multiple_metrics = self.model.fit(
            self.train_dataset, epochs=5, validation_data=self.val_dataset, verbose=0
        )

        fig = plot_training_history(history_multiple_metrics)
        fig.savefig(
            os.path.join(self.results_dir, "plot_training_history_multiple_metrics.png")
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    self.results_dir, "plot_training_history_multiple_metrics.png"
                )
            ),
            "Plot with multiple metrics was not saved.",
        )


if __name__ == "__main__":
    unittest.main()
