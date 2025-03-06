import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class AdaptiveHistogramEqualizer(StepBase):
    """
    A preprocessing step that applies Contrast Limited Adaptive Histogram
    Equalization (CLAHE) to an image.

    For RGB images, each color channel (Red, Green, Blue) is processed
    separately to enhance contrast.
    """

    arguments_datatype = {"clip_limit": float, "tile_gridsize": (int, int)}
    name = "Adaptive Histogram Equalizer"

    def __init__(self, clip_limit=2.0, tile_gridsize=(8, 8)):
        """
        Initialize the AdaptiveHistogramEqualizer for integration into an
        image preprocessing pipeline.

        Parameters
        ----------
        clip_limit : float, optional
            Threshold for contrast limiting. Higher values increase contrast,
            but too high values may lead to noise amplification. Default is 2.0.
        tile_gridsize : tuple of int, optional
            The size of the grid for the tiles (regions) of the image to which
            CLAHE will be applied. Smaller tiles can lead to more localized
            contrast enhancement. Default is (8, 8).
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply CLAHE to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The image with enhanced contrast using CLAHE.
        """
        channels = cv2.split(image_nparray)
        clahe = cv2.createCLAHE(
            clipLimit=self.parameters["clip_limit"],
            tileGridSize=self.parameters["tile_gridsize"],
        )
        clahe_channels = [clahe.apply(ch) for ch in channels]
        return cv2.merge(clahe_channels)


if __name__ == "__main__":
    step = AdaptiveHistogramEqualizer()
    print(step.get_step_json_representation())
