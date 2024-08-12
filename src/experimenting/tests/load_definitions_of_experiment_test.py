import json
import os
import unittest

from src.experimenting.helpers.load_definitions_of_experiment import (
    load_definitions_of_experiment,
)
from src.testing.bases.base_test_case import BaseTestCase


class TestLoadDefinitionsOfExperiment(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.experiment_definitions = {
            "name": "Test Experiment",
            "description": "This is a test experiment.",
            "directory": "test_experiment",
        }
        self.definitions_json_path = os.path.join(self.temp_dir, "definitions.json")

    def _write_definitions_to_file(self, definitions_content):
        with open(self.definitions_json_path, "w", encoding="utf-8") as f:
            json.dump(definitions_content, f)

    def test_load_definitions_of_experiment_1(self):
        definitions_content = {
            "experiment_definitions": self.experiment_definitions,
            "trials_definitions": [{"name": "trial_1", "hyperparameters": {}}],
        }
        self._write_definitions_to_file(definitions_content)
        experiment_definitions, trials_definitions = load_definitions_of_experiment(
            self.definitions_json_path
        )
        self.assertEqual(
            experiment_definitions, definitions_content["experiment_definitions"]
        )
        trial_def = next(trials_definitions)
        self.assertEqual(trial_def["name"], "trial_1")
        self.assertEqual(trial_def["hyperparameters"], {})

    def test_load_definitions_of_experiment_2(self):
        definitions_content = {
            "experiment_definitions": self.experiment_definitions,
            "trials_definitions": {
                "num_trials": 2,
                "prefix": "trial_",
                "hparams_configs": {"param": {"low": 1, "high": 10, "type": "int"}},
            },
        }
        self._write_definitions_to_file(definitions_content)
        experiment_definitions, trials_definitions = load_definitions_of_experiment(
            self.definitions_json_path
        )
        self.assertEqual(
            experiment_definitions, definitions_content["experiment_definitions"]
        )
        for i, trial_def in enumerate(trials_definitions):
            self.assertEqual(trial_def["name"], "trial_" + str(i + 1))
            self.assertIn("param", trial_def["hyperparameters"])
            # NOTE: In real use case do not set the last score manually, it is
            # just done here to isolate the functionality under test.
            trials_definitions.suggester.set_last_score(1)
        with self.assertRaises(StopIteration):
            next(trials_definitions)

    def test_load_definitions_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_definitions_of_experiment(self.definitions_json_path)

    def _test_invalid_content(self, invalid_content=None):
        invalid_content = {
            "trials_definitions": [{"name": "trial_1", "hyperparameters": {}}]
        }
        self._write_definitions_to_file(invalid_content)
        with self.assertRaises(AssertionError):
            load_definitions_of_experiment(self.definitions_json_path)

    def test_invalid_contents(self):
        invalid_contents = [
            {"trials_definitions": [{"name": "trial_1", "hyperparameters": {}}]},
            {"experiment_definitions": self.experiment_definitions},
            {
                "experiment_definitions": self.experiment_definitions,
                "trials_definitions": [{"name": "trial_1"}],
            },
            {
                "experiment_definitions": self.experiment_definitions,
                "trials_definitions": {},
            },
        ]
        for invalid_content in invalid_contents:
            self._test_invalid_content(invalid_content)

    def test_unused_key_in_trials_definitions(self):
        unused_key = {
            "experiment_definitions": self.experiment_definitions,
            "trials_definitions": {"hparams_configs": {}, "unused_key": 1},
        }
        self._write_definitions_to_file(unused_key)
        with self.assertWarns(UserWarning):
            load_definitions_of_experiment(self.definitions_json_path)


if __name__ == "__main__":
    unittest.main()
