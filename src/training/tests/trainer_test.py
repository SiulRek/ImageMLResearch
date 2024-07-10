import unittest

import tensorflow as tf

from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase
from src.training.trainer import Trainer


class TestTrainer(BaseTestCase):

    @classmethod
    def setUpClass(cls):
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
        super().setUp()
        self.trainer = Trainer()
        research_attributes = ResearchAttributes(
            label_type="multi_class", class_names=[str(i) for i in range(10)]
        )
        # To skip loading of datasets with DataHandler,
        # the attribute is set directly to private attribute of Trainer.
        research_attributes._datasets_container = {
            "train_dataset": self.train_dataset,
            "val_dataset": self.val_dataset,
            "test_dataset": self.test_dataset,
        }
        self.trainer.synchronize_research_attributes(research_attributes)

    def _create_compiled_model(self):
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

    def _verify_metrics_dict(self, metrics):
        """ Verify that the metrics dictionary contains expected keys and types. """
        expected_metrics = {
            "accuracy": float,
            "precision": float,
            "recall": float,
            "f1": float,
            "classification_report": str,
        }

        for metric, expected_type in expected_metrics.items():
            self.assertIn(metric, metrics)
            self.assertIsInstance(metrics[metric], expected_type)

    def test_set_compiled_model(self):
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        self.assertIs(self.trainer.model, model)

    def test_fit_predict_evaluate(self):
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
        self.trainer._datasets_container["train_dataset"] = self.train_dataset.unbatch()
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        with self.assertRaises(ValueError):
            self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

    def test_fit_predict_evaluate_no_val_dataset(self):
        self.trainer._datasets_container.pop("val_dataset")
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)
        self.assertIsNotNone(self.trainer.training_history)
        self.assertIn("train_output", self.trainer.outputs_container)
        self.assertIn("test_output", self.trainer.outputs_container)
        self.assertIsNotNone(self.trainer.evaluation_metrics)
        self._verify_metrics_dict(self.trainer.evaluation_metrics)

    def test_fit_predict_evaluate_no_dataset_for_training(self):
        self.trainer._datasets_container.pop("train_dataset")
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        with self.assertRaises(ValueError):
            self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

    def test_fit_predict_evaluate_no_dataset_for_evaluation(self):
        self.trainer._datasets_container.pop("test_dataset")
        model = self._create_compiled_model()
        self.trainer.set_compiled_model(model)
        with self.assertRaises(ValueError):
            self.trainer.fit_predict_evaluate(epochs=5, steps_per_epoch=5)

    def test_contents_of_output_container_after_fit_predict_evaluate(self):
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
