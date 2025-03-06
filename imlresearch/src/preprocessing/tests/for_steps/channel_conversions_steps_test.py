""" This module provides test suites for the RGBToGrayscale and GrayscaleToRGB
preprocessing steps within an image preprocessing pipeline. """

import unittest
from unittest import skip

from imlresearch.src.preprocessing.image_preprocessor import ImagePreprocessor
from imlresearch.src.preprocessing.steps import GrayscaleToRGB
from imlresearch.src.preprocessing.steps import RGBToGrayscale
from imlresearch.src.preprocessing.tests.for_steps.single_step_test import (
    TestSingleStep,
)

ENABLE_VISUAL_INSPECTION = True


class TestRGBToGrayscale(TestSingleStep):
    """
    A test suite for verifying the functionality of the `RGBToGrayscale`
    preprocessing step.

    This class inherits from `TestSingleStep` and overrides specific tests as
    the expected behaviour is slightly different compared to general steps, due
    to the channel conversion. The `TestSingleStep` class focuses on ensuring
    the correct functioning of these steps, both in isolation and when
    integrated into a pipeline.
    """

    parameters = {}
    TestStep = RGBToGrayscale
    process_grayscale_only = False

    def test_process_rgb_images(self):
        """
        Test to verify that RGB images are correctly processed into grayscale
        images. Ensures that the color channel is correctly transformed from
        RGB to grayscale.

        """
        pipeline = [self.test_step]
        preprocessor = ImagePreprocessor()
        preprocessor.set_pipe(pipeline)
        processed_dataset = preprocessor.process(self.image_dataset)
        self._verify_image_shapes(
            processed_dataset, self.image_dataset, color_channel_expected=1
        )

    if not ENABLE_VISUAL_INSPECTION:

        @skip("Visual inspection not enabled")
        def test_processed_image_visualization(self):
            """
            Skips the visualization test if visual inspection is disabled.
            """
            pass


class TestGrayscaleToRGB(TestSingleStep):
    """
    A test suite for verifying the functionality of the `GrayscaleToRGB`
    preprocessing step.

    This class inherits from `TestSingleStep` and overrides specific tests as
    the expected behaviour is slightly different compared to general steps, due
    to the channel conversion. The `TestSingleStep` class focuses on ensuring
    the correct functioning of these steps, both in isolation and when
    integrated into a pipeline. It further evaluates the interoperability of
    `GrayscaleToRGB` with `RGBToGrayscale` to confirm that sequential
    conversions within a pipeline yield expected results.

    Note:
        - The suite depends on `RGBToGrayscale` for full pipeline testing.
    """

    parameters = {}
    TestStep = GrayscaleToRGB
    process_grayscale_only = False

    def test_process_rgb_images(self):
        """
        Test to verify that RGB images are correctly processed into grayscale
        images within a pipeline. This test ensures the correct color channel
        dimensions after processing.

        """
        pipeline = [self.test_step, RGBToGrayscale()]
        preprocessor = ImagePreprocessor()
        preprocessor.set_pipe(pipeline)
        processed_dataset = preprocessor.process(self.image_dataset)
        self._verify_image_shapes(
            processed_dataset, self.image_dataset, color_channel_expected=1
        )

    def test_process_grayscaled_images(self):
        """
        Test to verify that grayscale images are processed correctly and
        converted back to RGB images. Ensures correct color channel dimensions
        and pipeline behavior.

        """
        pipeline = [RGBToGrayscale(), self.test_step]
        preprocessor = ImagePreprocessor()
        preprocessor.set_pipe(pipeline)
        processed_dataset = preprocessor.process(self.image_dataset)
        self._verify_image_shapes(
            processed_dataset, self.image_dataset, color_channel_expected=3
        )
        preprocessor.process(processed_dataset)
        self._verify_image_shapes(
            processed_dataset, self.image_dataset, color_channel_expected=3
        )

    def test_process_execution(self):
        """
        Test to verify that the preprocessing step executes correctly on the
        image dataset, ensuring that the step runs without errors.

        """
        processed_dataset = self.test_step(self.image_dataset)
        for _ in processed_dataset.take(
            1
        ):  # Consumes the dataset to force execution of the step.
            pass

    if not ENABLE_VISUAL_INSPECTION:

        @skip("Visual inspection not enabled")
        def test_processed_image_visualization(self):
            """
            Skips the visualization test if visual inspection is disabled.
            """
            pass


def load_channel_conversion_steps_tests():
    """
    Loads and combines test suites for RGBToGrayscale and GrayscaleToRGB
    preprocessing steps into a single test suite.

    This function specifically creates test suites for testing the
    RGBToGrayscale and GrayscaleToRGB steps in an image preprocessing pipeline.

    Returns
    -------
    unittest.TestSuite
        A unified test suite containing all the test cases from the
        RGBToGrayscale and GrayscaleToRGB test classes.
    """
    loader = unittest.TestLoader()
    suite1 = loader.loadTestsFromTestCase(TestRGBToGrayscale)
    suite2 = loader.loadTestsFromTestCase(TestGrayscaleToRGB)
    test_suite = unittest.TestSuite([suite1, suite2])  # Combine the suites
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(load_channel_conversion_steps_tests())
