import random

import cv2
import numpy as np
import tensorflow as tf

from imlresearch.src.preprocessing.helpers.step_utils import (
    correct_image_tensor_shape,
)
from imlresearch.src.preprocessing.steps.step_base import StepBase


class RandomPerspectiveTransformer(StepBase):
    """
    A preprocessing step that applies a perspective transformation to an
    image tensor.

    This transformation simulates a change in viewpoint by warping the
    image using randomly perturbed corner points.
    """

    arguments_datatype = {"warp_scale": float, "seed": int}
    name = "Random Perspective Transformer"

    def __init__(self, warp_scale=0.2, seed=None):
        """
        Initialize the RandomPerspectiveTransformer for integration into an
        image preprocessing pipeline.

        Parameters
        ----------
        warp_scale : float, optional
            Factor to scale the maximum warp intensity, determining the
            extent of perspective distortion. Default is 0.2.
        seed : int, optional
            Random seed for reproducibility. Default is None.
        """
        super().__init__(locals())

    def _setup(self, dataset):
        """
        Set up the transformer with a fixed random seed for reproducibility.

        Parameters
        ----------
        dataset : Any
            The dataset being processed.

        Returns
        -------
        Any
            The result of the superclass setup method.
        """
        random.seed(self.parameters["seed"])
        return super()._setup(dataset)

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply a random perspective transformation to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        tf.Tensor
            The transformed image tensor with corrected shape.
        """
        height, width, _ = image_nparray.shape
        warp_intensity = int(
            min(height, width) * self.parameters["warp_scale"]
        )

        src_points = np.float32(
            [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]]
        )

        def random_point(x, y):
            return [
                x - random.randint(-warp_intensity, warp_intensity),
                y - random.randint(-warp_intensity, warp_intensity),
            ]

        dst_points = np.float32(
            [
                random_point(0, 0),
                random_point(width - 1, 0),
                random_point(0, height - 1),
                random_point(width - 1, height - 1),
            ]
        )

        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        warped_image = cv2.warpPerspective(
            image_nparray, matrix, (width, height)
        )

        image_tensor = tf.convert_to_tensor(
            warped_image, dtype=self.output_datatype
        )

        return correct_image_tensor_shape(image_tensor)


if __name__ == "__main__":
    step = RandomPerspectiveTransformer()
    print(step.get_step_json_representation())
