import os
import unittest
from unittest import defaultTestLoader as Loader

from src.testing.helpers.test_result_logger import TestResultLogger
from src.utils.tests import get_sample_from_distribution_test
from src.utils.tests import unbatch_dataset_if_batched_test

ROOT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."
)
OUTPUT_DIR = os.path.join(ROOT_DIR, r"src/utils/tests/outputs")
LOG_FILE = os.path.join(OUTPUT_DIR, "test_results.log")


def load_tests(test_suite):
    test_suite.addTest(Loader.loadTestsFromModule(get_sample_from_distribution_test))
    test_suite.addTest(Loader.loadTestsFromModule(unbatch_dataset_if_batched_test))
    return test_suite


if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    TestResultLogger(LOG_FILE)  # Initialize Test Result Logger.

    test_suite = unittest.TestSuite()
    unittest.TextTestRunner().run(load_tests(test_suite))
