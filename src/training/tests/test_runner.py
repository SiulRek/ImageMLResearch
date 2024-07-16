import os
import unittest
from unittest import defaultTestLoader as Loader

from src.testing.helpers.test_result_logger import TestResultLogger
from src.training.tests.evaluate_test import (
    TestEvaluate,
)
from src.training.tests.trainer_test import TestTrainer

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, "src/training/tests/outputs")
LOG_FILE = os.path.join(OUTPUT_DIR, "test_results.log")


def load_tests(test_suite):
    test_suite.addTest(Loader.loadTestsFromTestCase(TestEvaluate))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestTrainer))
    return test_suite


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    TestResultLogger(LOG_FILE)  # Initialize Test Result Logger.

    test_suite = unittest.TestSuite()
    unittest.TextTestRunner().run(load_tests(test_suite))
