import unittest
from unittest.mock import MagicMock

import cv2
import tensorflow as tf

from imlresearch.src.preprocessing.helpers.step_utils import (
    correct_image_tensor_shape,
)
from imlresearch.src.preprocessing.steps.step_base import StepBase
from imlresearch.src.testing.bases.base_test_case import BaseTestCase


class TfTestStep(StepBase):
    arguments_datatype = {"param1": int, "param2": (int, int), "param3": bool}
    name = "Test_Step"

    def __init__(self, param1=10, param2=(10, 10), param3=True):
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        image_grayscale_tensor = tf.image.rgb_to_grayscale(image_tensor)
        image_grayscale_tensor = correct_image_tensor_shape(
            image_grayscale_tensor
        )
        return image_grayscale_tensor


class PyTestStep(StepBase):
    arguments_datatype = {"param1": int, "param2": (int, int), "param3": bool}
    name = "Test_Step"

    def __init__(self, param1=10, param2=(10, 10), param3=True):
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        blurred_image = cv2.GaussianBlur(
            image_nparray, ksize=(5, 5), sigmaX=2
        )
        blurred_image_tensor = tf.convert_to_tensor(
            blurred_image, dtype=tf.uint8
        )
        image_grayscale_tensor = tf.image.rgb_to_grayscale(
            blurred_image_tensor
        )
        processed_img = (image_grayscale_tensor.numpy()).astype("uint8")
        return processed_img


class TestStepBase(BaseTestCase):
    """
    Test suite for validating the functionality of the preprocessing steps
    parent class `StepBase` in the image preprocessing module.

    This test suite validates the `StepBase` class, focusing on the correct
    initialization and functionality of both TensorFlow and Python-based
    preprocessing steps. It tests image shape transformations, object equality,
    JSON representation, wrapper functions for processing image data, and
    datatype handling.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.image_dataset = cls.load_geometrical_forms_dataset()

    def setUp(self):
        super().setUp()
        self.local_vars = {"param1": 10, "param2": (10, 10), "param3": True}
        self.tf_preprocessing_step = TfTestStep(**self.local_vars)
        self.py_preprocessing_step = PyTestStep(**self.local_vars)

    def _verify_image_shapes(
        self, processed_images, original_images, color_channel_expected
    ):
        for original_image, processed_image in zip(
            original_images, processed_images
        ):
            self.assertEqual(
                processed_image.shape[:1], original_image.shape[:1]
            )
            self.assertEqual(color_channel_expected, processed_image.shape[2])

    def test_initialization(self):
        self.assertEqual(self.tf_preprocessing_step.name, "Test_Step")
        self.assertEqual(
            self.tf_preprocessing_step.parameters,
            {"param1": 10, "param2": (10, 10), "param3": True},
        )

    def test_correct_shape_gray(self):
        image_tensor = list(TestStepBase.image_dataset.take(1))[0]
        image_grayscale_tensor = tf.image.rgb_to_grayscale(image_tensor)
        reshaped_image = correct_image_tensor_shape(image_grayscale_tensor)
        self.assertEqual(reshaped_image.shape, image_tensor.shape[:2] + [1])

    def test_correct_shape_rgb(self):
        image_tensor = list(TestStepBase.image_dataset.take(1))[0]
        image_grayscale_tensor = tf.image.rgb_to_grayscale(image_tensor)
        image_rgb_tensor = tf.image.grayscale_to_rgb(image_grayscale_tensor)
        reshaped_image = correct_image_tensor_shape(image_rgb_tensor)
        self.assertEqual(reshaped_image.shape, image_tensor.shape)

    def _remove_new_lines_and_spaces(self, string):
        return string.replace("\n", "").replace(" ", "")

    def test_get_step_json_representation(self):
        json_repr_output = self.tf_preprocessing_step.get_step_json_representation()  # noqa
        json_repr_expected = (
            '"Test_Step": {"param1": 10, "param2": [10,10], "param3": true}'
        )
        json_repr_output = self._remove_new_lines_and_spaces(json_repr_output)
        json_repr_expected = self._remove_new_lines_and_spaces(
            json_repr_expected
        )
        self.assertEqual(json_repr_output, json_repr_expected)

    def test_tensor_pyfunc_wrapper(self):
        processed_dataset = self.tf_preprocessing_step(self.image_dataset)
        self._verify_image_shapes(processed_dataset, self.image_dataset, 1)

    def test_nparray_pyfunc_wrapper(self):
        processed_dataset = self.py_preprocessing_step(self.image_dataset)
        self._verify_image_shapes(processed_dataset, self.image_dataset, 1)

    def test__setup_called(self):
        self.tf_preprocessing_step._setup = MagicMock()
        self.tf_preprocessing_step(self.image_dataset)
        self.tf_preprocessing_step._setup.assert_called_once()

        self.py_preprocessing_step._setup = MagicMock()
        self.py_preprocessing_step(self.image_dataset)
        self.py_preprocessing_step._setup.assert_called_once()

    def test_output_datatype_conversion(self):
        self.py_preprocessing_step.output_datatype = tf.uint8
        processed_dataset = self.py_preprocessing_step(self.image_dataset)
        for img in processed_dataset.take(1):
            self.assertEqual(img.dtype, tf.uint8)

        self.py_preprocessing_step.output_datatype = tf.float16
        processed_dataset = self.py_preprocessing_step(self.image_dataset)
        for img in processed_dataset.take(1):
            self.assertEqual(img.dtype, tf.float16)

    def test_output_datatype_default(self):
        image_datatype_kept = StepBase.default_output_datatype
        StepBase.default_output_datatype = tf.uint8

        tf_preprocessing_step = TfTestStep(**self.local_vars)
        processed_dataset = tf_preprocessing_step(self.image_dataset)
        for img in processed_dataset.take(1):
            self.assertEqual(img.dtype, tf.uint8)

        StepBase.default_output_datatype = tf.float16
        tf_preprocessing_step = TfTestStep(**self.local_vars)
        processed_dataset = tf_preprocessing_step(self.image_dataset)
        for img in processed_dataset.take(1):
            self.assertEqual(img.dtype, tf.float16)

        # Ensure `default_output_datatype` remains unchanged
        tf_preprocessing_step.output_datatype = tf.uint8
        self.assertEqual(StepBase.default_output_datatype, tf.float16)

        StepBase.default_output_datatype = image_datatype_kept

    def test_equal_objects(self):
        self.assertEqual(
            self.py_preprocessing_step, self.tf_preprocessing_step
        )

    def test_not_equal_objects(self):
        local_vars = {"param1": 20, "param2": (20, 20), "param3": False}
        tf_preprocessing_step = TfTestStep(**local_vars)
        self.assertNotEqual(self.py_preprocessing_step, tf_preprocessing_step)


if __name__ == "__main__":
    unittest.main()
