import cv2

from imlresearch.preprocessing.steps.step_base import StepBase


class OstuThresholder(StepBase):
    """
    A preprocessing step that applies Otsu's Thresholding to an image.

    Note: In the case of RGB images, it processes each color channel (Red,
    Green, Blue) separately.
    """

    arguments_datatype = {"thresh": float, "max_val": float}
    name = "Otsu Thresholding"

    def __init__(self, thresh=0, max_val=255):
        """
        Initializes the OstuThresholder object that can be integrated in an
        image preprocessing pipeline.

        Args:
            - thresh (float, optional): The threshold value used for
                thresholding. Defaults to 0.
            - max_val (float, optional): The maximum value that a pixel can
                take after thresholding. Defaults to 255.
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):

        if image_nparray.shape[2] == 1:
            _, thresholded_image = cv2.threshold(
                image_nparray,
                thresh=self.parameters["thresh"],
                maxval=self.parameters["max_val"],
                type=cv2.THRESH_BINARY + cv2.THRESH_OTSU,
            )
        else:
            R, G, B = cv2.split(image_nparray)
            _, r_thresholded = cv2.threshold(
                R, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
            _, g_thresholded = cv2.threshold(
                G, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
            _, b_thresholded = cv2.threshold(
                B, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
            thresholded_image = cv2.merge([r_thresholded, g_thresholded, b_thresholded])

        return thresholded_image


if __name__ == "__main__":
    step = OstuThresholder()
    print(step.get_step_json_representation())
