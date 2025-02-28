import random

import cv2
import numpy as np

from imlresearch.src.preprocessing.steps.step_base import StepBase


class RandomSharpening(StepBase):
    """ A data augmentation step that applies random sharpening to an image. """

    arguments_datatype = {"min_intensity": float, "max_intensity": float, "seed": int}
    name = "Random Sharpening"

    def __init__(self, min_intensity=0.5, max_intensity=2.0, seed=42):
        """
        Initializes the RandomSharpening object for integration in an image
        preprocessing pipeline.

        Args:
            - min_intensity (float): Minimum intensity of sharpening.
            - max_intensity (float): Maximum intensity of sharpening.
            - seed (int): Random seed for reproducibility. Default is 42.
        """
        super().__init__(locals())

    def _setup(self, dataset):
        random.seed(self.parameters["seed"])
        return super()._setup(dataset)
    
    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        intensity = random.uniform(
            self.parameters["min_intensity"], self.parameters["max_intensity"]
        )

        kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]) * intensity
        kernel[1, 1] += 1

        sharpened_image = cv2.filter2D(image_nparray, -1, kernel)
        sharpened_image = np.clip(sharpened_image, 0, 255)

        return sharpened_image.astype(np.uint8)


if __name__ == "__main__":
    step = RandomSharpening()
    print(step.get_step_json_representation())
