"""
This module is designed to facilitate the running of all unit tests across the
various submodules of the Researcher system. It uses Python's built-in unittest
framework to run tests located in the 'tests' subdirectory of each module.
"""

import os
import unittest

from imlresearch.data_handling.tests.test_runner import DataHandlingTestRunner
from imlresearch.experimenting.tests.test_runner import ExperimentingTestRunner
from imlresearch.plotting.tests.test_runner import PlottingTestRunner
from imlresearch.research.tests.test_runner import ResearchTestRunner
from imlresearch.testing.helpers.generate_test_results_message import (
    generate_test_results_message,
)
from imlresearch.testing.helpers.test_result_logger import TestResultLogger
from imlresearch.training.tests.test_runner import TrainingTestRunner
from imlresearch.utils.tests.test_runner import UtilsTestRunner

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FILE_DIR, "test_results.log")


def run_tests():
    """
    Runs all the tests from various submodules and aggregates the results.

    Returns:
        - str: A message summarizing the test results.
    """
    os.makedirs(FILE_DIR, exist_ok=True)
    TestResultLogger(LOG_FILE)

    test_suite = unittest.TestSuite()

    # Instantiate test runners and add their tests to the suite
    test_runners = [
        DataHandlingTestRunner(),
        # NOTE: preprocessing tests currently disabled for performance reasons.
        # PreprocessingTestRunner(),
        ExperimentingTestRunner(),
        PlottingTestRunner(),
        ResearchTestRunner(),
        TrainingTestRunner(),
        UtilsTestRunner(),
    ]

    for runner in test_runners:
        runner.load_tests()
        test_suite.addTests(runner.test_suite)

    result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    msg = generate_test_results_message(result)

    print(msg)
    error_log_file = LOG_FILE.replace(".log", "_errors.log")
    simple_log_file = LOG_FILE.replace(".log", "_simple.log")
    print(f"Test results logged to file: {LOG_FILE}")
    print(f"Test errors logged to file: {error_log_file}")
    print(f"Simple test results logged to file: {simple_log_file}")


if __name__ == "__main__":
    """ Main execution block for running the aggregated test suite. """

    run_tests()
