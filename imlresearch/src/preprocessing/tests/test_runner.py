from imlresearch.src.preprocessing.tests.for_helpers import (
    copy_json_exclude_entries_test,
    recursive_type_conversion_test,
    randomly_select_sequential_keys_test,
    parse_and_repeat_test,
    json_instances_serializer_test,
)
from imlresearch.src.preprocessing.tests.for_preprocessor import (
    image_preprocessor_test,
)
from imlresearch.src.preprocessing.tests.for_preprocessor.long_pipeline_test import (  # noqa
    load_long_pipeline_tests,
)
from imlresearch.src.preprocessing.tests.for_steps import step_base_test
from imlresearch.src.preprocessing.tests.for_steps.channel_conversions_steps_test import (  # noqa
    load_channel_conversion_steps_tests,
)
from imlresearch.src.preprocessing.tests.for_steps.data_augmentation_steps_test import (  # noqa
    load_data_augmentation_steps_tests,
)
from imlresearch.src.preprocessing.tests.for_steps.multiple_steps_test import (  # noqa
    load_multiple_steps_tests,
)
from imlresearch.src.preprocessing.tests.for_steps.resize_operations_steps_test import (  # noqa
    load_resize_operations_steps_tests,
)
from imlresearch.src.testing.bases.test_runner_base import TestRunnerBase


class PreprocessingTestRunner(TestRunnerBase):
    """
    A test runner for image preprocessing tests. This runner aggregates tests
    from different modules and adds them to the test suite.
    """

    def load_tests(self):
        """
        Populate the test suite with test cases for image preprocessing.

        This method aggregates test cases covering various preprocessing
        functionalities, including:

        - Basic preprocessing operations.
        - Multi-step preprocessing pipelines.
        - Image channel conversions.
        - Resize operations.
        - General image preprocessing tasks.
        """

        helper_tests = [
            copy_json_exclude_entries_test,
            recursive_type_conversion_test,
            randomly_select_sequential_keys_test,
            json_instances_serializer_test,
            parse_and_repeat_test,
            step_base_test,
            image_preprocessor_test,
        ]
        for test in helper_tests:
            self.load_test_module(test)

        self.test_suite.addTest(load_multiple_steps_tests())
        self.test_suite.addTest(load_channel_conversion_steps_tests())
        self.test_suite.addTest(load_resize_operations_steps_tests())
        self.test_suite.addTest(load_data_augmentation_steps_tests())
        self.test_suite.addTest(load_long_pipeline_tests(1))


def run_tests():
    """
    Run the tests for the Preprocessing module.

    Returns
    -------
    unittest.TestResult
        The test result object.
    """
    runner = PreprocessingTestRunner()
    return runner.run_tests()


if __name__ == "__main__":
    run_tests()
