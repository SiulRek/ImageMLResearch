import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class GaussianBlurFilter(StepBase):
    """
    A preprocessing step that applies a Gaussian blur filter to an image.

    This step smooths the image by convolving it with a Gaussian function,
    reducing noise and detail.
    """

    arguments_datatype = {"kernel_size": (int, int), "sigma": float}
    name = "Gaussian Blur Filter"

    def __init__(self, kernel_size=(5, 5), sigma=0.3):
        """
        Initialize the GaussianBlurFilter for use in an image preprocessing
        pipeline.

        Parameters
        ----------
        kernel_size : tuple of int, optional
            The size of the Gaussian kernel. Both values should be odd
            numbers. Default is (5, 5).
        sigma : float, optional
            The standard deviation of the Gaussian kernel. A higher sigma
            results in more blur. Default is 0.3.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply a Gaussian blur filter to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The blurred image.
        """
        k = self.parameters["kernel_size"]
        sigma = self.parameters["sigma"]
        return cv2.GaussianBlur(image_nparray, k, sigma)


if __name__ == "__main__":
    step = GaussianBlurFilter()
    print(step.get_step_json_representation())
