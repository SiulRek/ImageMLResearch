from src.preprocessing.tests.for_helpers import copy_json_exclude_entries_test
from src.preprocessing.tests.for_helpers import recursive_type_conversion_test
from src.preprocessing.tests.for_helpers import randomly_select_sequential_keys_test
from src.preprocessing.tests.for_helpers import parse_and_repeat_test
from src.preprocessing.tests.for_helpers import json_instances_serializer_test
from src.preprocessing.tests.for_preprocessor import image_preprocessor_test
from src.preprocessing.tests.for_preprocessor.long_pipeline_test import (
    load_long_pipeline_tests,
)
from src.preprocessing.tests.for_steps import step_base_test
from src.preprocessing.tests.for_steps.channel_conversions_steps_test import (
    load_channel_conversion_steps_tests,
)
from src.preprocessing.tests.for_steps.data_augmentation_steps_test import (
    load_data_augmentation_steps_tests,
)
from src.preprocessing.tests.for_steps.multiple_steps_test import (
    load_multiple_steps_tests,
)
from src.preprocessing.tests.for_steps.resize_operations_steps_test import (
    load_resize_operations_steps_tests,
)
from src.testing.bases.test_runner_base import TestRunnerBase


class PreprocessingTestRunner(TestRunnerBase):
    """ A test runner for image preprocessing tests. This runner aggregates tests
    from different modules and adds them to the test suite. """

    def load_tests(self):
        """
        Populates the test suite with a series of test cases from the image
        preprocessing testing framework.

        This function aggregates tests from different aspects of the image
        preprocessing pipeline. It includes basic tests, tests for multiple
        steps, specific channel conversion tests, and general image
        preprocessing tests.
        """
        self.load_test_module(copy_json_exclude_entries_test)
        self.load_test_module(recursive_type_conversion_test)
        self.load_test_module(randomly_select_sequential_keys_test)
        self.load_test_module(json_instances_serializer_test)
        self.load_test_module(parse_and_repeat_test)
        self.load_test_module(step_base_test)
        self.load_test_module(image_preprocessor_test)
        self.test_suite.addTest(load_multiple_steps_tests())
        self.test_suite.addTest(load_channel_conversion_steps_tests())
        self.test_suite.addTest(load_resize_operations_steps_tests())
        self.test_suite.addTest(load_data_augmentation_steps_tests())
        self.test_suite.addTest(load_long_pipeline_tests(1))


if __name__ == "__main__":
    runner = PreprocessingTestRunner()
    runner.run_tests()
