import json
import os
import unittest
from unittest.mock import patch

import cv2
import tensorflow as tf

from imlresearch.src.preprocessing.helpers.step_utils import (
    correct_image_tensor_shape,
)
from imlresearch.src.preprocessing.image_preprocessor import ImagePreprocessor
from imlresearch.src.preprocessing.steps.step_base import StepBase
from imlresearch.src.testing.bases.base_test_case import BaseTestCase

ENABLE_VISUAL_INSPECTION = True
JSON_TEMPLATE_REL = os.path.join(
    "imlresearch/src/preprocessing/definitions/pipeline_template.json"
)


class GrayscaleToRGB(StepBase):
    arguments_datatype = {"param1": int, "param2": (int, int), "param3": bool}
    name = "Grayscale_to_RGB"

    def __init__(self, param1=10, param2=(10, 10), param3=True):
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        image_rgb_tensor = tf.image.grayscale_to_rgb(image_tensor)
        image_rgb_tensor = correct_image_tensor_shape(image_rgb_tensor)
        return image_rgb_tensor


class RGBToGrayscale(StepBase):
    arguments_datatype = {"param1": int, "param2": (int, int), "param3": bool}
    name = "RGB_to_Grayscale"

    def __init__(self, param1=10, param2=(10, 10), param3=True):
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        blurred_image = cv2.GaussianBlur(
            image_nparray, ksize=(5, 5), sigmaX=2
        )
        blurred_image = tf.convert_to_tensor(blurred_image, dtype=tf.uint8)
        image_grayscale_tensor = tf.image.rgb_to_grayscale(blurred_image)
        image_grayscale_tensor = correct_image_tensor_shape(
            image_grayscale_tensor
        )
        processed_image_nparray = (
            image_grayscale_tensor.numpy()
        ).astype("uint8")
        return processed_image_nparray


class ErrorStep(StepBase):
    name = "ErrorStep"

    def __init__(self):
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        processed_image = cv2.GaussianBlur(
            image_nparray, oops_unknown_parameter_here="sorry"
        )
        return processed_image


class TestImagePreprocessor(BaseTestCase):
    """
    Test suite for evaluating the `ImagePreprocessor` class functionality.

    This suite includes a variety of tests to ensure the proper functioning of
    the pipeline operations handled by the `ImagePreprocessor`, such as adding
    and removing steps, validating pipeline execution, and handling exceptions.
    It tests maintaining consistent image shapes and processing images through
    multiple preprocessing steps.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.json_template = os.path.join(cls.root_dir, JSON_TEMPLATE_REL)
        cls.image_dataset = cls.load_geometrical_forms_dataset()
        cls.visual_inspection = ENABLE_VISUAL_INSPECTION
        cls.step_visualization_dir = os.path.join(
            cls.visualizations_dir, "image_preprocessor"
        )
        if cls.visual_inspection and not os.path.isdir(cls.step_visualization_dir):
            os.makedirs(cls.step_visualization_dir)

    def setUp(self):
        super().setUp()
        self.json_test_file = os.path.join(self.temp_dir, "test_pipeline.json")
        with open(self.json_test_file, "a", encoding="utf-8"):
            pass
        self.pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
            RGBToGrayscale(param1=30, param2=(10, 10), param3=True),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
            RGBToGrayscale(param1=30, param2=(10, 10), param3=False),
        ]

    def tearDown(self):
        super().tearDown()
        if os.path.exists(self.json_test_file):
            os.remove(self.json_test_file)

    def _verify_image_shapes(
        self, processed_images, original_images, color_channel_expected
    ):
        for original, processed in zip(original_images, processed_images):
            self.assertEqual(processed.shape[:1], original.shape[:1])
            self.assertEqual(color_channel_expected, processed.shape[2])

    def test_pipe_pop_and_append(self):
        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        ]
        preprocessor = ImagePreprocessor(raise_step_process_exception=False)
        preprocessor.set_pipe(pipeline)
        popped_step = preprocessor.pipe_pop()

        self.assertEqual(
            popped_step,
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        )
        self.assertEqual(preprocessor.pipeline, pipeline[:1])

        preprocessor.pipe_append(popped_step)
        self.assertEqual(preprocessor.pipeline, pipeline)

    def test_pipeline_clear(self):
        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        ]
        preprocessor = ImagePreprocessor()
        preprocessor.set_pipe(pipeline)
        preprocessor.pipe_clear()
        self.assertEqual(preprocessor.pipeline, [])

        preprocessor.pipe_append(pipeline[0])
        preprocessor.pipe_append(pipeline[1])
        self.assertEqual(preprocessor.pipeline, pipeline)

    def test_process_pipeline(self):
        preprocessor = ImagePreprocessor()
        preprocessor.set_pipe(self.pipeline)
        processed_images = preprocessor.process(self.image_dataset)
        self._verify_image_shapes(
            processed_images, self.image_dataset, color_channel_expected=1
        )

    def test_set_default_datatype(self):
        preprocessor = ImagePreprocessor()
        preprocessor.set_default_datatype(tf.float32)
        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        ]
        preprocessor.set_pipe(pipeline)
        processed_dataset = preprocessor.process(self.image_dataset)

        for image in processed_dataset.take(1):
            self.assertEqual(image.dtype, tf.float32)

    def test_save_and_load_pipeline(self):
        mock_mapping = {
            "RGB_to_Grayscale": RGBToGrayscale,
            "Grayscale_to_RGB": GrayscaleToRGB,
        }
        with patch(
            "imlresearch.src.preprocessing.image_preprocessor.STEP_CLASS_MAPPING",
            mock_mapping,
        ):
            old_preprocessor = ImagePreprocessor()
            old_preprocessor.set_pipe(self.pipeline)
            old_preprocessor.save_pipe_to_json(self.json_test_file)
            new_preprocessor = ImagePreprocessor()
            new_preprocessor.load_pipe_from_json(self.json_test_file)

        self.assertEqual(
            len(old_preprocessor.pipeline),
            len(new_preprocessor.pipeline),
        )
        for old_step, new_step in zip(
            old_preprocessor.pipeline, new_preprocessor.pipeline
        ):
            self.assertEqual(old_step, new_step)

        processed_images = new_preprocessor.process(self.image_dataset)
        self._verify_image_shapes(
            processed_images, self.image_dataset, color_channel_expected=1
        )


if __name__ == "__main__":
    unittest.main()
