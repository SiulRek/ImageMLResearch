import cv2

from imlresearch.preprocessing.steps.step_base import StepBase


class TruncatedThresholder(StepBase):
    """
    A preprocessing step that applies truncated thresholding to an image.

    Note: In the case of RGB images, it processes each color channel (Red,
    Green, Blue) separately.
    """

    arguments_datatype = {"thresh": float, "max_val": float}
    name = "Truncated Thresholding"

    def __init__(self, thresh=128, max_val=255):
        """
        Initializes the TruncatedThresholder object that can be integrated into
        an image preprocessing pipeline.

        Args:
            - thresh (float, optional): The threshold value used for
                truncated thresholding. Pixel values greater than this threshold
                are set to the threshold value itself, and values less than or
                equal to the threshold remain unchanged. Defaults to 128.
            - max_val (float, optional): The maximum value that a pixel can
                take after thresholding. Defaults to 255.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):

        def apply_truncated_threshold(np_array):
            _, thresholded_np_array = cv2.threshold(
                src=np_array,
                thresh=self.parameters["thresh"],
                maxval=self.parameters["max_val"],
                type=cv2.THRESH_TRUNC,
            )
            return thresholded_np_array

        if image_nparray.shape[2] == 1:
            thresholded_image = apply_truncated_threshold(image_nparray)
        else:
            R, G, B = cv2.split(image_nparray)
            r_thresholded = apply_truncated_threshold(R)
            g_thresholded = apply_truncated_threshold(G)
            b_thresholded = apply_truncated_threshold(B)
            thresholded_image = cv2.merge([r_thresholded, g_thresholded, b_thresholded])

        return thresholded_image


if __name__ == "__main__":
    step = TruncatedThresholder()
    print(step.get_step_json_representation())
