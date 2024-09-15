from src.experimenting.tests.experiment_data_test import TestLoadExperimentData
from src.experimenting.tests.experiment_test import TestExperiment
from src.experimenting.tests.hparams_suggester_test import TestHParamsSuggester
from src.experimenting.tests.load_experiment_definitions_test import (
    TestLoadExperimentDefinitions,
)
from src.experimenting.tests.trial_test import TestTrial
from src.testing.bases.test_runner_base import TestRunnerBase


class ExperimentingTestRunner(TestRunnerBase):
    """ Test Runner for the Experimenting Module. """

    def load_tests(self):
        self.load_test_case(TestExperiment)
        self.load_test_case(TestTrial)
        self.load_test_module(TestLoadExperimentData)
        self.load_test_module(TestHParamsSuggester)
        self.load_test_module(TestLoadExperimentDefinitions)


if __name__ == "__main__":
    runner = ExperimentingTestRunner()
    runner.run_tests()
