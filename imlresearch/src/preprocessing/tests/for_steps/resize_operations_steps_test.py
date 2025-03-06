"""
Test suites for image preprocessing steps performing resize operations.

This module provides test cases for preprocessing steps that perform
resize operations within the image preprocessing pipeline. It ensures
correct integration and functionality of these steps.
"""

import unittest
from unittest import skip

import imlresearch.src.preprocessing.steps as steps
from imlresearch.src.preprocessing.tests.for_steps.single_step_test import (
    TestSingleStep,
)

ENABLE_VISUAL_INSPECTION = True


class TestSquareShapePadder(TestSingleStep):
    """
    Test suite for the SquareShapePadder step in the preprocessing pipeline.

    This class verifies that images are correctly padded to a square shape
    using the specified pixel value.

    Attributes
    ----------
    TestStep : type
        The preprocessing step class being tested (`steps.SquareShapePadder`).
    parameters : dict
        Dictionary containing parameters for `SquareShapePadder`.
    """

    TestStep = steps.SquareShapePadder
    parameters = {"padding_pixel_value": 0}

    if not ENABLE_VISUAL_INSPECTION:

        @skip("Visual inspection not enabled")
        def test_processed_image_visualization(self):
            pass

    def _verify_image_shapes(
        self, processed_dataset, original_dataset, color_channel_expected
    ):
        """
        Verify image dimensions and color channels in the processed dataset.

        Compares processed images to the original dataset to ensure that
        padding modifies height and width while maintaining the expected
        number of color channels.

        Parameters
        ----------
        processed_dataset : list
            List of processed images.
        original_dataset : list
            List of original images before processing.
        color_channel_expected : int
            Expected number of color channels in the processed images.
        """
        for original_image, processed_image in zip(
            original_dataset, processed_dataset
        ):
            processed_shape = tuple(processed_image.shape[:2].as_list())
            original_shape = tuple(original_image.shape[:2].as_list())
            self.assertNotEqual(processed_shape, original_shape)
            self.assertEqual(
                color_channel_expected,
                processed_image.shape[2],
                "Color channels are not equal.",
            )
            self.assertEqual(
                processed_shape[0],
                processed_shape[1],
                "Heights and widths are not equal.",
            )


class TestShapeResizer(TestSingleStep):
    """
    Test suite for the ShapeResizer step in the preprocessing pipeline.

    This class verifies that images are correctly resized to a desired shape,
    ensuring accuracy for both RGB and grayscale images.

    Attributes
    ----------
    TestStep : type
        The preprocessing step class being tested (`steps.ShapeResizer`).
    parameters : dict
        Dictionary of parameters for `ShapeResizer`.
    """

    TestStep = steps.ShapeResizer
    parameters = {"desired_shape": (200, 300), "resize_method": "nearest"}

    if not ENABLE_VISUAL_INSPECTION:

        @skip("Visual inspection not enabled")
        def test_processed_image_visualization(self):
            pass

    def _verify_image_shapes(
        self, processed_dataset, original_dataset, color_channel_expected
    ):
        """
        Verify image dimensions and color channels in the processed dataset.

        Compares processed images to the original dataset to ensure resizing
        modifies height and width according to the expected values while
        maintaining the correct number of color channels.

        Parameters
        ----------
        processed_dataset : list
            List of processed images.
        original_dataset : list
            List of original images before processing.
        color_channel_expected : int
            Expected number of color channels in the processed images.
        """
        for original_image, processed_image in zip(
            original_dataset, processed_dataset
        ):
            processed_shape = tuple(processed_image.shape[:2].as_list())
            original_shape = tuple(original_image.shape[:2].as_list())
            self.assertNotEqual(processed_shape, original_shape)
            self.assertEqual(
                color_channel_expected,
                processed_image.shape[2],
                "Color channels are not equal.",
            )
            self.assertEqual(
                self.parameters["desired_shape"][0],
                processed_shape[0],
                "Heights do not match the desired shape.",
            )
            self.assertEqual(
                self.parameters["desired_shape"][1],
                processed_shape[1],
                "Widths do not match the desired shape.",
            )


def load_resize_operations_steps_tests():
    """
    Load and aggregate test suites for resize operations preprocessing steps.

    This function loads test cases for resize operations and combines them
    into a single comprehensive test suite.

    Returns
    -------
    unittest.TestSuite
        A combined test suite containing tests for multiple preprocessing steps.
    """
    loader = unittest.TestLoader()
    test_suites = [
        loader.loadTestsFromTestCase(TestSquareShapePadder),
        loader.loadTestsFromTestCase(TestShapeResizer),
    ]
    test_suite = unittest.TestSuite(test_suites)  # Combine the suites
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(load_resize_operations_steps_tests())
