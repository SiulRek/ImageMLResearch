import unittest
import tensorflow as tf

from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase
from imlresearch.src.training.trainer import Trainer


class TestTrainer(BaseTestCase):
    """
    Tests for the Trainer class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the datasets for testing.
        """
        super().setUpClass()
        cls.train_dataset = cls.load_mnist_digits_dataset(
            sample_num=1000, labeled=True
        ).batch(32)
        cls.val_dataset = cls.load_mnist_digits_dataset(
            sample_num=200, labeled=True
        ).batch(32)
        cls.test_dataset = cls.load_mnist_digits_dataset(
            sample_num=300, labeled=True
        ).batch(32)

    def setUp(self):
        """
        Initialize Trainer and ResearchAttributes.
        """
        super().setUp()
        self.trainer = Trainer()
        self.class_names = [str(i) for i in range(10)]
        research_attributes = ResearchAttributes(
            label_type="multi_class",
            class_names=self.class_names,
        )
        research_attributes._datasets_container = {
            "train_dataset": self.train_dataset,
            "val_dataset": self.val_dataset,
            "test_dataset": self.test_dataset,
        }
        self.trainer.synchronize_research_attributes(research_attributes)

    def _create_compiled_model(self):
        """
        Create and compile a simple Keras model.

        Returns
        -------
        tf.keras.Model
            A compiled Keras model.
        """
        model = tf.keras.models.Sequential(
            [
                tf.keras.layers.Flatten(input_shape=(28, 28, 3)),
                tf.keras.layers.Dense(128, activation="relu"),
                tf.keras.layers.Dense(10, activation="softmax"),
            ]
        )
        model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy"],
        )
        return model

    def _verify_metrics_dict(self, metrics, set_len=3):
        """
        Verify that the metrics dictionary contains expected keys and types.

        Parameters
        ----------
        metrics : dict
            The computed metrics dictionary.
        set_len : int
            Expected number of dataset metrics.
        """
        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
            "classification_report": dict,
        }

        self.assertEqual(len(metrics), set_len)
        for metrics_set in metrics.values():
            self.assertEqual(len(metrics_set), len(expected_metrics))
            for metric, expected_type in expected_metrics.items():
                self.assertIn(metric, metrics_set)
                self.assertIsInstance(metrics_set[metric], expected_type)

            report = metrics_set["classification_report"]
            for class_name in self.class_names:
                self.assertIn(class_name, report)

    def test_set_compiled_model(self):
        """
        Test setting a compiled model.
        """
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        self.assertIs(self.trainer.model, model)

    def test_get_labels_tensor(self):
        """
        Test extracting labels from dataset.
        """
        label_tensor = self.trainer._get_labels_tensor("train_dataset")
        self.assertIsInstance(label_tensor, tf.Tensor)
        self.assertEqual(label_tensor.shape[1], 10)

    def test_fit_predict_evaluate(self):
        """
        Test the full training, prediction, and evaluation pipeline.
        """
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

        self.assertIsNotNone(self.trainer.training_history)
        self.assertIn("train_output", self.trainer.outputs_container)
        self.assertIn("val_output", self.trainer.outputs_container)
        self.assertIn("test_output", self.trainer.outputs_container)
        self.assertIsNotNone(self.trainer.evaluation_metrics)

        self._verify_metrics_dict(self.trainer.evaluation_metrics)

    def test_fit_predict_evaluate_unbatched_dataset(self):
        """
        Test error handling when training on an unbatched dataset.
        """
        self.trainer._datasets_container["train_dataset"] = (
            self.train_dataset.unbatch()
        )
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)

        with self.assertRaises(ValueError):
            self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

    def test_fit_predict_evaluate_no_val_dataset(self):
        """
        Test training when no validation dataset is provided.
        """
        self.trainer._datasets_container.pop("val_dataset")
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

        self.assertIsNotNone(self.trainer.training_history)
        self.assertIn("train_output", self.trainer.outputs_container)
        self.assertIn("test_output", self.trainer.outputs_container)
        self.assertIsNotNone(self.trainer.evaluation_metrics)

        self._verify_metrics_dict(self.trainer.evaluation_metrics, set_len=2)

    def test_fit_predict_evaluate_no_dataset_for_training(self):
        """
        Test error handling when no training dataset is provided.
        """
        self.trainer._datasets_container.pop("train_dataset")
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)

        with self.assertRaises(ValueError):
            self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

    def test_fit_predict_evaluate_only_complete_dataset(self):
        """
        Test error handling when only a complete dataset is provided.
        """
        dataset = self.trainer._datasets_container.pop("train_dataset")
        self.trainer._datasets_container.pop("val_dataset")
        self.trainer._datasets_container.pop("test_dataset")
        self.trainer._datasets_container["complete_dataset"] = dataset
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)

        with self.assertRaises(ValueError):
            self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

    def test_fit_predict_evaluate_no_test_dataset(self):
        """
        Test warning when no test dataset is provided.
        """
        self.trainer._datasets_container.pop("test_dataset")
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)

        with self.assertWarns(UserWarning):
            self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

        self.assertIsNotNone(self.trainer.training_history)
        self.assertIn("train_output", self.trainer.outputs_container)
        self.assertIn("val_output", self.trainer.outputs_container)
        self.assertIsNotNone(self.trainer.evaluation_metrics)

        self._verify_metrics_dict(self.trainer.evaluation_metrics, set_len=2)

    def test_contents_of_output_container_after_fit_predict_evaluate(self):
        """
        Test the structure of outputs stored after training.
        """
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

        self.assertIn("train_output", self.trainer.outputs_container)
        self.assertIn("val_output", self.trainer.outputs_container)
        self.assertIn("test_output", self.trainer.outputs_container)

        output = self.trainer.outputs_container["train_output"]
        self.assertIsInstance(output, tuple)

        for true_label, pred_label in zip(*output):
            self.assertEqual(len(true_label), len(pred_label))
            self.assertEqual(len(true_label), 10)


if __name__ == "__main__":
    unittest.main()
