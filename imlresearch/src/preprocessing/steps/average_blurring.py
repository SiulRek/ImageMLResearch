import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class AverageBlurFilter(StepBase):
    """
    A preprocessing step that applies an average blur filter to an image.

    This filter smooths the image by averaging the pixel values within a
    kernel around each pixel.
    """

    arguments_datatype = {"kernel_size": (int, int)}
    name = "Average Blur Filter"

    def __init__(self, kernel_size=(8, 8)):
        """
        Initialize the `AverageBlurFilter` for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        kernel_size : tuple of int, optional
            The size of the averaging kernel. Both values should be positive
            integers. Default is (8, 8).
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply an average blur filter to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The blurred image.
        """
        ksize = self.parameters["kernel_size"]
        blurred_image = cv2.blur(image_nparray, ksize)
        return blurred_image


if __name__ == "__main__":
    step = AverageBlurFilter()
    print(step.get_step_json_representation())
