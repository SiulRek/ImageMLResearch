import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class OstuThresholder(StepBase):
    """
    A preprocessing step that applies Otsu's Thresholding to an image.

    For RGB images, each color channel (Red, Green, Blue) is processed
    separately. Otsu's method automatically determines an optimal threshold
    value to separate the foreground from the background.
    """

    arguments_datatype = {"thresh": float, "max_val": float}
    name = "Otsu Thresholding"

    def __init__(self, thresh=0, max_val=255):
        """
        Initialize the OtsuThresholder for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        thresh : float, optional
            The threshold value used for thresholding. Default is 0.
        max_val : float, optional
            The maximum value that a pixel can take after thresholding.
            Default is 255.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply Otsu's thresholding to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The thresholded image.
        """
        if image_nparray.shape[2] == 1:
            _, thresholded_image = cv2.threshold(
                image_nparray,
                thresh=self.parameters["thresh"],
                maxval=self.parameters["max_val"],
                type=cv2.THRESH_BINARY + cv2.THRESH_OTSU,
            )
            return thresholded_image

        R, G, B = cv2.split(image_nparray)
        _, r_thresh = cv2.threshold(
            R, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        _, g_thresh = cv2.threshold(
            G, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        _, b_thresh = cv2.threshold(
            B, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return cv2.merge([r_thresh, g_thresh, b_thresh])


if __name__ == "__main__":
    step = OstuThresholder()
    print(step.get_step_json_representation())
