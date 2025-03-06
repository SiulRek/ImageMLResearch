import cv2
import numpy as np

from imlresearch.src.preprocessing.steps.step_base import StepBase


class ErosionFilter(StepBase):
    """
    A preprocessing step that applies erosion to an image.

    Erosion reduces the white regions in the image, making objects appear
    smaller.
    """

    arguments_datatype = {"kernel_size": int, "iterations": int}
    name = "Erosion Filter"

    def __init__(self, kernel_size=3, iterations=1):
        """
        Initialize the ErosionFilter for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        kernel_size : int, optional
            The size of the erosion kernel. Default is 3.
        iterations : int, optional
            The number of times the erosion operation is applied. Default is 1.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply erosion to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The eroded image.
        """
        kernel = np.ones(
            (self.parameters["kernel_size"], self.parameters["kernel_size"]),
            np.uint8,
        )
        eroded_image = cv2.erode(
            image_nparray, kernel, iterations=self.parameters["iterations"]
        )
        return eroded_image


if __name__ == "__main__":
    step = ErosionFilter()
    print(step.get_step_json_representation())
