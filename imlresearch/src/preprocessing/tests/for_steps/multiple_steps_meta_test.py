"""
This module contains tests for validating the functionality of the image
preprocessing test framework and focuses on dynamically generated test classes.
It provides tests to ensure that test classes are correctly created for one
example preprocessing step and that conditional test logic (skipping certain
tests) functions as expected.
"""

import unittest
from unittest.mock import patch

from imlresearch.src.preprocessing.steps import (
    AdaptiveHistogramEqualizer as ExampleStep,
)
from imlresearch.src.preprocessing.tests.for_steps.multiple_steps_test import (
    create_test_class_for_step,
)
from imlresearch.src.preprocessing.tests.for_steps.single_step_test import (
    TestSingleStep,
)


class TestTestFramework(unittest.TestCase):
    def test_dynamic_class_creation(self):
        """
        Test to verify the dynamic creation of test classes for preprocessing
        steps. Ensures that the class name is correct, the class inherits from
        `TestSingleStep`, and that `TestStep` and `parameters` attributes are
        properly set.
        """
        TestClass = create_test_class_for_step(
            ExampleStep, {"clip_limit": 1.0, "tile_gridsize": (5, 5)}
        )
        self.assertEqual(TestClass.__name__, "TestAdaptiveHistogramEqualizer")
        self.assertTrue(issubclass(TestClass, TestSingleStep))
        self.assertTrue(hasattr(TestClass, "TestStep"))
        self.assertTrue(hasattr(TestClass, "parameters"))

        test_instance = TestClass("test_load_from_json")
        self.assertEqual(test_instance.TestStep, ExampleStep)
        self.assertEqual(
            test_instance.parameters,
            {"clip_limit": 1.0, "tile_gridsize": (5, 5)},
        )


class TestConditionalSkipping(unittest.TestCase):
    def test_visual_inspection_skipping_1(self):
        """
        Test to verify that tests requiring visual inspection are skipped
        when `ENABLE_VISUAL_INSPECTION` is set to False.
        """
        with patch(
            "imlresearch.src.preprocessing.tests.multiple_steps_test."
            "ENABLE_VISUAL_INSPECTION",
            False,
        ):
            TestClass = create_test_class_for_step(
                ExampleStep, {"clip_limit": 1.0, "tile_gridsize": (5, 5)}
            )
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        result = unittest.TextTestRunner().run(suite)

        skipped_test_names = [
            test[0].id().split(".")[-1] for test in result.skipped
        ]
        self.assertIn("test_processed_image_visualization", skipped_test_names)
        TestClass = create_test_class_for_step(ExampleStep, {})

    def test_visual_inspection_skipping_2(self):
        """
        Test to verify that tests requiring visual inspection are skipped
        when `visual_inspection_always_disable` is set to True.
        """
        with patch(
            "imlresearch.src.preprocessing.tests.multiple_steps_test."
            "ENABLE_VISUAL_INSPECTION",
            True,
        ):
            TestClass = create_test_class_for_step(
                ExampleStep,
                {"clip_limit": 1.0, "tile_gridsize": (5, 5)},
                visual_inspection_always_disable=True,
            )
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        result = unittest.TextTestRunner().run(suite)

        skipped_test_names = [
            test[0].id().split(".")[-1] for test in result.skipped
        ]
        self.assertIn("test_processed_image_visualization", skipped_test_names)
        TestClass = create_test_class_for_step(ExampleStep, {})

    def test_visual_inspection_not_skipping(self):
        """
        Test to verify that tests requiring visual inspection are not skipped
        when `ENABLE_VISUAL_INSPECTION` is set to True.
        """
        with patch(
            "imlresearch.src.preprocessing.tests.multiple_steps_test."
            "ENABLE_VISUAL_INSPECTION",
            True,
        ):
            TestClass = create_test_class_for_step(
                ExampleStep, {"clip_limit": 1.0, "tile_gridsize": (5, 5)}
            )
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        result = unittest.TextTestRunner().run(suite)

        skipped_test_names = [
            test[0].id().split(".")[-1] for test in result.skipped
        ]
        self.assertNotIn(
            "test_processed_image_visualization",
            skipped_test_names,
        )  # Fixed line length issue
        TestClass = create_test_class_for_step(ExampleStep, {})


if __name__ == "__main__":
    unittest.main()
