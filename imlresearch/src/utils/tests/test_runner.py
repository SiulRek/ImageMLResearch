from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase
from imlresearch.src.utils.tests.get_sample_from_distribution_test import (
    TestGetSampleFromDistribution,
)
from imlresearch.src.utils.tests.unbatch_dataset_if_batched_test import TestUnbatchDatasetIfBatched


class UtilsTestRunner(TestRunnerBase):
    """ Test Runner for the Utils Module. """

    def load_tests(self):
        """ Loads the tests for the Utils Module. """
        self.load_test_case(TestUnbatchDatasetIfBatched)
        self.load_test_case(TestGetSampleFromDistribution)


if __name__ == "__main__":
    runner = UtilsTestRunner()
    runner.run_tests()
