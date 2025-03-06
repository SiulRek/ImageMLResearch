import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class NLMeanDenoiser(StepBase):
    """
    A preprocessing step that applies Non-Local Mean Denoising to an image.

    Non-Local Means Denoising reduces noise in an image by averaging pixels
    with similar neighborhood patterns across the image.
    """

    arguments_datatype = {
        "h": float,
        "template_window_size": int,
        "search_window_size": int,
    }
    name = "Non Local Mean Denoiser"

    def __init__(self, h=1.0, template_window_size=7, search_window_size=21):
        """
        Initialize the NLMeanDenoiser for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        h : float, optional
            Filter strength. Higher values remove noise better but may also
            remove image details. Default is 1.0.
        template_window_size : int, optional
            Odd size of the window used to compute the weighted average for
            the given pixel. Default is 7.
        search_window_size : int, optional
            Odd size of the window used to search for patches similar to the
            one centered at the current pixel. Default is 21.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply Non-Local Mean Denoising to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The denoised image.
        """
        return cv2.fastNlMeansDenoising(
            src=image_nparray,
            h=self.parameters["h"],
            templateWindowSize=self.parameters["template_window_size"],
            searchWindowSize=self.parameters["search_window_size"],
        )


if __name__ == "__main__":
    step = NLMeanDenoiser()
    print(step.get_step_json_representation())
