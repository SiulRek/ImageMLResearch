from imlresearch.src.experimenting.tests.experiment_assets_test import TestLoadExperimentAssets
from imlresearch.src.experimenting.tests.experiment_test import TestExperiment
from imlresearch.src.experimenting.tests.hparams_suggester_test import TestHParamsSuggester
from imlresearch.src.experimenting.tests.last_score_singleton_test import TestLastScoreSingleton
from imlresearch.src.experimenting.tests.load_experiment_definition_test import (
    TestLoadExperimentDefinition,
)
from imlresearch.src.experimenting.tests.trial_test import TestTrial
from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase


class ExperimentingTestRunner(TestRunnerBase):
    """ Test Runner for the Experimenting Module. """

    def load_tests(self):
        self.load_test_case(TestExperiment)
        self.load_test_case(TestTrial)
        self.load_test_case(TestLoadExperimentAssets)
        self.load_test_case(TestHParamsSuggester)
        self.load_test_case(TestLoadExperimentDefinition)
        self.load_test_case(TestLastScoreSingleton)


if __name__ == "__main__":
    runner = ExperimentingTestRunner()
    runner.run_tests()
