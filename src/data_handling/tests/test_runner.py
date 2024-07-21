from src.data_handling.tests import (
    shuffle_dataset_test,
    save_images_test,
    label_manager_test,
    create_dataset_test,
    split_dataset_test,
    enhance_dataset_test,
    tfrecord_serialization_test,
)
from src.data_handling.tests.data_handler_test import TestDataHandler
from src.testing.helpers.test_runner_base import TestRunnerBase


class DataHandlingTestRunner(TestRunnerBase):
    """ Test Runner for the Data Handling Module. """
    
    def load_tests(self):
        self.load_test_module(create_dataset_test)
        self.load_test_module(label_manager_test)
        self.load_test_module(split_dataset_test)
        self.load_test_module(enhance_dataset_test)
        self.load_test_module(tfrecord_serialization_test)
        self.load_test_case(TestDataHandler)
        self.load_test_module(shuffle_dataset_test)
        self.load_test_module(save_images_test)


if __name__ == "__main__":
    runner = DataHandlingTestRunner()
    runner.run_tests()
