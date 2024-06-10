"""
This module dynamically creates and manages unittest classes for testing
variuous of the image preprocessing steps, with each class inheriting from
`TestSingleStep`. It utilizes the dynamic class creation in Python to generate
test cases for different preprocessing steps. This module allows additionally
some tests to be skipped based on configuration flags.

Key Components:
    - DynamicTestStep: A class that dynamically generates test cases for
        each specific image preprocessing step.
    - ENABLE_VISUAL_INSPECTION: A flag used to enable or disable tests that
        require visual inspection of processed images.
    - steps_data: A collection of tuples (step_class, arguments,
        visual_inspection_always_disable), representing the different image
        preprocessing steps and their parameters to be tested.

Note:
    - The module accommodates variations in preprocessing steps, recognizing
        that not all test cases in `TestSingleStep` are universally applicable.
        Certain steps may necessitate customized modifications to the standard
        test cases, reflecting the diverse nature of image preprocessing
        challenges.
"""

import re
import unittest
from unittest import skip

import src.preprocessing.steps as steps
from src.preprocessing.tests.for_steps.single_step_test import TestSingleStep

ENABLE_VISUAL_INSPECTION = True


def create_test_class_for_step(
    step_class, arguments, visual_inspection_always_disable=False
):

    class DynamicTestStep(TestSingleStep):
        TestStep = step_class
        parameters = arguments

        if visual_inspection_always_disable:

            @skip("Visual inspection not enabled")
            def test_processed_image_visualization(self):
                pass

        elif not ENABLE_VISUAL_INSPECTION:

            @skip("Visual inspection not enabled")
            def test_processed_image_visualization(self):
                pass

        if isinstance(step_class(), steps.DilateErodeSequencer):

            def test_generate_dilation_and_erosion_sequence(self):
                """
                Tests the erosion probability accuracy in sequences generated by
                the DilateErodeSequencer.

                This test calculates the proportion of erosion operations in a
                long sequence generated by the DilateErodeSequencer. It then
                compares this proportion to the expected erosion probability,
                ensuring that the sequence generation aligns closely with the
                specified probability.
                """
                iterations = 1000  # Large number for statistical significance
                erosion_probability = 0.8
                result_sequence = step_class(**arguments).generate_sequence(
                    "", iterations, erosion_probability
                )
                erosion_count = len(
                    re.findall(r"e", result_sequence)
                )  # Assuming 'e' represents erosion
                # Check if erosion count is approximately 80% of the sequence
                self.assertAlmostEqual(
                    erosion_count / iterations, erosion_probability, delta=0.1
                )

        if isinstance(step_class(), steps.TypeCaster):

            @skip("No value or shape changes are to be expected when Type Casting.")
            def test_process_execution(self):
                pass

        if isinstance(step_class(), steps.DummyStep):

            @skip(
                "No value or shape changes are to be expected when processing Dummy Step."
            )
            def test_process_execution(self):
                pass

    name = step_class.name.replace(" ", "")
    DynamicTestStep.__name__ = f"Test{name}"

    return DynamicTestStep


steps_data = [
    (steps.AdaptiveHistogramEqualizer, {"clip_limit": 1.0, "tile_gridsize": (5, 5)}),
    (steps.GlobalHistogramEqualizer, {}),
    (steps.GaussianBlurFilter, {"kernel_size": (5, 5), "sigma": 2.0}),
    (steps.MedianBlurFilter, {"kernel_size": 5}),
    (steps.BilateralFilter, {"diameter": 9, "sigma_color": 75, "sigma_space": 75}),
    (steps.AverageBlurFilter, {"kernel_size": (8, 8)}),
    (steps.BinaryThresholder, {"thresh": 128}),
    (steps.OstuThresholder, {}),
    (steps.AdaptiveThresholder, {"block_size": 15, "c": -2}),
    (steps.TruncatedThresholder, {"thresh": 128}),
    (steps.ZeroThreshold, {"thresh": 128}),
    (steps.ErosionFilter, {"kernel_size": 3, "iterations": 1}),
    (steps.DilationFilter, {"kernel_size": 3, "iterations": 1}),
    (steps.DilateErodeSequencer, {"kernel_size": 5, "sequence": "ded"}),
    (steps.TypeCaster, {"output_dtype": "float16"}, True),
    (steps.MinMaxNormalizer, {}, True),
    (steps.StandardNormalizer, {}, True),
    (steps.MeanNormalizer, {}, True),
    (
        steps.LocalContrastNormalizer,
        {"depth_radius": 5, "bias": 1.0, "alpha": 0.0001, "beta": 0.75},
        True,
    ),
    (steps.ReverseScaler, {"scale_factor": 255}, True),
    (steps.Mirrorer, {"mirror_direction": "horizontal"}),
    (steps.Rotator, {"angle": 180}),
    (steps.DummyStep, {}),
    (steps.Clipper, {"min_value": 0.0, "max_value": 1.0}),
]


def load_multiple_steps_tests():
    """
    Dynamically loads and aggregates individual test suites for multiple image
    preprocessing steps into a unified test suite.

    This function iterates over a predefined list of image preprocessing steps
    and their corresponding arguments. For each step, it dynamically creates a
    test class using `create_test_class_for_step` and then loads the test cases
    from these classes into individual test suites. These suites are then
    combined into a single comprehensive test suite.

    Returns:
        - unittest.TestSuite: A combined test suite that aggregates tests
            for multiple image preprocessing step test classes.
    """
    test_suites = []
    loader = unittest.TestLoader()
    for step_data in steps_data:
        test_class = create_test_class_for_step(*step_data)
        test_suites.append(loader.loadTestsFromTestCase(test_class))
    test_suite = unittest.TestSuite(test_suites)  # Combine the suites
    return test_suite


if __name__ == "__main__":
    """ Main execution block for running the loaded test suite. """
    runner = unittest.TextTestRunner()
    runner.run(load_multiple_steps_tests())
