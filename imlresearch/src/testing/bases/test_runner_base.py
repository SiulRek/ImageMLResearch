from abc import ABC, abstractmethod
import os
import sys
import unittest
from unittest import defaultTestLoader as Loader

from imlresearch.src.testing.helpers.generate_test_results_message import (
    generate_test_results_message,
)
from imlresearch.src.testing.helpers.test_result_logger import TestResultLogger


class TestRunnerBase(ABC):
    """
    Base class for running unit tests.

    This class sets up the environment for test execution, including
    initializing loggers and managing test suites. Subclasses should
    implement the `load_tests` method to specify which tests to run.
    """

    def __init__(self):
        """
        Initialize the TestRunnerBase instance.

        This method sets up the test file path, output directory, logger,
        and test suite.
        """
        self.test_file = self._infere_test_file_path()
        self.output_dir = self._compute_output_dir()
        os.makedirs(self.output_dir, exist_ok=True)
        self._init_logger()
        self.test_suite = unittest.TestSuite()

    def _init_logger(self):
        """
        Initialize the test result logger.

        This method creates a log file in the output directory.
        """
        self.log_file = os.path.join(self.output_dir, "test_results.log")
        TestResultLogger(self.log_file)  # Initialize Test Result Logger.

    @classmethod
    def _infere_test_file_path(cls):
        """
        Infer the file path of the test file.

        This method attempts to infer the file path from the module
        information. If that fails, it tries to infer the path from the
        command-line arguments.

        Returns
        -------
        str
            The inferred file path.
        """
        module = cls.__module__
        if module in sys.modules:
            return sys.modules[module].__file__
        raise FileNotFoundError("Cannot infer test file path.")

    @classmethod
    def _compute_output_dir(cls, parent_folder="tests"):
        """
        Compute the directory path for test outputs.

        This method traverses up the file hierarchy until it finds a
        directory named 'tests', then returns the path to the 'outputs'
        subdirectory.

        Parameters
        ----------
        parent_folder : str, optional
            The parent folder name that contains the 'tests' directory,
            by default "tests".

        Returns
        -------
        str
            The path to the output directory.
        """
        current_dir = os.path.dirname(cls._infere_test_file_path())

        while parent_folder not in os.listdir(current_dir):
            current_dir = os.path.dirname(current_dir)
            if current_dir == os.path.dirname(current_dir):
                raise NotADirectoryError(
                    "Tests directory not found in the path hierarchy."
                )

        return os.path.join(current_dir, parent_folder, "outputs")

    @abstractmethod
    def load_tests(self):
        """
        Load specific tests into the test suite.

        This method should be overridden in subclasses to specify which tests
        to add to the test suite.
        """
        pass

    def load_test_case(self, test_case):
        """
        Add a test case to the test suite.

        Parameters
        ----------
        test_case : unittest.TestCase
            The test case to add.
        """
        self.test_suite.addTest(Loader.loadTestsFromTestCase(test_case))

    def load_test_module(self, test_module):
        """
        Add all test cases from a module to the test suite.

        Parameters
        ----------
        test_module : module
            The test module to add.
        """
        self.test_suite.addTest(Loader.loadTestsFromModule(test_module))

    def run_tests(self):
        """
        Run the tests in the test suite.

        Prints the results if called from the command line.

        Returns
        -------

        unittest.TestResult
            The test result object.
        """
        self.load_tests()
        test_result = unittest.TextTestRunner().run(self.test_suite)

        print("\n" + "*" * 35 + "\n")
        print(generate_test_results_message(test_result))
        print()
        print(f"Test results logged to: {self.log_file}")
        print(
            f"Test errors logged to: "
            f"{self.log_file.replace('.log', '_errors.log')}"
        )
        print(
            f"Simple test results logged to: "
            f"{self.log_file.replace('.log', '_simple.log')}"
        )
        
        return test_result
