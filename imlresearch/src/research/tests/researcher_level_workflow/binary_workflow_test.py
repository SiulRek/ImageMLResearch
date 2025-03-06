import os
import unittest

import tensorflow as tf

import imlresearch.src.preprocessing.steps as steps
from imlresearch.src.research.researchers import BinaryResearcher
from imlresearch.src.testing.bases.base_test_case import BaseTestCase
from imlresearch.src.testing.helpers.empty_directory import empty_directory


class TestBinaryResearcherLevelWorkflow(BaseTestCase):
    """
    Test case for the binary classification research workflow from a
    high-level perspective using the Researcher class.
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

        This initializes the BinaryResearcher instance.
        """
        super().setUp()
        self.researcher = BinaryResearcher(class_names=["Digit 0", "Digit 1"])

    def _create_compiled_model(self, units):
        """
        Create and compile a binary classification model.

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

    def _assert_datasets_container(self, datasets_container=None, batched=True):
        """
        Assert that the researcher contains valid dataset containers.

        Parameters
        ----------
        datasets_container : dict, optional
            The datasets container to validate. If None, the researcher's
            datasets container is used.
        batched : bool, optional
            Whether the dataset is expected to be batched, by default True.
        """
        if datasets_container is None:
            has_datasets_container = (
                hasattr(self.researcher, "datasets_container")
                and self.researcher.datasets_container is not None
            )
            self.assertTrue(has_datasets_container)
            datasets_container = self.researcher.datasets_container

        for dataset_name in ["train_dataset", "val_dataset", "test_dataset"]:
            self.assertIn(dataset_name, datasets_container)
            dataset = datasets_container[dataset_name]
            for img, label in dataset.take(1):
                expected_img_shape = (32, 28, 28, 3) if batched else (28, 28, 3)
                self.assertEqual(img.shape, expected_img_shape)
                expected_label_shape = (32,) if batched else tf.TensorShape([])
                self.assertEqual(label.shape, expected_label_shape)

    def _make_preprocessing_pipeline(self):
        """
        Create a preprocessing pipeline.

        Returns
        -------
        list
            A list of preprocessing steps.
        """
        pipeline = [
            steps.ReverseScaler(255),
            steps.TypeCaster(output_dtype="float32"),
        ]
        return pipeline

    def _assert_outputs_container(self):
        """
        Assert that the researcher contains a valid outputs container.
        """
        has_outputs_container = (
            hasattr(self.researcher, "outputs_container")
            and self.researcher.outputs_container is not None
        )
        self.assertTrue(has_outputs_container)

        for output_name in ["train_output", "val_output", "test_output"]:
            self.assertIn(output_name, self.researcher.outputs_container)

    def test_workflow(self):
        """
        Test the complete binary classification research workflow.

        This method ensures that datasets are loaded, split, backed up,
        restored, preprocessed, and correctly processed through trials.
        """
        dataset = self.load_mnist_digits_dataset(
            sample_num=1000, labeled=True, binary=True
        )
        self.researcher.load_dataset(dataset)
        self.researcher.split_dataset(
            train_split=0.7, val_split=0.15, test_split=0.15
        )
        self._assert_datasets_container(batched=False)
        self.researcher.backup_datasets()
        self.researcher.restore_datasets()
        self._assert_datasets_container(batched=False)
        preprocessing_pipe = self._make_preprocessing_pipeline()
        self.researcher.apply_preprocessing_pipeline(preprocessing_pipe)
        self._assert_datasets_container(batched=False)
        self.researcher.prepare_datasets(
            ["train_dataset", "val_dataset", "test_dataset"],
            batch_size=32,
            shuffle_seed=42,
            prefetch_buffer_size=12,
            repeat_num=1,
        )
        self._assert_datasets_container()

        trial_definitions = [
            {"name": "Trial 1", "hyperparameters": {"units": 128}},
            {"name": "Trial 2", "hyperparameters": {"units": 256}},
        ]

        with self.researcher.run_experiment(
            directory=self.results_dir,
            name="test_experiment",
            description="A test experiment",
        ) as experiment:
            self._assert_datasets_container(experiment.datasets_container)
            self.assertTrue(
                os.path.exists(experiment.experiment_assets["directory"])
            )

            self.researcher.plot_images()
            for i, trial_definition in enumerate(trial_definitions):
                with experiment.run_trial(**trial_definition) as trial:
                    self.assertTrue(
                        os.path.exists(trial.trial_assets["directory"])
                    )
                    model = self._create_compiled_model(
                        trial_definition["hyperparameters"]["units"]
                    )
                    self.researcher.set_compiled_model(model)
                    self.researcher.fit_predict_evaluate(
                        epochs=10, batch_size=32
                    )
                    self._assert_outputs_container()
                    has_evaluation_metrics = (
                        hasattr(self.researcher, "evaluation_metrics")
                        and self.researcher.evaluation_metrics is not None
                    )
                    self.assertTrue(has_evaluation_metrics)

                    has_training_history = (
                        hasattr(self.researcher, "training_history")
                        and self.researcher.training_history is not None
                    )
                    self.assertTrue(has_training_history)
                    self.researcher.plot_training_history(
                        title="Training History"
                    )
                    self.researcher.plot_confusion_matrix(
                        title="Confusion Matrix"
                    )
                    self.researcher.plot_roc_curve(title="ROC Curve")
                    self.researcher.plot_pr_curve(title="PR Curve")
                    self.researcher.plot_results(grid_size=(2, 2))

        self.assertEqual(len(experiment.experiment_assets["trials"]), i + 1)
        images_plot = os.path.join(
            experiment.experiment_assets["directory"], "images.png"
        )
        self.assertTrue(os.path.exists(images_plot))

        for trial in experiment.experiment_assets["trials"]:
            trial_directory = trial["directory"]
            figures_exist = all(
                os.path.exists(os.path.join(trial_directory, f"{fig}.png"))
                for fig in ["training_history", "confusion_matrix"]
            )
            self.assertTrue(figures_exist)
            trial_info_exist = os.path.exists(
                os.path.join(trial_directory, "trial_info.json")
            )
            self.assertTrue(trial_info_exist)

        experiment_directory = experiment.experiment_assets["directory"]
        experiment_info_exist = os.path.exists(
            os.path.join(experiment_directory, "experiment_info.json")
        )
        self.assertTrue(experiment_info_exist)

        experiment_report_files = [
            f
            for f in os.listdir(experiment_directory)
            if f.startswith("experiment_report.")
        ]
        self.assertEqual(len(experiment_report_files), 1)


if __name__ == "__main__":
    unittest.main()
