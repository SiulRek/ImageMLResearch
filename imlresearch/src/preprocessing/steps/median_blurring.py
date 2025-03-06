import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class MedianBlurFilter(StepBase):
    """
    A preprocessing step that applies a median filter to an image.

    This filter reduces noise by replacing each pixel's value with the
    median of neighboring pixels defined by a kernel.
    """

    arguments_datatype = {"kernel_size": int}
    name = "Median Blur Filter"

    def __init__(self, kernel_size=5):
        """
        Initialize the `MedianBlurFilter` for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        kernel_size : int, optional
            The size of the kernel. It must be an odd and positive integer.
            Default is 5.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply a median blur filter to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The filtered image.
        """
        ksize = self.parameters["kernel_size"]
        blurred_image = cv2.medianBlur(image_nparray, ksize)
        return blurred_image


if __name__ == "__main__":
    step = MedianBlurFilter()
    print(step.get_step_json_representation)
