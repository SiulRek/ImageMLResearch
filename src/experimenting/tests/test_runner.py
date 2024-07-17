import os
import unittest
from unittest import defaultTestLoader as Loader

from src.experimenting.tests.experiment_data_test import TestLoadExperimentData
from src.experimenting.tests.experiment_test import TestExperiment
from src.experimenting.tests.trial_test import TestTrial
from src.testing.helpers.test_result_logger import TestResultLogger

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, r"src/experimenting/tests/outputs")
LOG_FILE = os.path.join(OUTPUT_DIR, "test_results.log")


def load_tests(test_suite):
    test_suite.addTest(Loader.loadTestsFromTestCase(TestExperiment))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestTrial))
    test_suite.addTest(Loader.loadTestsFromModule(TestLoadExperimentData))
    return test_suite


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    TestResultLogger(LOG_FILE)  # Initialize Test Result Logger.

    test_suite = unittest.TestSuite()
    unittest.TextTestRunner().run(load_tests(test_suite))
