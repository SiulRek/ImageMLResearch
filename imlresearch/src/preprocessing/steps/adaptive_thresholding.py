import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class AdaptiveThresholder(StepBase):
    """
    A preprocessing step that applies adaptive Thresholding to an image.

    Note: In the case of RGB images, it processes each color channel (Red,
    Green, Blue) separately.
    """

    arguments_datatype = {"block_size": int, "c": float, "max_val": float}
    name = "Adaptive Thresholding"

    def __init__(self, block_size=15, c=-2, max_val=255):
        """
        Initializes the AdaptiveThresholder object that can be integrated in an
        image preprocessing pipeline.

        Args:
            - block_size (int, optional): Size of the pixel neighborhood
                that is used to calculate the threshold value. Defaults to 15.
            - c (float, optional): Constant subtracted from the mean or
                weighted mean. Defaults to -2.
            - max_val (float, optional): The maximum value that a pixel can
                take. Defaults to 255.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):

        def apply_adaptive_threshold(np_array):
            return cv2.adaptiveThreshold(
                np_array,
                maxValue=self.parameters["max_val"],
                adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                thresholdType=cv2.THRESH_BINARY,
                blockSize=self.parameters["block_size"],  # Block size.
                C=self.parameters["c"],
            )

        if image_nparray.shape[2] == 1:
            thresholded_image = apply_adaptive_threshold(image_nparray)
        else:
            R, G, B = cv2.split(image_nparray)
            R_thresholded = apply_adaptive_threshold(R)
            G_thresholded = apply_adaptive_threshold(G)
            B_thresholded = apply_adaptive_threshold(B)
            thresholded_image = cv2.merge([R_thresholded, G_thresholded, B_thresholded])

        return thresholded_image


if __name__ == "__main__":
    step = AdaptiveThresholder()
    print(step.get_step_json_representation())
