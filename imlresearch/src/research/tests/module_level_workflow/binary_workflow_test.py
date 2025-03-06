import os
import unittest

import tensorflow as tf

from imlresearch.src.data_handling.data_handler import DataHandler
from imlresearch.src.experimenting.experiment import Experiment
from imlresearch.src.plotting.plotters.binary_plotter import BinaryPlotter
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase
from imlresearch.src.testing.helpers.empty_directory import empty_directory
from imlresearch.src.training.trainer import Trainer


class TestBinaryModuleLevelWorkflow(BaseTestCase):
    """
    Test case for the binary classification research workflow at the
    module level.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment for all test cases.

        This method clears the results directory before running tests.
        """
        super().setUpClass()
        empty_directory(cls.results_dir)

    def setUp(self):
        """
        Set up the test environment before each test case.

        This initializes research attributes, data handlers, trainers,
        and plotters.
        """
        super().setUp()
        self.research_attributes = ResearchAttributes(
            label_type="binary",
            class_names=["Digit 0", "Digit 1"],
        )
        self.data_handler = DataHandler()
        self.data_handler.synchronize_research_attributes(
            self.research_attributes
        )
        self.trainer = Trainer()
        self.plotter = BinaryPlotter()

    def _create_compiled_model(self, units):
        """
        Create and compile a simple binary classification model.

        Parameters
        ----------
        units : int
            The number of units in the hidden dense layer.

        Returns
        -------
        tf.keras.Model
            The compiled Keras model.
        """
        model = tf.keras.models.Sequential(
            [
                tf.keras.layers.Input(shape=(28, 28, 3)),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(units, activation="relu"),
                tf.keras.layers.Dense(1, activation="sigmoid"),
            ]
        )
        model.compile(
            optimizer="adam",
            loss="binary_crossentropy",
            metrics=["accuracy"],
        )
        return model

    def _assert_datasets_container(self, module):
        """
        Assert that the module contains valid dataset containers.

        Parameters
        ----------
        module : object
            The module whose dataset container is validated.

        Raises
        ------
        AssertionError
            If the datasets container is missing or incorrect.
        """
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

    def _assert_outputs_container(self, module):
        """
        Assert that the module contains valid output containers.

        Parameters
        ----------
        module : object
            The module whose outputs container is validated.

        Raises
        ------
        AssertionError
            If the outputs container is missing or incorrect.
        """
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

    def test_workflow(self):
        """
        Test the complete binary classification research workflow.

        This method ensures that datasets are loaded, split, backed up,
        restored, and correctly processed through trials.
        """
        dataset = self.load_mnist_digits_dataset(
            sample_num=1000, labeled=True, binary=True
        )
        self.data_handler.load_dataset(dataset)
        self.data_handler.split_dataset(
            train_split=0.7, val_split=0.15, test_split=0.15
        )
        self._assert_datasets_container(self.data_handler)
        self.data_handler.prepare_datasets(
            ["train_dataset", "val_dataset", "test_dataset"],
            batch_size=32,
            shuffle_seed=42,
            prefetch_buffer_size=10,
            repeat_num=1,
        )
        self.data_handler.backup_datasets()
        self.data_handler.restore_datasets()
        self._assert_datasets_container(self.data_handler)

        trial_definitions = [
            {"name": "Trial 1", "hyperparameters": {"units": 128}},
            {"name": "Trial 2", "hyperparameters": {"units": 256}},
        ]

        with Experiment(
            self.data_handler,
            directory=self.results_dir,
            name="test_experiment",
            description="A test experiment",
        ) as experiment:
            self._assert_datasets_container(experiment)
            self.assertTrue(
                os.path.exists(experiment.experiment_assets["directory"]),
                "The experiment directory does not exist.",
            )

            self.plotter.synchronize_research_attributes(experiment)
            self.plotter.plot_images()
            experiment.synchronize_research_attributes(self.plotter)

            for i, trial_definition in enumerate(trial_definitions):
                with experiment.run_trial(**trial_definition) as trial:
                    self.assertTrue(
                        os.path.exists(trial.trial_assets["directory"]),
                        "The trial directory does not exist.",
                    )
                    self.trainer.synchronize_research_attributes(experiment)
                    self._assert_datasets_container(self.trainer)
                    model = self._create_compiled_model(
                        trial_definition["hyperparameters"]["units"]
                    )
                    self.trainer.set_compiled_model(model)
                    self.trainer.fit_predict_evaluate(epochs=10, batch_size=32)
                    self._assert_outputs_container(self.trainer)

                    has_evaluation_metrics = (
                        hasattr(self.trainer, "evaluation_metrics")
                        and self.trainer.evaluation_metrics is not None
                    )
                    self.assertTrue(
                        has_evaluation_metrics,
                        "The trainer does not have evaluation metrics.",
                    )

                    self.plotter.synchronize_research_attributes(self.trainer)
                    self._assert_outputs_container(self.plotter)

                    has_training_history = (
                        hasattr(self.trainer, "training_history")
                        and self.trainer.training_history is not None
                    )
                    self.assertTrue(
                        has_training_history,
                        "The trainer does not have a training history.",
                    )

                    self.plotter.plot_training_history(
                        title="Training History"
                    )
                    self.plotter.plot_confusion_matrix(
                        title="Confusion Matrix"
                    )
                    self.plotter.plot_roc_curve(title="ROC Curve")
                    self.plotter.plot_pr_curve(title="PR Curve")
                    self.plotter.plot_results(grid_size=(2, 2))
                    experiment.synchronize_research_attributes(self.plotter)

        self.assertEqual(
            len(experiment.experiment_assets["trials"]),
            i + 1,
            "The number of trials is incorrect.",
        )

        images_plot = os.path.join(
            experiment.experiment_assets["directory"], "images.png"
        )
        self.assertTrue(
            os.path.exists(images_plot),
            "The images plot does not exist.",
        )

        for trial in experiment.experiment_assets["trials"]:
            trial_directory = trial["directory"]
            figures_exist = all(
                os.path.exists(os.path.join(trial_directory, f"{fig}.png"))
                for fig in ["training_history", "confusion_matrix"]
            )
            self.assertTrue(
                figures_exist,
                f"Not all figures exist for the trial {trial['name']}.",
            )

            trial_info_exist = os.path.exists(
                os.path.join(trial_directory, "trial_info.json")
            )
            self.assertTrue(
                trial_info_exist,
                f"The trial info does not exist for the trial {trial['name']}.",
            )

        experiment_directory = experiment.experiment_assets["directory"]
        experiment_info_exist = os.path.exists(
            os.path.join(experiment_directory, "experiment_info.json")
        )
        self.assertTrue(
            experiment_info_exist,
            "The experiment info does not exist.",
        )

        experiment_report_files = [
            f
            for f in os.listdir(experiment_directory)
            if f.startswith("experiment_report.")
        ]
        self.assertEqual(
            len(experiment_report_files),
            1,
            "Expected 1 report file, but found "
            f"{len(experiment_report_files)}.",
        )


if __name__ == "__main__":
    unittest.main()
