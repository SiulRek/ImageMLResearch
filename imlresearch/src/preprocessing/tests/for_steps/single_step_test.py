"""
This module contains a suite of tests designed to validate image preprocessing
steps before their integration into an image preprocessing pipeline. Each
preprocessing step must successfully pass all the tests specified in this module
or customized tests to ensure its functionality, compatibility, and reliability
within the pipeline!

Note:
    - Test Adaptability: The module acknowledges that not all tests in
      `TestSingleStep` are universally applicable. Therefore, it accommodates
      the need for customized modifications in test cases to effectively
      challenge and validate the diversity of image preprocessing steps.
"""

import json
import os
import unittest
from unittest.mock import patch

import tensorflow as tf

from imlresearch.src.preprocessing.definitions.step_class_mapping import (
    STEP_CLASS_MAPPING,
)
from imlresearch.src.preprocessing.helpers.recursive_type_conversion import (
    recursive_type_conversion,
)
from imlresearch.src.preprocessing.helpers.step_utils import (
    correct_image_tensor_shape,
)
from imlresearch.src.preprocessing.image_preprocessor import ImagePreprocessor
from imlresearch.src.preprocessing.steps import Rotator as StepToTest
from imlresearch.src.preprocessing.steps.step_base import StepBase
from imlresearch.src.testing.bases.base_test_case import BaseTestCase
from imlresearch.src.testing.helpers.image_plotter import ImagePlotter

# TODO Select Step to test here!
STEP_PARAMETERS = {"angle": 180}

ENABLE_VISUAL_INSPECTION = True
JSON_TEMPLATE_REL = os.path.join(
    "imlresearch/src/preprocessing/definitions/pipeline_template.json"
)


class RGBToGrayscale(StepBase):
    arguments_datatype = {}
    name = "RGB_to_Grayscale"

    def __init__(self):
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        image_grayscale_tensor = tf.image.rgb_to_grayscale(image_tensor)
        image_grayscale_tensor = correct_image_tensor_shape(
            image_grayscale_tensor
        )
        return image_grayscale_tensor


class GrayscaleToRGB(StepBase):
    arguments_datatype = {}
    name = "Grayscale_to_RGB"

    def __init__(self):
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        image_tensor = tf.image.grayscale_to_rgb(image_tensor)
        image_grayscale_tensor = correct_image_tensor_shape(image_tensor)
        return image_grayscale_tensor


class TypeCaster(StepBase):
    """ A preprocessing step that casts an image tensor to a specified data type. """

    arguments_datatype = {"output_dtype": str}
    name = "Type Caster"

    def __init__(self, output_dtype="float16"):
        """
        Initializes the TypeCaster object for integration into an image
        preprocessing pipeline.

        Args:
            - output_dtype (str): The desired data type to cast the image
              tensor to. Must be an attribute in tensorflow. Default is
              'float16'.
        """
        super().__init__(locals())
        self.output_datatype = getattr(tf, output_dtype)

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        return image_tensor


class TestSingleStep(BaseTestCase):
    """
    A unit test class for testing individual image preprocessing steps in to be
    integrated in the image preprocessing framework. The class focuses on
    ensuring the correct functioning of these steps, both in isolation and when
    integrated into a pipeline.
    """

    parameters = STEP_PARAMETERS
    TestStep = StepToTest

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.json_template = os.path.join(cls.root_dir, JSON_TEMPLATE_REL)
        cls.image_dataset = cls.load_geometrical_forms_dataset()
        cls.visual_inspection = ENABLE_VISUAL_INSPECTION
        step_name_edit = cls.TestStep.name.replace(" ", "_").lower()
        cls.step_visualization_dir = os.path.join(
            cls.visualizations_dir, step_name_edit
        )
        if cls.visual_inspection:
            os.makedirs(cls.step_visualization_dir, exist_ok=True)

    def setUp(self):
        super().setUp()
        self.json_test_file = os.path.join(self.temp_dir, "test_step.json")
        with open(self.json_test_file, "a", encoding="utf-8"):
            pass
        self.test_step = self.TestStep(**self.parameters)

    def tearDown(self):
        super().tearDown()
        if os.path.exists(self.json_test_file):
            os.remove(self.json_test_file)

    def _verify_image_shapes(
        self, processed_images, original_images, color_channel_expected
    ):
        """
        Helper method to verify the image dimensions and color channels in a
        processed dataset. Compares the processed images to the original dataset
        to ensure correct height, width, and color channel transformations.
        """
        for original_image, processed_image in zip(
            original_images, processed_images
        ):
            processed_data_shape = tuple(processed_image.shape[:2].as_list())
            original_data_shape = tuple(original_image.shape[:2].as_list())
            self.assertEqual(
                processed_data_shape,
                original_data_shape,
                "heights and/or widths are not equal.",
            )
            self.assertEqual(
                color_channel_expected,
                processed_image.shape[2],
                "Color channels are not equal.",
            )

    def test_arguments_datatype(self):
        """
        Test to verify that the datatype specifications for StepToTest instance
        parameters are correct.
        """
        parameters = self.test_step.parameters
        init_parameters_datatype = self.TestStep.arguments_datatype
        self.assertEqual(
            parameters.keys(),
            init_parameters_datatype.keys(),
            "Keys do not match between datatype specifications and parameters.",
        )
        for key in parameters.keys():
            param_converted = recursive_type_conversion(
                parameters[key], init_parameters_datatype[key]
            )
            self.assertEqual(
                param_converted,
                parameters[key],
                "Datatype specification is incorrect.",
            )

    def test_mapping_entry_of_step(self):
        """
        Test to verify the presence and correctness of the mapping entry for the
        tested preprocessing step.
        """
        step_name = self.test_step.name
        self.assertIn(
            step_name,
            STEP_CLASS_MAPPING.keys(),
            "No mapping is specified for the tested step.",
        )
        self.assertIs(
            STEP_CLASS_MAPPING[step_name],
            self.TestStep,
            "Mapped value of tested step is incorrect.",
        )

    def test_process_execution(self):
        """
        Verifies the execution and efficacy of the preprocessing step on an
        image dataset.
        """
        dtype_str = self.test_step.output_datatype.name
        image_dataset = TypeCaster(dtype_str)(self.image_dataset)
        processed_images = self.test_step(image_dataset)
        for _ in processed_images.take(1):
            pass
        for ori_img, prc_img in zip(image_dataset, processed_images):
            equal_flag = True
            prc_img = tf.cast(prc_img, dtype=ori_img.dtype)
            if ori_img.shape != prc_img.shape:
                equal_flag = False
            elif not tf.reduce_all(tf.equal(ori_img, prc_img)).numpy():
                equal_flag = False
            self.assertFalse(equal_flag)

    def test_output_datatype(self):
        """
        Ensures that the datatype of the images after processing matches the
        expected datatype.
        """
        processed_images = self.test_step(self.image_dataset)
        for image in processed_images:
            self.assertEqual(image.dtype, self.test_step.output_datatype)


if __name__ == "__main__":
    unittest.main()
