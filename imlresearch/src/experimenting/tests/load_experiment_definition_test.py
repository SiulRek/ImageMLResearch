import json
import os
import unittest

from imlresearch.src.experimenting.helpers.load_experiment_definition import (
    load_experiment_definition,
)
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TestLoadExperimentDefinition(BaseTestCase):
    """
    Unit tests for the load_experiment_definition function.
    """

    def setUp(self):
        """
        Sets up the test environment before each test case.
        """
        super().setUp()
        experiment_dir = os.path.join(self.temp_dir, "test_experiment")
        self.experiment_metadata = {
            "name": "Test Experiment",
            "description": "This is a test experiment.",
            "directory": experiment_dir,
        }
        self.definitions_json_path = os.path.join(
            self.temp_dir, "definition.json"
        )

    def _write_definitions_to_file(self, definitions_content):
        """
        Writes the provided experiment definitions to a JSON file.

        Parameters
        ----------
        definitions_content : dict
            The content to be written into the definitions file.
        """
        with open(self.definitions_json_path, "w", encoding="utf-8") as f:
            json.dump(definitions_content, f)

    def test_load_definitions_of_experiment_manual(self):
        """
        Tests loading manually defined experiment metadata and trials.
        """
        definitions_content = {
            "experiment_metadata": self.experiment_metadata,
            "trial_definitions": [{"name": "trial_1", "hyperparameters": {}}],
        }
        self._write_definitions_to_file(definitions_content)
        experiment_metadata, trial_definitions = load_experiment_definition(
            self.definitions_json_path
        )
        self.assertEqual(
            experiment_metadata, definitions_content["experiment_metadata"]
        )
        trial_def = next(trial_definitions)
        self.assertEqual(trial_def["name"], "trial_1")
        self.assertEqual(trial_def["hyperparameters"], {})

    def test_load_definitions_of_experiment_automatic(self):
        """
        Tests loading automatically generated trial definitions.
        """
        definitions_content = {
            "experiment_metadata": self.experiment_metadata,
            "trial_definitions": {
                "num_trials": 2,
                "prefix": "trial_",
                "hparams_configs": {
                    "param": {"low": 1, "high": 10, "type": "int"}
                },
            },
        }
        self._write_definitions_to_file(definitions_content)
        experiment_metadata, trial_definitions = load_experiment_definition(
            self.definitions_json_path
        )
        self.assertEqual(
            experiment_metadata, definitions_content["experiment_metadata"]
        )
        for i, trial_def in enumerate(trial_definitions):
            self.assertEqual(trial_def["name"], "trial_" + str(i + 1))
            self.assertIn("param", trial_def["hyperparameters"])
            # NOTE: In real use case do not set the last score manually,
            # it is just done here to isolate the functionality under test.
            trial_definitions.suggester.set_last_score(1)
        with self.assertRaises(StopIteration):
            next(trial_definitions)

    def test_load_definitions_file_not_found(self):
        """
        Tests behavior when the definitions file does not exist.
        """
        with self.assertRaises(FileNotFoundError):
            load_experiment_definition(self.definitions_json_path)

    def _test_invalid_content(self, invalid_content=None):
        """
        Helper function to test invalid JSON content.

        Parameters
        ----------
        invalid_content : dict, optional
            The invalid content to write into the definitions file.
        """
        invalid_content = {
            "trial_definitions": [{"name": "trial_1", "hyperparameters": {}}]
        }
        self._write_definitions_to_file(invalid_content)
        with self.assertRaises(AssertionError):
            load_experiment_definition(self.definitions_json_path)

    def test_invalid_contents(self):
        """
        Tests various invalid JSON structures for experiment definitions.
        """
        invalid_contents = [
            {
                "trial_definitions": [
                    {"name": "trial_1", "hyperparameters": {}}
                ]
            },
            {"experiment_metadata": self.experiment_metadata},
            {
                "experiment_metadata": self.experiment_metadata,
                "trial_definitions": [{"name": "trial_1"}],
            },
            {
                "experiment_metadata": self.experiment_metadata,
                "trial_definitions": {},
            },
        ]
        for invalid_content in invalid_contents:
            self._test_invalid_content(invalid_content)

    def test_unused_key_in_trial_definitions(self):
        """
        Tests that a warning is raised when an unused key is present
        in the trial definitions.
        """
        unused_key = {
            "experiment_metadata": self.experiment_metadata,
            "trial_definitions": {"hparams_configs": {}, "unused_key": 1},
        }
        self._write_definitions_to_file(unused_key)
        with self.assertWarns(UserWarning):
            load_experiment_definition(self.definitions_json_path)


if __name__ == "__main__":
    unittest.main()
