import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class BinaryThresholder(StepBase):
    """
    A preprocessing step that applies binary thresholding to an image.

    Note: In the case of RGB images, it processes each color channel
    (Red, Green, Blue) separately.
    """

    arguments_datatype = {"thresh": float, "max_val": float}
    name = "Binary Thresholding"

    def __init__(self, thresh=128, max_val=255):
        """
        Initializes the BinaryThresholder object that can be integrated in
        an image preprocessing pipeline.

        Args:
            - thresh (float, optional): The threshold value used for binary
              thresholding. Pixel values greater than this threshold are set
              to the maximum value (255, white), and values less than or equal
              to the threshold are set to 0 (black). Defaults to 128.
            - max_val (float, optional): The maximum value that a pixel can
              take after thresholding. Defaults to 255.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):

        def apply_binary_threshold(np_array):
            _, thresholded_np_array = cv2.threshold(
                src=np_array,
                thresh=self.parameters["thresh"],
                maxval=self.parameters["max_val"],
                type=cv2.THRESH_BINARY,
            )
            return thresholded_np_array

        if image_nparray.shape[2] == 1:
            return apply_binary_threshold(image_nparray)

        R, G, B = cv2.split(image_nparray)
        r_thresh = apply_binary_threshold(R)
        g_thresh = apply_binary_threshold(G)
        b_thresh = apply_binary_threshold(B)

        return cv2.merge([r_thresh, g_thresh, b_thresh])


if __name__ == "__main__":
    step = BinaryThresholder()
    print(step.get_step_json_representation())
