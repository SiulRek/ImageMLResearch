from imlresearch.src.data_handling.tests import prepare_dataset_test
from imlresearch.src.data_handling.tests import (
    shuffle_dataset_test,
    save_images_test,
    label_manager_test,
    create_dataset_test,
    split_dataset_test,
    tfrecord_serialization_test,
)
from imlresearch.src.data_handling.tests.data_handler_test import (
    TestDataHandler,
)
from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase


class DataHandlingTestRunner(TestRunnerBase):
    """
    Test Runner for the Data Handling Module.
    """

    def load_tests(self):
        self.load_test_module(create_dataset_test)
        self.load_test_module(label_manager_test)
        self.load_test_module(split_dataset_test)
        self.load_test_module(prepare_dataset_test)
        self.load_test_module(tfrecord_serialization_test)
        self.load_test_case(TestDataHandler)
        self.load_test_module(shuffle_dataset_test)
        self.load_test_module(save_images_test)


def run_tests():
    """
    Run the tests for the Data Handling module.

    Returns
    -------
    unittest.TestResult
        The test result object.
    """
    runner = DataHandlingTestRunner()
    return runner.run_tests()


if __name__ == "__main__":
    run_tests()
