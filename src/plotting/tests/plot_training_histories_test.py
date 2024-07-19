import os
import unittest

import matplotlib.pyplot as plt
import tensorflow as tf

from src.plotting.functions.plot_training_histories import plot_training_histories
from src.testing.base.base_test_case import BaseTestCase


class TestPlotTrainingHistories(BaseTestCase):
    """ Test suite for the plot_training_histories function. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.visualization_path = os.path.join(
            cls.results_dir, "plot_training_histories_test.png"
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

        # Generate training histories for multiple models
        cls.history1 = cls.model.fit(
            cls.train_dataset, epochs=5, validation_data=cls.val_dataset, verbose=0
        ).history
        cls.history2 = cls.model.fit(
            cls.train_dataset, epochs=5, validation_data=cls.val_dataset, verbose=0
        ).history

        cls.histories = {"Model 1": cls.history1, "Model 2": cls.history2}

    @classmethod
    def load_mnist_data(cls):
        """ Load MNIST data for generating training history. """
        dataset = cls.load_mnist_digits_dataset(sample_num=1000, labeled=True)
        dataset = dataset.shuffle(10000)

        train_size = int(0.8 * len(list(dataset)))
        train_dataset = dataset.take(train_size).batch(32)
        val_dataset = dataset.skip(train_size).batch(32)

        return train_dataset, val_dataset

    def test_plot_training_histories(self):
        """ Test plotting training histories for multiple models. """
        fig = plot_training_histories(self.histories)
        fig.savefig(os.path.join(self.results_dir, "plot_training_histories.png"))
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(self.results_dir, "plot_training_histories.png")
            ),
            "Combined plot for multiple training histories was not saved.",
        )

    def test_plot_training_histories_with_missing_metrics(self):
        """ Test plotting training histories with missing metrics. """
        # Remove a metric from the history of one model
        self.histories["Model 1"].pop("accuracy")
        self.histories["Model 1"].pop("val_accuracy")

        fig = plot_training_histories(self.histories)
        fig.savefig(
            os.path.join(
                self.results_dir, "plot_training_histories_missing_metrics.png"
            )
        )
        plt.close(fig)
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    self.results_dir, "plot_training_histories_missing_metrics.png"
                )
            )
        )


if __name__ == "__main__":
    unittest.main()
