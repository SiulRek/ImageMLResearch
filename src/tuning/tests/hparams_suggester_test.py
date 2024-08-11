import unittest

import numpy as np

from src.testing.bases.base_test_case import BaseTestCase
from src.tuning.hparams_suggester import HParamsSuggester


class TestHParamsSuggester(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.hparams_distributions_configs = {
            "learning_rate": {"type": "float", "low": 0.0001, "high": 0.1},
            "batch_size": {"type": "int", "low": 16, "high": 256, "log": True},
            "num_layers": {"type": "int", "low": 2, "high": 9},
            "activation": {
                "type": "categorical",
                "choices": ["relu", "tanh", "sigmoid"],
            },
        }
        self.suggester = HParamsSuggester(self.hparams_distributions_configs)

    def assert_valid_hyperparams(self, hyperparams):
        configs = self.hparams_distributions_configs
        for param in configs:
            self.assertIn(param, hyperparams)
            param_type = configs[param]["type"]
            if param_type in ["float", "int"]:
                self.assertIsInstance(hyperparams[param], (int, float))
                self.assertGreaterEqual(hyperparams[param], configs[param]["low"])
                self.assertLessEqual(hyperparams[param], configs[param]["high"])
            elif param_type == "categorical":
                self.assertIn(
                    hyperparams[param],
                    configs[param]["choices"],
                )
            else:
                self.fail(f"Invalid hyperparameter type {param_type} for {param}")

    def test_initial_suggestion(self):
        """ Test if the suggester provides a valid set of hyperparameters initially. """
        next_hyperparams = self.suggester.suggest_next()
        self.assert_valid_hyperparams(next_hyperparams)
        self.assertIsNotNone(self.suggester.current_trial)

    def test_to_nearest_power2(self):
        """ Test if the suggester correctly rounds to the nearest power of two. """
        hparams_distributions_configs = {
            "batch_size": {
                "type": "int",
                "low": 16,
                "high": 256,
                "nearest_power2": True,
            },
        }
        suggester = HParamsSuggester(hparams_distributions_configs)
        batch_sizes = []
        for _ in range(5):
            next_hyperparams = suggester.suggest_next()
            batch_sizes.append(next_hyperparams["batch_size"])
            suggester.set_last_score(np.random.uniform(0.8, 0.95))
        for batch_size in batch_sizes:
            self.assertTrue(np.log2(batch_size).is_integer())

    def test_update_trial(self):
        """ Test if the suggester updates the trial correctly after setting the
        score. """
        next_hyperparams = self.suggester.suggest_next()
        trial_1 = self.suggester.current_trial
        self.assert_valid_hyperparams(next_hyperparams)
        simulated_score = np.random.uniform(8, 0.95)
        self.suggester.set_last_score(simulated_score)
        next_suggestion = self.suggester.suggest_next()
        trial_2 = self.suggester.current_trial
        self.assert_valid_hyperparams(next_suggestion)
        self.assertNotEqual(trial_1, trial_2)

    def test_invalid_config(self):
        """ Test if the suggester raises an error with an invalid configuration. """
        invalid_config = {
            "learning_rate": {"type": "float", "low": 0.1},
            "batch_size": {"type": "int", "low": 16},
            "num_layers": {"type": "int", "low": 2, "high": "nine"},
            "activation": {
                "type": "invalid_type",
                "choices": ["relu", "tanh", "sigmoid"],
            },
        }
        with self.assertRaises(AssertionError):
            HParamsSuggester(invalid_config)

    def test_multiple_trials(self):
        """ Test if the suggester correctly handles multiple trials. """
        for _ in range(5):
            next_hyperparams = self.suggester.suggest_next()
            self.assert_valid_hyperparams(next_hyperparams)
            simulated_score = np.random.uniform(0.8, 0.95)
            self.suggester.set_last_score(simulated_score)

        trials = self.suggester.study.trials
        self.assertEqual(len(trials), 5)

        # Check if all trials are unique
        for i, trial in enumerate(trials):
            for j in range(i + 1, len(trials)):
                self.assertNotEqual(trial, trials[j])


if __name__ == "__main__":
    unittest.main()
