import os
import unittest
from unittest import defaultTestLoader as Loader

from src.plotting.tests.binary_plotter_test import TestBinaryPlotter
from src.plotting.tests.multi_class_plotter_test import TestMultiClassPlotter
from src.plotting.tests.plot_confusion_matrix_test import TestPlotConfusionMatrix
from src.plotting.tests.plot_decorator_test import TestPlotDecorator
from src.plotting.tests.plot_images_test import TestPlotImages
from src.plotting.tests.plot_model_summary_test import TestPlotModelSummary
import src.plotting.tests.plot_results_test as plot_results_test
from src.plotting.tests.plot_text_test import TestPlotText
from src.plotting.tests.plot_training_history_test import TestPlotTrainingHistory
from src.plotting.tests.plotter_test import TestPlotter
from src.testing.helpers.test_result_logger import TestResultLogger

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
OUTPUT_DIR = os.path.join(ROOT_DIR, r"src/plotting/tests/outputs")
LOG_FILE = os.path.join(OUTPUT_DIR, "test_results.log")


def load_tests(test_suite):
    """
    Populates the given test suite with the specified test cases.

    Args:
        - test_suite (unittest.TestSuite): The test suite to which the tests
            will be added.

    Returns:
        - unittest.TestSuite: The test suite populated with the specified
            tests.
    """
    test_suite.addTest(Loader.loadTestsFromTestCase(TestPlotConfusionMatrix))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestPlotText))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestPlotImages))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestPlotter))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestBinaryPlotter))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestMultiClassPlotter))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestPlotTrainingHistory))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestPlotDecorator))
    test_suite.addTest(Loader.loadTestsFromTestCase(TestPlotModelSummary))
    test_suite.addTest(Loader.loadTestsFromModule(plot_results_test))
    return test_suite


if __name__ == "__main__":
    """ Main execution block for running the aggregated test suite. """

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    TestResultLogger(LOG_FILE)  # Initialize Test Result Logger.
    test_suite = unittest.TestSuite()
    unittest.TextTestRunner().run(load_tests(test_suite))
