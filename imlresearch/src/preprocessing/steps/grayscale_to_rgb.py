from tensorflow import image

from imlresearch.src.preprocessing.steps.step_base import StepBase


class GrayscaleToRGB(StepBase):
    """
    A preprocessing step that converts grayscale images to RGB images.

    If the input image has a single channel, it is expanded to three channels
    to match the RGB format.
    """

    arguments_datatype = {}
    name = "Grayscale To RGB"

    def __init__(self):
        """
        Initialize the GrayscaleToRGB for integration into an image
        preprocessing pipeline.
        """
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Convert a grayscale image tensor to an RGB image.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The converted RGB image tensor if the input was grayscale,
            otherwise returns the original tensor.
        """
        if image_tensor.shape[2] == 1:
            return image.grayscale_to_rgb(image_tensor)
        return image_tensor


if __name__ == "__main__":
    step = GrayscaleToRGB()
    print(step.get_step_json_representation())
