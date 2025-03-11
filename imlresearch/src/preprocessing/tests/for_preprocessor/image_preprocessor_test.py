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
        blurred_image = cv2.GaussianBlur(image_nparray, ksize=(5, 5), sigmaX=2)
        blurred_image = tf.convert_to_tensor(blurred_image, dtype=tf.uint8)
        image_grayscale_tensor = tf.image.rgb_to_grayscale(blurred_image)
        image_grayscale_tensor = correct_image_tensor_shape(
            image_grayscale_tensor
        )
        processed_image_nparray = (image_grayscale_tensor.numpy()).astype(
            "uint8"
        )
        return processed_image_nparray


class ErrorStep(StepBase):
    name = "ErrorStep"

    def __init__(self):
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        processed_image = cv2.GaussianBlur(
            image_nparray, sigmaX=2
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
        if cls.visual_inspection and not os.path.isdir(
            cls.step_visualization_dir
        ):
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
        """
        Tests the functionality of popping and appending steps in the image
        preprocessing pipeline.

        This test case first populates the pipeline with specific steps, then
        pops the last step, and finally appends it back. It verifies both the
        popped step and the integrity of the pipeline after these operations.
        """
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
        """
        Tests the functionality of clearing and reinitializing the image
        preprocessing pipeline.

        This test case verifies that the `pipe_clear` method of the
        ImagePreprocessor class effectively clears the existing pipeline and
        allows to rebuild the pipeline from start.
        """
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
        preprocessor.pipe_clear()
        self.assertEqual(preprocessor.pipeline, [])
        preprocessor.set_pipe(pipeline)
        self.assertEqual(preprocessor.pipeline, pipeline)

    def test_deepcopy_of_pipeline(self):
        """
        This test ensures that the ImagePreprocessor maintains a consistent and
        isolated state of its preprocessing pipeline.

        Assert is equal implies, that the internal pipeline was successfully
        deep-copied.
        """
        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        ]
        pipeline_expected = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        ]
        preprocessor = ImagePreprocessor(raise_step_process_exception=False)
        preprocessor.set_pipe(pipeline)
        pipeline.append(
            "Changing pipeline by appending invalid element to it."
        )
        self.assertEqual(preprocessor.pipeline, pipeline_expected)

    def test_image_preprocessor_equality(self):
        """ Test the equality operator for the ImagePreprocessor class. """
        preprocessor1 = ImagePreprocessor()
        preprocessor2 = ImagePreprocessor()

        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        ]

        preprocessor1.set_pipe(pipeline)
        preprocessor2.set_pipe(pipeline)

        self.assertEqual(
            preprocessor1, preprocessor2, "The preprocessors should be equal."
        )

        preprocessor2.pipe_append(
            RGBToGrayscale(param1=50, param2=(50, 50), param3=True)
        )

        self.assertNotEqual(
            preprocessor1,
            preprocessor2,
            "The preprocessors should not be equal after modifying one of them."
        )

        self.assertNotEqual(
            preprocessor1,
            "Not an ImagePreprocessor",
            "The preprocessor should not be equal to an unrelated type.",
        )

    def test_invalid_step_in_pipeline(self):
        """
        Tests the ImagePreprocessor's ability to validate the types of steps
        added to its pipeline.

        This test ensures that the ImagePreprocessor class correctly identifies
        and rejects any objects added to its pipeline that are not a subclass
        of StepBase.
        """

        class StepNotOfStepBase:
            pass

        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            StepNotOfStepBase,
        ]
        with self.assertRaises(ValueError):
            preprocessor = ImagePreprocessor()
            preprocessor.set_pipe(pipeline)

    def _remove_new_lines_and_spaces(self, string):
        string = string.replace("\n", "")
        string = string.replace(" ", "")
        return string

    def test_pipeline_code_representation(self):
        """ Tests ensures the correctness of the pipeline code representation
        generated by the ImagePreprocessor. """
        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3="a nice str"),
        ]
        representation_expected = """[
        RGBToGrayscale(param1=20,param2=(20,20),param3=False),
        GrayscaleToRGB(param1=40, param2=(30,30),param3='a nice str')
        ]"""
        preprocessor = ImagePreprocessor(raise_step_process_exception=False)
        preprocessor.set_pipe(pipeline)
        representation_output = preprocessor.get_pipe_code_representation()
        representation_output = self._remove_new_lines_and_spaces(
            representation_output
        )
        representation_expected = self._remove_new_lines_and_spaces(
            representation_expected
        )
        self.assertEqual(representation_output, representation_expected)

    def test_process_pipeline(self):
        """
        Tests the functionality of the image preprocessing pipeline.

        This test case validates that the pipeline, when applied to an image
        dataset, correctly processes images through multiple preprocessing
        steps and maintains the integrity of the images' shape, specifically
        ensuring the color channel conversion was done and the dimension is
        correct after processing.
        """
        preprocessor = ImagePreprocessor()
        preprocessor.set_pipe(self.pipeline)
        processed_images = preprocessor.process(self.image_dataset)
        self._verify_image_shapes(
            processed_images, self.image_dataset, color_channel_expected=1
        )

    def test_process_pipeline_for_packed_dataset(self):
        """
        Tests the functionality of the image preprocessing pipeline for packed
        datasets.

        This test case validates that the pipeline, when applied to a packed
        dataset, meaning a dataset with both images and labels.
        """
        unpacked_dataset = self.image_dataset
        # The dataset is packed with itself to create a dataset with both images
        # and labels.
        packed_dataset = tf.data.Dataset.zip(
            (unpacked_dataset, unpacked_dataset)
        )

        preprocessor = ImagePreprocessor()
        preprocessor.set_pipe(self.pipeline)
        processed_dataset = preprocessor.process(packed_dataset)

        processed_images, processed_labels = zip(*processed_dataset)

        processed_images = list(processed_images)
        processed_labels = list(processed_labels)
        original_images = list(unpacked_dataset)

        self._verify_image_shapes(
            processed_images, original_images, color_channel_expected=1
        )

        # Check if the labels are not modified.
        self._verify_image_shapes(
            processed_labels, original_images, color_channel_expected=3
        )

    def test_set_default_datatype(self):
        """
        Test the functionality of the set_default_datatype method. This test
        changes the default output datatype and verifies if the processed
        images are in the new datatype.
        """
        preprocessor = ImagePreprocessor()
        preprocessor.set_default_datatype(tf.float32)
        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            GrayscaleToRGB(param1=40, param2=(30, 30), param3=False),
        ]
        preprocessor.set_pipe(pipeline)
        processed_dataset = preprocessor.process(self.image_dataset)

        for image in processed_dataset.take(1):
            self.assertEqual(
                image.dtype,
                tf.float32,
                "The datatype of the processed image does not match the "
                "expected default datatype.",
            )

    def test_set_default_datatype_invalid(self):
        preprocessor = ImagePreprocessor()
        with self.assertRaises(TypeError):
            preprocessor.set_default_datatype(int)

    def test_save_and_load_pipeline(self):
        """
        Ensures the image preprocessing pipeline can be saved and subsequently
        loaded.

        This test case checks the pipeline's persistence mechanism, verifying
        that the pipeline can be serialized to JSON and reloaded to create an
        identical pipeline setup.
        """

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
            "Pipeline lengths are not equal.",
        )
        for old_step, new_step in zip(
            old_preprocessor.pipeline, new_preprocessor.pipeline
        ):
            self.assertEqual(
                old_step, new_step, "Pipeline steps are not equal."
            )

        processed_images = new_preprocessor.process(self.image_dataset)
        self._verify_image_shapes(
            processed_images, self.image_dataset, color_channel_expected=1
        )

    def test_load_randomized_pipeline(self):
        """
        Tests loading a pipeline with randomized settings from a JSON file.

        Ensures that the pipeline correctly uses random parameters for its
        steps as defined in the JSON file.
        """

        mock_class_parameters = {
            "param1": {"distribution": "uniform", "low": 2, "high": 10},
            "param2": "[(3,3)]*10 + [(5,5)]*10 + [(8,8)]",
            "param3": [True, True],
        }
        json_data = {
            "RGB_to_Grayscale": mock_class_parameters,
            "Grayscale_to_RGB": mock_class_parameters,
        }

        with open(self.json_test_file, "w", encoding="utf-8") as file:
            json.dump(json_data, file)

        mock_mapping = {
            "RGB_to_Grayscale": RGBToGrayscale,
            "Grayscale_to_RGB": GrayscaleToRGB,
        }
        with patch(
            "imlresearch.src.preprocessing.image_preprocessor.STEP_CLASS_MAPPING",
            mock_mapping,
        ):
            preprocessor = ImagePreprocessor()
            preprocessor.load_randomized_pipe_from_json(self.json_test_file)
            pipeline = preprocessor.pipeline

        self.assertIsInstance(pipeline[0], RGBToGrayscale)
        self.assertIsInstance(pipeline[1], GrayscaleToRGB)
        for i in range(2):
            self.assertTrue(2 <= pipeline[i].parameters["param1"] <= 10)
            self.assertIn(
                pipeline[i].parameters["param2"], [(3, 3), (5, 5), (8, 8)]
            )
            self.assertTrue(pipeline[i].parameters["param3"])

    def test_not_raised_step_process_exception_1(self):
        """
        Test case for ensuring that the ErrorStep subclass, when processing an
        image dataset, raises an exception as expected, but the exception is
        caught and handled silently by the ImagePreprocessor pipeline, allowing
        the execution to continue without interruption.
        """

        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            ErrorStep(),
        ]
        preprocessor = ImagePreprocessor(raise_step_process_exception=False)
        preprocessor.set_pipe(pipeline)
        processed_images = preprocessor.process(self.image_dataset)
        self.assertIn(
            "missing required argument 'ksize'",
            preprocessor.occurred_exception_message,
        )
        self.assertIsNone(processed_images)

    def test_not_raised_step_process_exception_2(self):
        """
        Test case for ensuring that when pipeline construction is faulty, when
        processing an image dataset, raises an exception as expected, but the
        exception is caught and handled silently by the ImagePreprocessor
        pipeline, allowing the execution to continue without interruption.
        """

        pipeline = [
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
            RGBToGrayscale(param1=20, param2=(20, 20), param3=False),
        ]
        preprocessor = ImagePreprocessor(raise_step_process_exception=False)
        preprocessor.set_pipe(pipeline)
        processed_images = preprocessor.process(self.image_dataset)
        self.assertIn(
            "An error occurred in step RGB_to_Grayscale",
            preprocessor.occurred_exception_message,
        )
        self.assertIsNone(processed_images)


if __name__ == "__main__":
    unittest.main()
