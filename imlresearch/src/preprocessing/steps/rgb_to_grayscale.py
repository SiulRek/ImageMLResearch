from tensorflow import image

from imlresearch.src.preprocessing.steps.step_base import StepBase


class RGBToGrayscale(StepBase):
    """
    A preprocessing step that converts an RGB image to a grayscale image.

    The conversion uses the standard method for transforming RGB values into
    a single grayscale value based on luminance.
    """

    arguments_datatype = {}
    name = "RGB To Grayscale"

    def __init__(self):
        """
        Initialize the RGBToGrayscale for integration into an image
        preprocessing pipeline.
        """
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Convert an RGB image tensor to grayscale.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor with 3 channels (RGB).

        Returns
        -------
        tf.Tensor
            The grayscale image tensor if the input is RGB, otherwise returns
            the original tensor.
        """
        if image_tensor.shape[2] == 3:
            return image.rgb_to_grayscale(image_tensor)
        return image_tensor


if __name__ == "__main__":
    step = RGBToGrayscale()
    print(step.get_step_json_representation())
