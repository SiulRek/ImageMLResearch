import json
import os
import unittest

from imlresearch.src.experimenting.helpers.experiment_assets import (
    load_experiment_assets,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestLoadExperimentAssets(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.experiment_dir = self.temp_dir
        self.experiment_info_path = os.path.join(
            self.experiment_dir, "experiment_info.json"
        )
        self.trial_name = "Trial 1"
        self.trial_dir = os.path.join(self.experiment_dir, "trial_1")
        self.trial_file = os.path.join(self.trial_dir, "trial_info.json")

        self.mock_experiment_assets = {
            "name": "test_experiment",
            "description": "test_description",
            "start_time": None,
            "resume_time": None,
            "duration": None,
            "directory": self.experiment_dir,
            "figures": {},
            "trials": [self.trial_name],
            "sort_metric": "accuracy",
        }

        self.mock_trial_assets = {
            "name": self.trial_name,
            "start_time": None,
            "duration": None,
            "directory": self.trial_dir,
            "hyperparameters": {},
            "figures": {},
            "evaluation_metrics": {},
            "training_history": {},
        }

    def create_experiment_info_file(self, assets):
        with open(self.experiment_info_path, "w", encoding="utf-8") as f:
            json.dump(assets, f)

    def create_trial_info_file(self, assets):
        os.makedirs(self.trial_dir, exist_ok=True)
        with open(self.trial_file, "w", encoding="utf-8") as f:
            json.dump(assets, f)

    def test_load_experiment_assets_tracked_trial(self):
        self.create_experiment_info_file(self.mock_experiment_assets)
        self.create_trial_info_file(self.mock_trial_assets)

        experiment_assets = load_experiment_assets(self.experiment_dir)

        self.assertEqual(
            experiment_assets["name"],
            self.mock_experiment_assets["name"],
        )
        self.assertEqual(
            experiment_assets["description"],
            self.mock_experiment_assets["description"],
        )
        self.assertEqual(len(experiment_assets["trials"]), 1)
        self.assertEqual(
            experiment_assets["trials"][0], self.mock_trial_assets
        )

    def test_load_experiment_assets_untracked_trial(self):
        mock_experiment_assets = self.mock_experiment_assets
        mock_experiment_assets["trials"] = []
        self.create_experiment_info_file(mock_experiment_assets)
        self.create_trial_info_file(self.mock_trial_assets)

        experiment_assets = load_experiment_assets(self.experiment_dir)

        self.assertEqual(
            experiment_assets["name"],
            self.mock_experiment_assets["name"],
        )
        self.assertEqual(
            experiment_assets["description"],
            self.mock_experiment_assets["description"],
        )
        self.assertEqual(len(experiment_assets["trials"]), 1)
        self.assertEqual(
            experiment_assets["trials"][0], self.mock_trial_assets
        )

    def test_load_experiment_assets_ignore_untracked_folder(self):
        mock_experiment_assets = self.mock_experiment_assets
        mock_experiment_assets["trials"] = []
        self.create_experiment_info_file(mock_experiment_assets)
        untracked_dir = os.path.join(self.experiment_dir, "untracked_trial")
        os.makedirs(untracked_dir, exist_ok=True)

        experiment_assets = load_experiment_assets(self.experiment_dir)
        self.assertEqual(len(experiment_assets["trials"]), 0)

    def test_load_experiment_assets_missing_trial_file(self):
        self.create_experiment_info_file(self.mock_experiment_assets)

        with self.assertWarns(UserWarning):
            experiment_assets = load_experiment_assets(self.experiment_dir)

        self.assertEqual(
            experiment_assets["name"],
            self.mock_experiment_assets["name"],
        )
        self.assertEqual(
            experiment_assets["description"],
            self.mock_experiment_assets["description"],
        )
        self.assertEqual(len(experiment_assets["trials"]), 0)

    def test_load_experiment_assets_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_experiment_assets(self.experiment_dir)

    def test_assert_experiment_assets_fail(self):
        mock_experiment_assets = self.mock_experiment_assets
        mock_experiment_assets.pop("name")
        self.create_experiment_info_file(mock_experiment_assets)
        self.create_trial_info_file(self.mock_trial_assets)

        with self.assertRaises(ValueError):
            load_experiment_assets(self.experiment_dir)

    def test_assert_trial_assets_fail(self):
        self.create_experiment_info_file(self.mock_experiment_assets)
        mock_trial_assets = self.mock_trial_assets
        mock_trial_assets.pop("name")
        self.create_trial_info_file(mock_trial_assets)

        with self.assertRaises(ValueError):
            load_experiment_assets(self.experiment_dir)


if __name__ == "__main__":
    unittest.main()
