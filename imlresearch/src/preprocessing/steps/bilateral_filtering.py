import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class BilateralFilter(StepBase):
    """A preprocessing step that applies bilateral filter to an image."""

    arguments_datatype = {
        "diameter": int,
        "sigma_color": float,
        "sigma_space": float,
    }
    name = "Bilateral Filter"

    def __init__(self, diameter=9, sigma_color=75, sigma_space=75):
        """
        Initializes the `BilateralFilter` object that can be integrated in
        an image preprocessing pipeline.

        Args:
            - diameter (int): Diameter of each pixel neighborhood used
              during filtering.
            - sigma_color (float): Filter sigma in the color space. Larger
              values mean farther colors mix together.
            - sigma_space (float): Filter sigma in the coordinate space.
              Larger values mean farther pixels influence each other.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        return cv2.bilateralFilter(
            src=image_nparray,
            d=self.parameters["diameter"],
            sigmaColor=self.parameters["sigma_color"],
            sigmaSpace=self.parameters["sigma_space"],
        )


if __name__ == "__main__":
    step = BilateralFilter()
    print(step.get_step_json_representation())
