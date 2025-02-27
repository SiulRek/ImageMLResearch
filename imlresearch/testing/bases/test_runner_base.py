from abc import ABC, abstractmethod
import os
import sys
import unittest
from unittest import defaultTestLoader as Loader

from imlresearch.testing.helpers.generate_test_results_message import (
    generate_test_results_message,
)
from imlresearch.testing.helpers.test_result_logger import TestResultLogger


class TestRunnerBase(ABC):
    """
    A base class for running unit tests. This class sets up the environment for
    test execution, including initializing loggers and managing test suites.
    Subclasses should implement the `load_tests` method to specify which tests
    to run.
    """

    def __init__(self):
        """ Initializes the TestRunnerBase instance, setting up the test file path,
        output directory, logger, and test suite. """
        self.test_file = self._infere_test_file_path()
        self.output_dir = self._compute_output_dir()
        os.makedirs(self.output_dir, exist_ok=True)
        self._init_logger()
        self.test_suite = unittest.TestSuite()

    def _init_logger(self):
        """ Initializes the test result logger, creating a log file in the output
        directory. """
        self.log_file = os.path.join(self.output_dir, "test_results.log")
        TestResultLogger(self.log_file)  # Initialize Test Result Logger.

    @classmethod
    def _infere_test_file_path(cls):
        """
        Infers the file path of the test file. This method first attempts to
        infer the file path from the module information. If that fails, it
        attempts to infer the path from the command-line arguments.

        Returns:
            - str: The inferred file path.
        """
        module = cls.__module__
        if module in sys.modules:
            return sys.modules[module].__file__
        msg = "Cannot infer test file path."
        raise FileNotFoundError(msg)

    # ------ Duplicated Method from BaseTestCase ----------------------
    @classmethod
    def _compute_output_dir(cls, parent_folder="tests"):
        """
        Computes the directory path for test outputs by traversing up the file
        hierarchy until a directory named 'tests' is found. It then returns the
        path to the 'outputs' subdirectory within 'tests'.

        Args:
            - parent_folder (str, optional): The name of the parent folder
                containing the 'tests' directory. Default is "tests".

        Returns:
            - str: The path to the output directory.

        Raises:
            - NotADirectoryError: If the 'tests' directory is not found in
                the path hierarchy.
        """
        current_dir = os.path.dirname(cls._infere_test_file_path())

        while parent_folder not in os.listdir(current_dir):
            current_dir = os.path.dirname(current_dir)
            if current_dir == os.path.dirname(current_dir):
                msg = "Tests directory not found in the path hierarchy."
                raise NotADirectoryError(msg)

        return os.path.join(current_dir, parent_folder, "outputs")

    # ------------------------------------------------------------------

    @abstractmethod
    def load_tests(self):
        """ Abstract method to load specific tests. This method should be overridden
        in subclasses to specify which tests to add to the test suite. """
        pass

    def load_test_case(self, test_case):
        """
        Adds a test case to the test suite.

        Args:
            - test_case (unittest.TestCase): The test case to add.
        """
        self.test_suite.addTest(Loader.loadTestsFromTestCase(test_case))

    def load_test_module(self, test_module):
        """
        Adds all the test cases from a module to the test suite.

        Args:
            - test_module (module): The test module to add.
        """
        self.test_suite.addTest(Loader.loadTestsFromModule(test_module))

    def run_tests(self):
        """ Runs the tests in the test suite and prints the results if called from
        the command line. """
        self.load_tests()
        test_result = unittest.TextTestRunner().run(self.test_suite)
        print("\n" + "*" * 35 + "\n")
        msg = generate_test_results_message(test_result)
        print(msg)
        print()
        print("Test results logged to:", self.log_file)
        error_log_file = self.log_file.replace(".log", "_errors.log")
        print("Test errors logged to:", error_log_file)
        simple_log_file = self.log_file.replace(".log", "_simple.log")
        print("Simple test results logged to:", simple_log_file)
