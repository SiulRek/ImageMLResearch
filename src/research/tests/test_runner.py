import os
import unittest
from unittest import defaultTestLoader as Loader

from src.research.tests.data_retriever_test import TestDataRetriever
from src.research.tests.module_level_workflow.multi_class_workflow_test import (
    TestMultiClassModuleLevelWorkflow,
)
from src.research.tests.researcher_level_workflow.multi_class_workflow_test import (
    TestMultiClassResearcherLevelWorkflow,
)
from src.testing.helpers.test_result_logger import TestResultLogger

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, r"src/research/tests/outputs")
LOG_FILE = os.path.join(OUTPUT_DIR, "test_results.log")


def load_tests(test_suite):
    test_suite.addTest(Loader.loadTestsFromTestCase(TestMultiClassModuleLevelWorkflow))
    test_suite.addTest(
        Loader.loadTestsFromTestCase(TestMultiClassResearcherLevelWorkflow)
    )
    test_suite.addTest(Loader.loadTestsFromTestCase(TestDataRetriever))
    return test_suite


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    TestResultLogger(LOG_FILE)  # Initialize Test Result Logger.

    test_suite = unittest.TestSuite()
    unittest.TextTestRunner().run(load_tests(test_suite))
