import cv2
import numpy as np

from imlresearch.src.preprocessing.steps.step_base import StepBase


class DilationFilter(StepBase):
    """
    A preprocessing step that applies dilation to an image.

    Dilation enlarges the white regions of the image, making objects
    appear larger.
    """

    arguments_datatype = {"kernel_size": int, "iterations": int}
    name = "Dilation Filter"

    def __init__(self, kernel_size=3, iterations=1):
        """
        Initialize the DilationFilter for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        kernel_size : int, optional
            The size of the dilation kernel. Default is 3.
        iterations : int, optional
            The number of times the dilation operation is applied. Default is 1.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply dilation to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The dilated image.
        """
        kernel = np.ones(
            (self.parameters["kernel_size"], self.parameters["kernel_size"]),
            np.uint8,
        )
        dilated_image = cv2.dilate(
            image_nparray, kernel, iterations=self.parameters["iterations"]
        )
        return dilated_image


if __name__ == "__main__":
    step = DilationFilter()
    print(step.get_step_json_representation())
