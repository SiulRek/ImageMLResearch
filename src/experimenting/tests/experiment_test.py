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
from src.testing.bases.base_test_case import BaseTestCase


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
        self.experiment_json = os.path.join(
            self.directory, "output", "experiment_info.json"
        )
        self.description = "This is a test experiment"
        self.sort_metric = "accuracy"
        self.sort_metric_inv = "accuracy_inv"
        self.call_test_experiment = lambda: Experiment(
            research_attributes=self.research_attributes,
            directory=self.directory,
            name=self.name,
            description=self.description,
            sort_metric=self.sort_metric,
        )

    def test_experiment_initialization(self):
        # Check experiment data initialization
        with self.call_test_experiment() as experiment:
            self.assertIsInstance(experiment, Experiment)
            self.assertEqual(experiment.experiment_assets["name"], self.name)
            self.assertEqual(
                experiment.experiment_assets["description"], self.description
            )
            self.assertTrue(os.path.exists(experiment.experiment_assets["directory"]))
            log_file = os.path.join(
                experiment.experiment_assets["directory"], "execution.log"
            )
            self.assertTrue(os.path.exists(log_file))

    def test_experiment_data_written_to_json(self):
        with self.call_test_experiment() as experiment:
            pass
        self.assertTrue(os.path.exists(self.experiment_json))

        with open(self.experiment_json, "r", encoding="utf-8") as f:
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
                experiment.experiment_assets
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

    def _run_trials_in_experiment(self, trial_definitions, sleep_time=None):
        with self.call_test_experiment() as experiment:
            trial_runned = False
            for i, (name, hyperparameters) in enumerate(trial_definitions):
                with experiment.run_trial(name, hyperparameters) as trial:
                    self.assertIsInstance(trial, Trial)
                    self.assertEqual(trial.trial_assets["name"], name)
                    self.assertEqual(
                        trial.trial_assets["hyperparameters"], hyperparameters
                    )
                    self.assertTrue("start_time" in trial.trial_assets)
                    # Simulate accuracy
                    metric_val = float(1 - i * 0.1)
                    metric_inv_val = float(1 - metric_val)
                    metric_kw = {
                        self.sort_metric: metric_val,
                        self.sort_metric_inv: metric_inv_val,
                    }
                    metrics_set = {"test": metric_kw}
                    experiment._evaluation_metrics.update(metrics_set)
                    trial_runned = True
            if trial_runned:
                self.assertIn(trial.trial_assets, experiment.experiment_assets["trials"])

            if sleep_time is not None:
                sleep(sleep_time)

        return experiment

    def test_trials_creation(self):

        trial_definitions = [
            ("trial1", {"lr": 0.01, "batch_size": 16}),
            ("trial2", {"lr": 0.001, "batch_size": 32}),
        ]
        experiment = self._run_trials_in_experiment(trial_definitions)

        self.assertEqual(len(experiment.experiment_assets["trials"]), 2)

    def test_load_experiment_data(self):
        trial_definitions = [
            ("trial1", {"lr": 0.01, "batch_size": 16}),
            ("trial2", {"lr": 0.001, "batch_size": 32}),
        ]
        new_description = "This is a new description"
        new_sort_metric = "accuracy_inv"

        experiment = self._run_trials_in_experiment(trial_definitions)
        reloaded_experiment = Experiment(
            research_attributes=self.research_attributes,
            directory=self.directory,
            name=self.name,
            description=new_description,
            sort_metric=new_sort_metric,
        )
        # Check if experiment_data is updated correctly.
        description = reloaded_experiment.experiment_assets["description"]
        sort_metric = reloaded_experiment.experiment_assets["sort_metric"]
        self.assertEqual(description, new_description)
        self.assertEqual(sort_metric, new_sort_metric)
        # Check if the trials are loaded correctly
        trials_data = experiment.experiment_assets["trials"]
        reloaded_trials_data = reloaded_experiment.experiment_assets["trials"]

        self.assertIn(trials_data[0], reloaded_trials_data)
        self.assertIn(trials_data[1], reloaded_trials_data)

    # def test_load_experiment_data_with_warnings(self):
    #     trial_definitions = [
    #         ("trial1", {"lr": 0.01, "batch_size": 16}),
    #         ("trial2", {"lr": 0.001, "batch_size": 32}),
    #     ]
    #     self._run_trials_in_experiment(trial_definitions)

    #     new_name = "new_experiment"
    #     # XXX: Warning is not being caught even when issued.
    #     with self.assertWarns(UserWarning):
    #         Experiment(
    #             research_attributes=self.research_attributes,
    #             directory=self.directory,
    #             name=new_name,
    #             description=self.description,
    #             sort_metric=self.sort_metric,
    #         )

    def test_trials_order(self):

        def metric_val(trial_num, metric):
            trial = experiment.experiment_assets["trials"][trial_num]
            metrics_set = trial["evaluation_metrics"]["test"]
            return metrics_set[metric]

        trial_definitions = [
            ("trial1", {"lr": 0.01, "batch_size": 16}),
            ("trial2", {"lr": 0.001, "batch_size": 32}),
        ]
        experiment = self._run_trials_in_experiment(trial_definitions)

        # Ordered by accuracy
        metric_1st_trial = metric_val(0, self.sort_metric)
        metric_2nd_trial = metric_val(1, self.sort_metric)
        self.assertGreater(metric_1st_trial, metric_2nd_trial)

        # Modify the experiment to sort by accuracy_inv
        metric_kw = {"sort_metric": self.sort_metric_inv}
        self._modify_experiment_json(metric_kw)

        self._run_trials_in_experiment([])
        # Ordered by accuracy_inv
        metric_1st_trial = metric_val(0, self.sort_metric_inv)
        metric_2nd_trial = metric_val(1, self.sort_metric_inv)
        self.assertLess(metric_1st_trial, metric_2nd_trial)

    def _modify_experiment_json(self, kwargs):
        with open(self.experiment_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        for key, value in kwargs.items():
            data[key] = value
        with open(self.experiment_json, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def test_resume_experiment(self):
        def get_experiment_duration(experiment):
            duration = experiment.experiment_assets["duration"]
            duration = float(duration.replace(":", ""))
            return duration

        trial_definitions = [
            ("trial1", {"lr": 0.01, "batch_size": 16}),
            ("trial2", {"lr": 0.001, "batch_size": 32}),
        ]
        initial_experiment = self._run_trials_in_experiment(
            trial_definitions, sleep_time=0.01
        )
        initial_duration = get_experiment_duration(initial_experiment)

        del initial_experiment

        new_trial_definitions = [
            ("trial3", {"lr": 0.001, "batch_size": 32}),
            ("trial4", {"lr": 0.001, "batch_size": 32}),
        ]
        resumed_experiment = self._run_trials_in_experiment(
            new_trial_definitions, sleep_time=0.01
        )
        total_duration = get_experiment_duration(resumed_experiment)

        self.assertEqual(len(resumed_experiment.experiment_assets["trials"]), 4)
        self.assertGreater(total_duration, initial_duration)


if __name__ == "__main__":
    unittest.main()
