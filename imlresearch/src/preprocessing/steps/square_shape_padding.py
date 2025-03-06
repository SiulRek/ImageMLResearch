import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class SquareShapePadder(StepBase):
    """
    Pads an image to a square shape using a specified pixel value.
    """

    arguments_datatype = {"padding_pixel_value": int}
    name = "Square Shape Padder"

    def __init__(self, padding_pixel_value=0):
        """
        Initializes the SquareShapePadder for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        padding_pixel_value : int, optional
            The pixel value to be used for padding (default is 0).
        """
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Pads the input image to make it square while maintaining content
        alignment.

        Parameters
        ----------
        image_tensor : tf.Tensor
            A 3D tensor representing the image with shape
            (height, width, channels).

        Returns
        -------
        tf.Tensor
            The padded square image tensor.
        """
        shape = tf.shape(image_tensor)
        height, width, channels = shape[0], shape[1], shape[2]

        if height > width:
            pad_top, pad_bottom = 0, 0
            pad_left = (height - width) // 2
            pad_right = height - width - pad_left
        else:
            pad_left, pad_right = 0, 0
            pad_top = (width - height) // 2
            pad_bottom = width - height - pad_top

        pad_width = [[pad_top, pad_bottom], [pad_left, pad_right], [0, 0]]

        tf_padded_img = tf.pad(
            image_tensor,
            pad_width,
            constant_values=self.parameters["padding_pixel_value"],
        )

        tf_padded_img = tf.ensure_shape(
            tf_padded_img, [max(height, width), max(height, width), channels]
        )

        return tf_padded_img


if __name__ == "__main__":
    step = SquareShapePadder()
    print(step.get_step_json_representation())
