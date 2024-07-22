import os
import unittest

import tensorflow as tf

from src.research.researchers import MultiClassResearcher
from src.testing.base.base_test_case import BaseTestCase
from src.testing.helpers.empty_directory import empty_directory


class TestMultiClassResearcherLevelWorkflow(BaseTestCase):
    """ Test case for the multi-class research workflow on high-level perspective
    using the Researcher class. """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        empty_directory(cls.results_dir)

    def setUp(self):
        super().setUp()
        self.researcher = MultiClassResearcher(
            class_names=["Digit " + str(i) for i in range(10)]
        )

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

    def _assert_datasets_container(self, datasets_container=None):
        if datasets_container is None:
            has_datasets_container = (
                hasattr(self.researcher, "datasets_container")
                and self.researcher.datasets_container is not None
            )
            self.assertTrue(
                has_datasets_container,
                "The researcher does not have a datasets container.",
            )
            datasets_container = self.researcher.datasets_container
        for dataset_name in ["train_dataset", "val_dataset", "test_dataset"]:
            self.assertIn(
                dataset_name,
                datasets_container,
                f"{dataset_name} is not in the datasets container.",
            )

    def _assert_outputs_container(self):
        has_outputs_container = (
            hasattr(self.researcher, "outputs_container")
            and self.researcher.outputs_container is not None
        )
        self.assertTrue(
            has_outputs_container,
            "The researcher does not have an outputs container.",
        )
        for output_name in ["train_output", "val_output", "test_output"]:
            self.assertIn(
                output_name,
                self.researcher.outputs_container,
                f"{output_name} is not in the outputs container.",
            )

    def test_workflow(self):
        # #### Dataset Handling ####
        dataset = self.load_mnist_digits_dataset(sample_num=1000, labeled=True)
        self.researcher.load_dataset(dataset)
        self.researcher.split_dataset(train_size=0.7, val_size=0.15, test_size=0.15)
        self._assert_datasets_container()
        self.researcher.enhance_datasets(
            ["train_dataset", "val_dataset", "test_dataset"],
            batch_size=32,
            shuffle_seed=42,
            prefetch_buffer_size=10,
            repeat_num=1,
        )
        self.researcher.backup_datasets()
        self.researcher.restore_datasets()
        self._assert_datasets_container()

        #### Experimenting ####
        trial_definitions = [
            {
                "name": "Trial 1",
                "hyperparameters": {"units": 128},
            },
            {
                "name": "Trial 2",
                "hyperparameters": {"units": 256},
            },
        ]

        with self.researcher.run_experiment(
            directory=self.results_dir,
            name="test_experiment",
            description="A test experiment",
        ) as experiment:
            self._assert_datasets_container(experiment.datasets_container)
            self.assertTrue(
                os.path.exists(experiment.experiment_data["directory"]),
                "The experiment directory does not exist.",
            )

            # Initial Visualization
            self.researcher.plot_images()
            for i, trial_definition in enumerate(trial_definitions):
                with experiment.run_trial(**trial_definition) as trial:
                    # ## Training ##
                    self.assertTrue(
                        os.path.exists(trial.trial_data["directory"]),
                        "The trial directory does not exist.",
                    )
                    model = self._create_compiled_model(
                        trial_definition["hyperparameters"]["units"]
                    )
                    self.researcher.set_compiled_model(model)
                    self.researcher.fit_predict_evaluate(
                        epochs=10, validation_steps=5
                    )
                    self._assert_outputs_container()
                    has_evaluation_metrics = (
                        hasattr(self.researcher, "evaluation_metrics")
                        and self.researcher.evaluation_metrics is not None
                    )
                    self.assertTrue(
                        has_evaluation_metrics,
                        "The researcher does not have evaluation metrics.",
                    )

                    # ## Plotting ##
                    has_training_history = (
                        hasattr(self.researcher, "training_history")
                        and self.researcher.training_history is not None
                    )
                    self.assertTrue(
                        has_training_history,
                        "The researcher does not have a training history.",
                    )
                    self.researcher.plot_training_history(title="Training History")
                    self.researcher.plot_confusion_matrix(title="Confusion Matrix")

        #### Assertions of experiment files existence ####
        self.assertEqual(
            len(experiment.experiment_data["trials"]),
            i + 1,
            "The number of trials is incorrect.",
        )
        images_plot = os.path.join(
            experiment.experiment_data["directory"], "images.png"
        )
        self.assertTrue(
            os.path.exists(images_plot),
            "The images plot does not exist.",
        )
        for trail in experiment.experiment_data["trials"]:
            trial_directory = trail["directory"]
            figures_exist = all(
                [
                    os.path.exists(os.path.join(trial_directory, figure_name + ".png"))
                    for figure_name in ["training_history", "confusion_matrix"]
                ]
            )
            self.assertTrue(
                figures_exist,
                f"Not all figures exist for the trial {trail['name']}.",
            )
            trial_info_exist = os.path.exists(
                os.path.join(trial_directory, "trial_info.json")
            )
            self.assertTrue(
                trial_info_exist,
                f"The trial info does not exist for the trial {trail['name']}.",
            )

        experiment_directory = experiment.experiment_data["directory"]
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
            f"Expected 1 report file, but found {len(experiment_report_files)}.",
        )


if __name__ == "__main__":
    unittest.main()
