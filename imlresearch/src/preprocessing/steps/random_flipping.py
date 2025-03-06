import random

import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class RandomFlipper(StepBase):
    """
    A data augmentation step that flips the image randomly in a specified
    direction.

    The direction of the flip can be 'horizontal', 'vertical', or 'both'.
    A random decision is made for whether the flip is applied or not.
    """

    arguments_datatype = {"flip_direction": str, "seed": int}
    name = "Random Flipper"

    def __init__(self, flip_direction="horizontal", seed=42):
        """
        Initialize the RandomFlipper for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        flip_direction : str, optional
            Direction of the potential flip. Can be 'horizontal', 'vertical',
            or 'both'. Default is 'horizontal'.
        seed : int, optional
            Random seed for reproducible flipping. Default is 42.
        """
        super().__init__(locals())
        if flip_direction not in ["horizontal", "vertical", "both"]:
            raise ValueError(
                "flip_direction must be 'horizontal', 'vertical', or 'both'."
            )
        self.seed = seed

    def _setup(self, dataset):
        """
        Set up the RandomFlipper with a fixed random seed for reproducibility.

        Parameters
        ----------
        dataset : Any
            The dataset being processed.

        Returns
        -------
        Any
            The result of the superclass setup method.
        """
        random.seed(self.seed)
        return super()._setup(dataset)

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Flip the image randomly in the specified direction.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The flipped image if the random flip is applied, otherwise the
            original image.
        """
        flip_direction = self.parameters["flip_direction"]
        do_flip = random.choice([True, False])

        if do_flip:
            if flip_direction == "horizontal":
                flipped_image = cv2.flip(image_nparray, 1)  # Flip horizontally
            elif flip_direction == "vertical":
                flipped_image = cv2.flip(image_nparray, 0)  # Flip vertically
            elif flip_direction == "both":
                flipped_image = cv2.flip(image_nparray, -1)  # Flip both ways
        else:
            flipped_image = image_nparray  # No flip applied

        return flipped_image


if __name__ == "__main__":
    step = RandomFlipper()
    print(step.get_step_json_representation())
