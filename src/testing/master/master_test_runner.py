"""
This module is designed to facilitate the running of all unit tests across the
various submodules of the PCB Defect Detection system. It uses Python's built-in
unittest framework to run tests located in the 'tests' subdirectory of each
module.
"""

import os
import unittest

import src.data_handling.tests.test_runner as data_handling_tests
import src.experimenting.tests.test_runner as experimenting_tests
import src.plotting.tests.test_runner as plotting_tests
import src.research.tests.test_runner as research_tests
from src.testing.helpers.generate_test_results_message import (
    generate_test_result_message,
)
from src.testing.helpers.test_result_logger import TestResultLogger
import src.training.tests.test_runner as training_tests
import src.utils.tests.test_runner as utils_tests

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(FILE_DIR, "test_results.log")


def run_tests():
    test_suite = unittest.TestSuite()

    # Load tests from test modules
    test_suite = utils_tests.load_tests(test_suite)
    # NOTE: preprocessing tests currently disabled for performance reasons.
    # test_suite = preprocessing_tests.load_tests(test_suite)
    test_suite = data_handling_tests.load_tests(test_suite)
    test_suite = plotting_tests.load_tests(test_suite)
    test_suite = utils_tests.load_tests(test_suite)
    test_suite = experimenting_tests.load_tests(test_suite)
    test_suite = training_tests.load_tests(test_suite)
    test_suite = research_tests.load_tests(test_suite)

    result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    msg = generate_test_result_message(result)

    return msg


if __name__ == "__main__":

    os.makedirs(FILE_DIR, exist_ok=True)
    TestResultLogger(LOG_FILE)

    message = run_tests()
    print(message)
