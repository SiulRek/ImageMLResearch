import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class TruncatedThresholder(StepBase):
    """
    A preprocessing step that applies truncated thresholding to an image.

    For RGB images, each color channel (Red, Green, Blue) is processed
    separately. Truncated thresholding sets pixel values greater than the
    threshold to the threshold value, leaving values less than or equal to
    the threshold unchanged.
    """

    arguments_datatype = {"thresh": float, "max_val": float}
    name = "Truncated Thresholding"

    def __init__(self, thresh=128, max_val=255):
        """
        Initialize the TruncatedThresholder for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        thresh : float, optional
            The threshold value used for truncated thresholding. Pixel values
            greater than this threshold are set to the threshold value itself,
            and values less than or equal to the threshold remain unchanged.
            Default is 128.
        max_val : float, optional
            The maximum value that a pixel can take after thresholding. Default
            is 255.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply truncated thresholding to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The thresholded image.
        """
        def apply_truncated_threshold(np_array):
            _, thresholded_np_array = cv2.threshold(
                src=np_array,
                thresh=self.parameters["thresh"],
                maxval=self.parameters["max_val"],
                type=cv2.THRESH_TRUNC,
            )
            return thresholded_np_array

        if image_nparray.shape[2] == 1:
            return apply_truncated_threshold(image_nparray)

        R, G, B = cv2.split(image_nparray)
        r_thresh = apply_truncated_threshold(R)
        g_thresh = apply_truncated_threshold(G)
        b_thresh = apply_truncated_threshold(B)

        return cv2.merge([r_thresh, g_thresh, b_thresh])


if __name__ == "__main__":
    step = TruncatedThresholder()
    print(step.get_step_json_representation())
