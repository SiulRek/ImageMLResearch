import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class AdaptiveThresholder(StepBase):
    """
    A preprocessing step that applies adaptive thresholding to an image.

    This method dynamically determines threshold values for different regions
    of the image. For RGB images, each color channel (Red, Green, Blue) is
    processed separately.
    """

    arguments_datatype = {"block_size": int, "c": float, "max_val": float}
    name = "Adaptive Thresholding"

    def __init__(self, block_size=15, c=-2, max_val=255):
        """
        Initialize the AdaptiveThresholder for use in an image preprocessing
        pipeline.

        Parameters
        ----------
        block_size : int, optional
            The size of the pixel neighborhood used to calculate the threshold
            value. Must be an odd number. Default is 15.
        c : float, optional
            A constant subtracted from the mean or weighted mean. Default is -2.
        max_val : float, optional
            The maximum pixel intensity value after thresholding.
            Default is 255.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply adaptive thresholding to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The thresholded image.
        """
        def apply_adaptive_threshold(np_array):
            return cv2.adaptiveThreshold(
                np_array,
                maxValue=self.parameters["max_val"],
                adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                thresholdType=cv2.THRESH_BINARY,
                blockSize=self.parameters["block_size"],
                C=self.parameters["c"],
            )

        if image_nparray.shape[2] == 1:
            return apply_adaptive_threshold(image_nparray)

        R, G, B = cv2.split(image_nparray)
        R_thresh = apply_adaptive_threshold(R)
        G_thresh = apply_adaptive_threshold(G)
        B_thresh = apply_adaptive_threshold(B)

        return cv2.merge([R_thresh, G_thresh, B_thresh])


if __name__ == "__main__":
    step = AdaptiveThresholder()
    print(step.get_step_json_representation())
