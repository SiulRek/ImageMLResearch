import json
import os
from time import sleep
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from src.experimenting.experiment import Experiment
import src.experimenting.experiment as experiment_module
from src.experimenting.helpers.trial import Trial
from src.research.attributes.research_attributes import ResearchAttributes
from src.testing.base.base_test_case import BaseTestCase


class TestExperiment(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.label_type = "multi_class"
        cls.class_names = ["cat", "dog"]
        cls.research_attributes = ResearchAttributes(
            label_type=cls.label_type, class_names=cls.class_names
        )

    @patch("src.experimenting.helpers.create_experiment_report")
    def setUp(self, mock_create_experiment_report):
        super().setUp()
        self.mock_create_experiment_report = mock_create_experiment_report

        self.directory = self.temp_dir
        self.name = "test_experiment"
        self.description = "This is a test experiment"

        self.call_test_experiment = lambda: Experiment(
            research_attributes=self.research_attributes,
            directory=self.directory,
            name=self.name,
            description=self.description,
        )

    def test_experiment_initialization(self):
        # Check experiment data initialization
        with self.call_test_experiment() as experiment:
            self.assertIsInstance(experiment, Experiment)
            self.assertEqual(experiment.experiment_data["name"], self.name)
            self.assertEqual(
                experiment.experiment_data["description"], self.description
            )
            self.assertTrue(os.path.exists(experiment.experiment_data["directory"]))

    def test_experiment_data_written_to_json(self):
        with self.call_test_experiment() as experiment:
            pass
        experiment_info_json = os.path.join(
            experiment.experiment_data["directory"],
            "experiment_info.json",
        )
        self.assertTrue(os.path.exists(experiment_info_json))

        with open(experiment_info_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data["name"], self.name)
        self.assertEqual(data["description"], self.description)
        self.assertTrue("start_time" in data)
        self.assertTrue("duration" in data)
        self.assertTrue("trials" in data)

    def test_create_experiment_report_called(self):
        with patch.object(
            experiment_module, "create_experiment_report", MagicMock()
        ) as mock_create_experiment_report:
            with self.call_test_experiment() as experiment:
                pass
            mock_create_experiment_report.assert_called_once_with(
                experiment.experiment_data
            )

    def test_experiment_exit_with_exception(self):
        def raise_error_with_traceback():
            try:
                raise ValueError()
            except ValueError as e:
                raise ValueError() from e

        experiment_exception_raised = False
        try:
            with self.call_test_experiment():
                raise_error_with_traceback()
        except ValueError as e:
            experiment_exception_raised = True
            self.assertTrue(e.__traceback__)
        self.assertTrue(experiment_exception_raised)

    def _run_trials_and_verify(self, trial_definitions, sleep_time=None):
        with self.call_test_experiment() as experiment:
            for i, (name, trial_description, hyperparameters) in enumerate(
                trial_definitions
            ):
                with experiment.run_trial(
                    name, trial_description, hyperparameters
                ) as trial:
                    self.assertIsInstance(trial, Trial)
                    self.assertEqual(trial.trial_data["name"], name)
                    self.assertEqual(trial.trial_data["description"], trial_description)
                    self.assertEqual(
                        trial.trial_data["hyperparameters"], hyperparameters
                    )
                    self.assertTrue("start_time" in trial.trial_data)
                    # Simulate accuracy
                    accuracy = float(1 - i * 0.1)
                    metrics_set = {"test": {"accuracy": accuracy}}
                    experiment._evaluation_metrics.update(metrics_set)

            self.assertIn(trial.trial_data, experiment.experiment_data["trials"])

            if sleep_time is not None:
                sleep(sleep_time)

        return experiment

    def test_trials_creation(self):

        def get_accuracy(trial_num):
            trial = experiment.experiment_data["trials"][trial_num]
            metrics_set = trial["evaluation_metrics"]["test"]
            return metrics_set["accuracy"]

        trial_definitions = [
            ("trial1", "This is trial 1", {"lr": 0.01, "batch_size": 16}),
            ("trial2", "This is trial 2", {"lr": 0.001, "batch_size": 32}),
        ]
        experiment = self._run_trials_and_verify(trial_definitions)

        self.assertEqual(len(experiment.experiment_data["trials"]), 2)

        # Assert if trials are sorted by accuracy
        self.assertEqual(get_accuracy(trial_num=0), 1)
        self.assertEqual(get_accuracy(trial_num=1), 0.9)

    def test_load_experiment_data(self):
        trial_definitions = [
            ("trial1", "This is trial 1", {"lr": 0.01, "batch_size": 16}),
            ("trial2", "This is trial 2", {"lr": 0.001, "batch_size": 32}),
        ]

        experiment = self._run_trials_and_verify(trial_definitions)
        reloaded_experiment = Experiment(
            research_attributes=self.research_attributes,
            directory=self.directory,
            name=self.name,
            description=self.description,
        )
        # Check if the trials are loaded correctly
        trials_data = experiment.experiment_data["trials"]
        # No reloading supported currently for training_history
        for trials in trials_data:
            trials.pop("training_history", None)
        reloaded_trials_data = reloaded_experiment.experiment_data["trials"]

        self.assertEqual(trials_data, reloaded_trials_data)

    def test_resume_experiment(self):
        def get_experiment_duration(experiment):
            duration = experiment.experiment_data["duration"]
            duration = float(duration.replace(":", ""))
            return duration

        trial_definitions = [
            ("trial1", "This is trial 1", {"lr": 0.01, "batch_size": 16}),
            ("trial2", "This is trial 2", {"lr": 0.001, "batch_size": 32}),
        ]
        initial_experiment = self._run_trials_and_verify(
            trial_definitions, sleep_time=0.01
        )
        initial_duration = get_experiment_duration(initial_experiment)

        del initial_experiment

        new_trial_definitions = [
            ("trial3", "This is trial 3", {"lr": 0.001, "batch_size": 32}),
            ("trial4", "This is trial 4", {"lr": 0.001, "batch_size": 32}),
        ]
        resumed_experiment = self._run_trials_and_verify(
            new_trial_definitions, sleep_time=0.01
        )
        total_duration = get_experiment_duration(resumed_experiment)

        self.assertEqual(len(resumed_experiment.experiment_data["trials"]), 4)
        self.assertGreater(total_duration, initial_duration)


if __name__ == "__main__":
    unittest.main()
