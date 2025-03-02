import json
import os
import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt

from imlresearch.src.experimenting.helpers.last_score_singleton import (
    LastScoreSingleton,
)
from imlresearch.src.experimenting.helpers.trial import Trial
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestTrial(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.mock_experiment = MagicMock()
        self.mock_experiment.experiment_assets = {
            "directory": self.temp_dir,
            "trials": [],
        }
        self.mock_experiment.get_results.return_value = {
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
        trial_info_json = os.path.join(
            trial.trial_assets["directory"], "trial_info.json"
        )
        with open(trial_info_json, "r", encoding="utf-8") as f:
            assets = json.load(f)
        return assets

    def test_trial_initialization(self):
        with self.call_test_trial() as trial:
            self.assertIsInstance(trial, Trial)
            self.assertEqual(trial.trial_assets["name"], self.name)
            self.assertEqual(
                trial.trial_assets["hyperparameters"], self.hyperparameters
            )
            self.assertTrue(os.path.exists(trial.trial_assets["directory"]))
            self.assertIsInstance(trial.trial_assets["start_time"], str)
            self.assertIsNone(trial.trial_assets["duration"])
            self.assertIsNone(trial.trial_assets["figures"])
            self.assertIsNone(trial.trial_assets["evaluation_metrics"])
            self.assertIsNone(trial.trial_assets["training_history"])
        self.assertIsInstance(trial.trial_assets["duration"], str)

    def test_trial_info_written_to_json(self):
        with self.call_test_trial() as trial:
            pass
        trial_info_json = os.path.join(
            trial.trial_assets["directory"], "trial_info.json"
        )
        self.assertTrue(os.path.exists(trial_info_json))

        assets = self._read_trial_info(trial)

        self.assertEqual(assets["name"], self.name)
        self.assertEqual(assets["hyperparameters"], self.hyperparameters)
        self.assertIn("start_time", assets)
        self.assertIn("duration", assets)
        self.assertIn("figures", assets)
        self.assertIn("evaluation_metrics", assets)
        self.assertIn("training_history", assets)

    def test_add_trial_to_experiment_assets(self):
        with self.call_test_trial() as trial:
            pass
        trials = self.mock_experiment.experiment_assets["trials"]
        self.assertEqual(len(trials), 1)
        self.assertEqual(trials[0], trial.trial_assets)

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
                "training_history": training_history,
            }
            trial_assets = trial.trial_assets

        for name, path in trial_assets["figures"].items():
            self.assertTrue(os.path.exists(path), f"Figure {name} not saved.")

        self.assertEqual(
            trial_assets["evaluation_metrics"],
            evaluation_metrics,
        )
        read_assets = self._read_trial_info(trial)
        self.assertEqual(read_assets, trial_assets)

    def test_set_last_score(self):
        return_value = {
            "figures": {},
            "evaluation_metrics": {},
            "training_history": {},
        }

        # val_loss is present in training history.
        with self.call_test_trial():
            return_value["training_history"] = {
                "loss": [0.1, 0.2, 0.3],
                "val_loss": [0.2, 0.3, 0.4],
            }
            self.mock_experiment.get_results.return_value = return_value
        last_score = LastScoreSingleton().take()
        self.assertEqual(last_score, 0.4)

        # val_loss is not present in training history.
        with self.call_test_trial():
            return_value["training_history"] = {"loss": [0.1, 0.2, 0.3]}
            self.mock_experiment.get_results.return_value = return_value
        last_score = LastScoreSingleton().take()
        self.assertEqual(last_score, 0.3)

        # Non empty results but training_history is empty ...
        LastScoreSingleton().clear()
        with self.call_test_trial():
            return_value["evaluation_metrics"] = {"accuracy": 0.9}
            return_value["training_history"] = {}
            self.mock_experiment.get_results.return_value = return_value
        # ... should raise an exception as no score was set.
        with self.assertRaises(ValueError):
            LastScoreSingleton().take()

        # Empty results sets last score to None.
        LastScoreSingleton().clear()
        with self.call_test_trial():
            return_value["evaluation_metrics"] = {}
            return_value["training_history"] = {}
            self.mock_experiment.get_results.return_value = return_value
        self.assertIsNone(LastScoreSingleton().take())

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
        trials = self.mock_experiment.experiment_assets["trials"]
        self.assertEqual(len(trials), 0)

    def test_trial_already_runned(self):
        with self.call_test_trial() as trial:
            self.assertFalse(trial.already_runned)

        with self.call_test_trial() as trial:
            self.assertTrue(trial.already_runned)

    def test_non_serializable_hyperparameters(self):
        non_serializable_params = {"lr": MagicMock(), "model": MagicMock()}
        with Trial(
            experiment=self.mock_experiment,
            name="non_serializable_trial",
            hyperparameters=non_serializable_params,
        ) as trial:
            pass

        assets = self._read_trial_info(trial)
        self.assertIsNone(assets["hyperparameters"])


if __name__ == "__main__":
    unittest.main()
