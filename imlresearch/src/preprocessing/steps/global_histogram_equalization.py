import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class GlobalHistogramEqualizer(StepBase):
    """
    A preprocessing step that applies global histogram equalization to an image.

    This step enhances image contrast by distributing intensity values more
    evenly across the histogram. For RGB images, each color channel (Red, Green,
    Blue) is processed separately.
    """

    arguments_datatype = {}
    name = "Global Histogram Equalizer"

    def __init__(self):
        """
        Initialize the GlobalHistogramEqualizer for use in an image
        preprocessing pipeline.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply global histogram equalization to an input image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The processed image with enhanced contrast.
        """
        channels = cv2.split(image_nparray)
        eq_channels = [cv2.equalizeHist(ch) for ch in channels]
        return cv2.merge(eq_channels)


if __name__ == "__main__":
    step = GlobalHistogramEqualizer()
    print(step.get_step_json_representation())
