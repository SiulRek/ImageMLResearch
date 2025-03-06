import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class ZeroThreshold(StepBase):
    """
    Applies thresholding to zero on an image.

    Pixel values greater than the threshold remain unchanged, whereas values
    less than or equal to the threshold are set to zero.
    """

    arguments_datatype = {"thresh": float, "max_val": float}
    name = "Threshold to Zero"

    def __init__(self, thresh=128, max_val=255):
        """
        Initializes the ZeroThreshold for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        thresh : float, optional
            The threshold value for zero thresholding. Pixel values greater
            than this threshold remain unchanged, while values less than or
            equal to it are set to 0 (default is 128).
        max_val : float, optional
            The maximum possible pixel value after thresholding
            (default is 255).
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Applies thresholding to zero on the input image.

        Parameters
        ----------
        image_nparray : np.ndarray
            The input image array.

        Returns
        -------
        np.ndarray
            The thresholded image.
        """

        def apply_zero_threshold(np_array):
            _, thresholded_np_array = cv2.threshold(
                src=np_array,
                thresh=self.parameters["thresh"],
                maxval=self.parameters["max_val"],
                type=cv2.THRESH_TOZERO,
            )
            return thresholded_np_array

        if image_nparray.shape[2] == 1:
            return apply_zero_threshold(image_nparray)

        R, G, B = cv2.split(image_nparray)
        r_thresh = apply_zero_threshold(R)
        g_thresh = apply_zero_threshold(G)
        b_thresh = apply_zero_threshold(B)

        return cv2.merge([r_thresh, g_thresh, b_thresh])


if __name__ == "__main__":
    step = ZeroThreshold()
    print(step.get_step_json_representation())
