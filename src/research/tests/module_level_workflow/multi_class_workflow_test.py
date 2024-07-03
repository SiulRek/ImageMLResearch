import os
import shutil
import unittest
from src.testing.helpers.empty_directory import empty_directory
import tensorflow as tf

from src.data_handling.data_handler import DataHandler
from src.experimenting.experiment import Experiment
from src.plotting.plotters.multi_class_plotter import MultiClassPlotter
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase
from src.training.trainer import Trainer


class TestMultiClassWorkflow(BaseTestCase):
    """ Test case for the multi-class research workflow on module level. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        empty_directory(cls.results_dir)

    def setUp(self):
        super().setUp()
        self.research_attributes = ResearchAttributes(
            label_type="multi_class", class_names=["Digit " + str(i) for i in range(10)]
        )
        self.data_handler = DataHandler()
        # Only synchronize the research attributes for the data handler
        # as it is the first, the rest will be synchronized later.
        self.data_handler.synchronize_research_attributes(self.research_attributes)
        self.trainer = Trainer()
        self.plotter = MultiClassPlotter()

    def _create_compiled_model(self, units):
        model = tf.keras.models.Sequential(
            [
                tf.keras.layers.Flatten(input_shape=(28, 28, 3)),
                tf.keras.layers.Dense(units, activation="relu"),
                tf.keras.layers.Dense(10, activation="softmax"),
            ]
        )
        model.compile(
            optimizer="adam",
            loss="categorical_crossentropy",
            metrics=["accuracy"],
        )
        return model

    def test_workflow(self):
        def assert_datasets_container(module):
            has_datasets_container = (
                hasattr(module, "datasets_container")
                and module.datasets_container is not None
            )
            self.assertTrue(
                has_datasets_container,
                f"The {str(module)} does not have a datasets container.",
            )
            for dataset_name in ["train_dataset", "val_dataset", "test_dataset"]:
                self.assertIn(
                    dataset_name,
                    module.datasets_container,
                    f"{dataset_name} is not in the datasets container.",
                )

        def assert_outputs_container(module):
            has_outputs_container = (
                hasattr(module, "outputs_container")
                and module.outputs_container is not None
            )
            self.assertTrue(
                has_outputs_container,
                f"The {str(module)} does not have an outputs container.",
            )
            for output_name in ["train_output", "val_output", "test_output"]:
                self.assertIn(
                    output_name,
                    module.outputs_container,
                    f"{output_name} is not in the outputs container.",
                )

        # #### Dataset Handling ####
        dataset = self.load_mnist_digits_dataset(sample_num=1000, labeled=True)
        self.data_handler.load_dataset(dataset)
        self.data_handler.split_dataset(train_size=0.7, val_size=0.15, test_size=0.15)
        assert_datasets_container(self.data_handler)
        self.data_handler.enhance_datasets(
            ["train_dataset", "val_dataset", "test_dataset"],
            batch_size=32,
            shuffle=True,
            random_seed=42,
            prefetch_buffer_size=10,
            repeat_num=1,
        )
        self.data_handler.backup_datasets()
        self.data_handler.restore_datasets()
        assert_datasets_container(self.data_handler)

        #### Experimenting ####
        trial_definitions = [
            {
                "name": "Trial 1",
                "description": "Description of the first trial",
                "hyperparameters": {"units": 128},
            },
            {
                "name": "Trial 2",
                "description": "Description of the second trial",
                "hyperparameters": {"units": 256},
            },
        ]

        with Experiment(
            self.data_handler,
            directory=self.results_dir,
            name="test_experiment",
            description="A test experiment",
            report_kwargs={},
        ) as experiment:
            assert_datasets_container(experiment)
            self.assertTrue(
                os.path.exists(experiment.experiment_data["directory"]),
                "The experiment directory does not exist.",
            )
            for i, trial_definition in enumerate(trial_definitions):
                with experiment.trial(**trial_definition) as trial:
                    # ## Training ##
                    self.assertTrue(
                        os.path.exists(trial.trial_data["directory"]),
                        "The trial directory does not exist.",
                    )
                    self.trainer.synchronize_research_attributes(experiment)
                    assert_datasets_container(self.trainer)
                    model = self._create_compiled_model(
                        trial_definition["hyperparameters"]["units"]
                    )
                    self.trainer.set_compiled_model(model)
                    self.trainer.fit_predict_evaluate(
                        epochs=10, steps_per_epoch=10, validation_steps=5
                    )
                    assert_outputs_container(self.trainer)
                    has_evaluation_metrics = (
                        hasattr(self.trainer, "evaluation_metrics")
                        and self.trainer.evaluation_metrics is not None
                    )
                    self.assertTrue(
                        has_evaluation_metrics,
                        "The trainer does not have evaluation metrics.",
                    )

                    # ## Plotting ##
                    self.plotter.synchronize_research_attributes(self.trainer)
                    assert_outputs_container(self.plotter)
                    has_training_history = (
                        hasattr(self.trainer, "training_history")
                        and self.trainer.training_history is not None
                    )
                    self.assertTrue(
                        has_training_history,
                        "The trainer does not have a training history.",
                    )
                    has_output_container = (
                        hasattr(self.plotter, "outputs_container")
                        and self.plotter.outputs_container is not None
                    )
                    self.assertTrue(
                        has_output_container,
                        "The plotter does not have an output container.",
                    )
                    self.plotter.plot_training_history(title="Training History")
                    self.plotter.plot_confusion_matrix(title="Confusion Matrix")
                    experiment.synchronize_research_attributes(self.plotter)

                self.assertEqual(
                    len(experiment.experiment_data["trials"]),
                    i + 1,
                    "The number of trials is incorrect.",
                )


if __name__ == "__main__":
    unittest.main()
