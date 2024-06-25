import json
import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt

from src.experimenting.helpers.trial import Trial, TrialError
from src.testing.base.base_test_case import BaseTestCase


class TestTrial(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.mock_experiment = MagicMock()
        self.mock_experiment.experiment_data = {
            "directory": self.temp_dir,
            "trials": [],
        }
        self.mock_experiment.figures = {}
        self.mock_experiment.evaluation_metrics = {}

        self.trial_name = "test_trial"
        self.description = "A test trial"
        self.hyperparameters = {"lr": 0.001, "batch_size": 32}
        self.call_test_trial = lambda: Trial(
            experiment=self.mock_experiment,
            trial_name=self.trial_name,
            description=self.description,
            hyperparameters=self.hyperparameters,
        )

    def test_trial_initialization(self):
        with self.call_test_trial() as trial:
            self.assertIsInstance(trial, Trial)
            self.assertEqual(trial.trial_data["trial_name"], self.trial_name)
            self.assertEqual(trial.trial_data["description"], self.description)
            self.assertEqual(trial.trial_data["hyperparameters"], self.hyperparameters)
            self.assertTrue(os.path.exists(trial.trial_data["directory"]))

    def test_trial_info_written_to_json(self):
        with self.call_test_trial() as trial:
            trial_info_json = os.path.join(
                trial.trial_data["directory"], "trial_info.json"
            )
            self.assertTrue(os.path.exists(trial_info_json))

        with open(trial_info_json, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data["trial_name"], self.trial_name)
        self.assertEqual(data["description"], self.description)
        self.assertEqual(data["hyperparameters"], self.hyperparameters)
        self.assertTrue("start_time" in data)

    def test_add_trial_to_experiment_data(self):
        with self.call_test_trial() as trial:
            pass
        self.assertEqual(len(self.mock_experiment.experiment_data["trials"]), 1)
        self.assertEqual(
            self.mock_experiment.experiment_data["trials"][0], trial.trial_data
        )

    def test_trial_with_outputs(self):
        with self.call_test_trial() as trial:
            figures = {
                "history": plt.figure(),
                "confusion_matrix": plt.figure(),
            }
            self.mock_experiment.figures = figures
            evaluation_metrics = {"accuracy": 0.9, "f1_score": 0.8}
            self.mock_experiment.evaluation_metrics = evaluation_metrics
            trial_data = trial.trial_data

        for name, path in trial_data["figures"].items():
            self.assertTrue(os.path.exists(path), f"Figure {name} not saved.")

        self.assertEqual(
            trial_data["evaluation_metrics"],
            self.mock_experiment.evaluation_metrics,
        )
        trial_info_json = os.path.join(trial_data["directory"], "trial_info.json")
        with open(trial_info_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, trial_data)

    def test_trial_exit_with_exception(self):

        def raise_error_with_traceback():
            try:
                raise ValueError()
            except ValueError as e:
                raise ValueError() from e

        trial_exception_raised = False
        try:
            with self.call_test_trial():
                raise_error_with_traceback()
        except TrialError as e:
            trial_exception_raised = True
            exception_msg = "An error occurred during the trial."
            self.assertTrue(exception_msg in str(e))
            self.assertTrue(e.__traceback__)
        self.assertTrue(trial_exception_raised)
        self.assertEqual(len(self.mock_experiment.experiment_data["trials"]), 0)

    def test_non_serializable_hyperparameters(self):
        non_serializable_params = {"lr": MagicMock(), "model": MagicMock()}
        trial_with_non_serializable_params = Trial(
            experiment=self.mock_experiment,
            trial_name="non_serializable_trial",
            description="Trial with non-serializable hyperparameters",
            hyperparameters=non_serializable_params,
        )

        self.assertIsNone(
            trial_with_non_serializable_params.trial_data["hyperparameters"]
        )


if __name__ == "__main__":
    unittest.main()
