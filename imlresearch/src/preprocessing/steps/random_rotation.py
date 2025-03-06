import random

import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class RandomRotator(StepBase):
    """
    A preprocessing step that applies random rotation to an image within a
    specified angle range.

    The rotation angle is randomly chosen from the specified range.
    """

    arguments_datatype = {"angle_range": (int, int), "seed": int}
    name = "Random Rotator"

    def __init__(self, angle_range=(-90, 90), seed=42):
        """
        Initialize the RandomRotator for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        angle_range : tuple of int, optional
            Tuple of two integers specifying the range of angles for rotation.
            For example, (-90, 90) allows rotations between -90 and 90 degrees.
            Default is (-90, 90).
        seed : int, optional
            Random seed for reproducible rotations. Default is 42.
        """
        super().__init__(locals())

    def _setup(self, dataset):
        """
        Set up the RandomRotator with a fixed random seed for reproducibility.

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
        Apply a random rotation to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The rotated image.
        """
        angle = random.randint(*self.parameters["angle_range"])
        height, width = image_nparray.shape[:2]

        rotation_matrix = cv2.getRotationMatrix2D(
            (width / 2, height / 2), angle, 1
        )

        return cv2.warpAffine(image_nparray, rotation_matrix, (width, height))


if __name__ == "__main__":
    step = RandomRotator()
    print(step.get_step_json_representation())
