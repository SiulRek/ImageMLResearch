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
                tf.keras.layers.Dense(10, activation="relu", input_shape=(784,)),
                tf.keras.layers.Dense(10, activation="softmax"),
            ]
        )
        cls.model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )

        # Load MNIST data for generating training history
        (x_train, y_train), (x_val, y_val) = tf.keras.datasets.mnist.load_data()
        x_train = x_train.reshape(-1, 784).astype("float32") / 255
        x_val = x_val.reshape(-1, 784).astype("float32") / 255

        # Generate training history with and without validation data
        cls.mnist_data = (x_train, y_train, x_val, y_val)
        cls.history_with_val = cls.model.fit(
            x_train, y_train, epochs=5, validation_data=(x_val, y_val), verbose=0
        )
        cls.history_without_val = cls.model.fit(x_train, y_train, epochs=5, verbose=0)

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
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy", "mae"],
        )
        x_train, y_train, x_val, y_val = self.mnist_data
        history_multiple_metrics = self.model.fit(
            x_train, y_train, epochs=5, validation_data=(x_val, y_val), verbose=0
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
