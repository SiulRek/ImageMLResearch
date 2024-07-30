import json
import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt

from src.experimenting.helpers.trial import Trial, ResultsEmptyError
from src.testing.bases.base_test_case import BaseTestCase


class TestTrial(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.mock_experiment = MagicMock()
        self.mock_experiment.experiment_data = {
            "directory": self.temp_dir,
            "trials": [],
        }
        self.mock_experiment.get_results.return_value = {
            # Experiment requires at least one value in dict
            # to be not empty for the trial to be saved.
            "figures": {},
            "evaluation_metrics": {},
            "training_history": {"loss": [0.1, 0.2, 0.3]},
        }

        self.name = "test_trial"
        self.description = "A test trial"
        self.hyperparameters = {"lr": 0.001, "batch_size": 32}
        self.call_test_trial = lambda: Trial(
            experiment=self.mock_experiment,
            name=self.name,
            hyperparameters=self.hyperparameters,
        )

    def _read_trial_info(self, trial):
        trial_info_json = os.path.join(trial.trial_data["directory"], "trial_info.json")
        with open(trial_info_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def test_trial_initialization(self):
        with self.call_test_trial() as trial:
            self.assertIsInstance(trial, Trial)
            self.assertEqual(trial.trial_data["name"], self.name)
            self.assertEqual(trial.trial_data["hyperparameters"], self.hyperparameters)
            self.assertTrue(os.path.exists(trial.trial_data["directory"]))
            self.assertIsInstance(trial.trial_data["start_time"], str)
            self.assertIsNone(trial.trial_data["duration"])
            self.assertIsNone(trial.trial_data["figures"])
            self.assertIsNone(trial.trial_data["evaluation_metrics"])
            self.assertIsNone(trial.trial_data["training_history"])
        self.assertIsInstance(trial.trial_data["duration"], str)

    def test_trial_info_written_to_json(self):
        with self.call_test_trial() as trial:
            pass
        trial_info_json = os.path.join(trial.trial_data["directory"], "trial_info.json")
        self.assertTrue(os.path.exists(trial_info_json))

        data = self._read_trial_info(trial)

        self.assertEqual(data["name"], self.name)
        self.assertEqual(data["hyperparameters"], self.hyperparameters)
        self.assertTrue("start_time" in data)
        self.assertTrue("duration" in data)
        self.assertTrue("figures" in data)
        self.assertTrue("evaluation_metrics" in data)
        self.assertTrue("training_history" in data)

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
            evaluation_metrics = {"accuracy": 0.9, "f1_score": 0.8}
            training_history = {"loss": [0.1, 0.2, 0.3]}
            self.mock_experiment.get_results.return_value = {
                "figures": figures,
                "evaluation_metrics": evaluation_metrics,
                "training_history": {"loss": training_history},
            }  # Simulates the generation of trial results.
            trial_data = trial.trial_data

        for name, path in trial_data["figures"].items():
            self.assertTrue(os.path.exists(path), f"Figure {name} not saved.")

        self.assertEqual(
            trial_data["evaluation_metrics"],
            evaluation_metrics,
        )
        read_data = self._read_trial_info(trial)
        self.assertEqual(read_data, trial_data)

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
        except ValueError as e:
            trial_exception_raised = True
            self.assertTrue(e.__traceback__)
        self.assertTrue(trial_exception_raised)
        self.assertEqual(len(self.mock_experiment.experiment_data["trials"]), 0)

    def test_trial_already_runned(self):
        with self.call_test_trial() as trial:
            self.assertFalse(trial.already_runned)
            pass

        with self.call_test_trial() as trial:
            self.assertTrue(trial.already_runned)

    def test_trial_execution_in_four_cases(self):
        def get_trials():
            return self.mock_experiment.experiment_data["trials"]

        empty_results = {
            "figures": {},
            "evaluation_metrics": {},
            "training_history": {},
        }
        non_empty_results = {
            "figures": {},
            "evaluation_metrics": {},
            "training_history": {"loss": [0.1, 0.2, 0.3]},
        }

        # Case 1: Trial never runned, actual results are empty.
        # Trial is not saved therefore we consider it as never runned.
        self.mock_experiment.get_results.return_value = empty_results
        with self.assertWarns(UserWarning):
            with self.call_test_trial():
                pass
        self.assertEqual(len(get_trials()), 0)

        # Case 2: Trial never runned, actual results are not empty.
        # Normal case.
        self.mock_experiment.get_results.return_value = non_empty_results
        with self.call_test_trial():
            pass
        self.assertEqual(len(get_trials()), 1)
        prev_trial_data = get_trials()[0]

        # Case 3: Trial already runned, actual results are empty.
        # Nothing new is saved.
        self.mock_experiment.get_results.return_value = empty_results
        with self.call_test_trial():
            pass
        self.assertEqual(len(get_trials()), 1)
        new_trial_data = get_trials()[0]
        # Trial data should be the same as the previous trial, as
        # the results are empty and therefore the old trial 
        # data should be kept.
        self.assertEqual(prev_trial_data, new_trial_data)

        # Case 4: Trial already runned, actual results are not empty.
        # Old results are overwritten.
        self.mock_experiment.get_results.return_value = non_empty_results
        with self.assertWarns(UserWarning):
            with self.call_test_trial():
                pass

    def test_non_serializable_hyperparameters(self):
        non_serializable_params = {"lr": MagicMock(), "model": MagicMock()}
        with Trial(
            experiment=self.mock_experiment,
            name="non_serializable_trial",
            hyperparameters=non_serializable_params,
        ) as trial:
            pass

        data = self._read_trial_info(trial)
        self.assertIsNone(data["hyperparameters"])


if __name__ == "__main__":
    unittest.main()
