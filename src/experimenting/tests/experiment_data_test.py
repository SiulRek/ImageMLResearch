import json
import os
import unittest

from src.experimenting.helpers.experiment_data import load_experiment_data
from src.testing.bases.base_test_case import BaseTestCase


class TestLoadExperimentData(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.experiment_dir = self.temp_dir
        self.experiment_info_path = os.path.join(
            self.experiment_dir, "experiment_info.json"
        )
        self.trial_name = "Trial 1"
        self.trial_dir = os.path.join(self.experiment_dir, "trial_1")
        self.trial_file = os.path.join(self.trial_dir, "trial_info.json")

        self.mock_experiment_data = {
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

        self.mock_trial_data = {
            "name": self.trial_name,
            "start_time": None,
            "duration": None,
            "directory": self.trial_dir,
            "hyperparameters": {},
            "figures": {},
            "evaluation_metrics": {},
            "training_history": {},
        }

    def create_experiment_info_file(self, data):
        with open(self.experiment_info_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def create_trial_info_file(self, data):
        os.makedirs(self.trial_dir, exist_ok=True)
        with open(self.trial_file, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def test_load_experiment_data_existing(self):
        self.create_experiment_info_file(self.mock_experiment_data)
        self.create_trial_info_file(self.mock_trial_data)

        experiment_data = load_experiment_data(self.experiment_dir)

        self.assertEqual(experiment_data["name"], self.mock_experiment_data["name"])
        self.assertEqual(
            experiment_data["description"], self.mock_experiment_data["description"]
        )
        self.assertEqual(len(experiment_data["trials"]), 1)
        self.assertEqual(experiment_data["trials"][0], self.mock_trial_data)

    def test_load_experiment_data_missing_trial_file(self):
        self.create_experiment_info_file(self.mock_experiment_data)

        with self.assertWarns(UserWarning):
            experiment_data = load_experiment_data(self.experiment_dir)

        self.assertEqual(experiment_data["name"], self.mock_experiment_data["name"])
        self.assertEqual(
            experiment_data["description"], self.mock_experiment_data["description"]
        )
        self.assertEqual(len(experiment_data["trials"]), 0)

    def test_load_experiment_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_experiment_data(self.experiment_dir)

    def test_assert_experiment_data_fail(self):
        mock_experiment_data = self.mock_experiment_data
        mock_experiment_data.pop("name")
        self.create_experiment_info_file(mock_experiment_data)
        self.create_trial_info_file(self.mock_trial_data)
        with self.assertRaises(ValueError):
            load_experiment_data(self.experiment_dir)

    def test_assert_trial_data_fail(self):
        self.create_experiment_info_file(self.mock_experiment_data)
        mock_trial_data = self.mock_trial_data
        mock_trial_data.pop("name")
        self.create_trial_info_file(mock_trial_data)
        with self.assertRaises(ValueError):
            load_experiment_data(self.experiment_dir)


if __name__ == "__main__":
    unittest.main()
