from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase
from imlresearch.src.utils.tests.get_sample_from_distribution_test import TestGetSampleFromDistribution    # noqa: E501
from imlresearch.src.utils.tests.unbatch_dataset_if_batched_test import TestUnbatchDatasetIfBatched     # noqa: E501


class UtilsTestRunner(TestRunnerBase):
    """
    Test runner for the Utils module.
    """

    def load_tests(self):
        """
        Load the test cases for the Utils module.
        """
        self.load_test_case(TestUnbatchDatasetIfBatched)
        self.load_test_case(TestGetSampleFromDistribution)


def run_tests():
    """
    Run the tests for the Utils module.

    Returns
    -------
    unittest.TestResult
        The test result object.
    """
    runner = UtilsTestRunner()
    return runner.run_tests()

if __name__ == "__main__":
    run_tests()