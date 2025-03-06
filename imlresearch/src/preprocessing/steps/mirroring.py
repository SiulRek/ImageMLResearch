import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class Mirrorer(StepBase):
    """
    A preprocessing step that mirrors an image tensor either horizontally
    or vertically.

    The direction of mirroring is specified as an input parameter.
    """

    arguments_datatype = {"mirror_direction": str}
    name = "Mirrorer"

    def __init__(self, mirror_direction="horizontal"):
        """
        Initialize the Mirrorer for integration into an image preprocessing
        pipeline.

        Parameters
        ----------
        mirror_direction : str, optional
            The direction for mirroring the image. Accepts 'horizontal' or
            'vertical'. Default is 'horizontal'.
        """
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Apply mirroring to an image tensor based on the specified direction.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The mirrored image tensor.
        """
        direction = self.parameters["mirror_direction"]

        if direction == "horizontal":
            return tf.image.flip_left_right(image_tensor)
        if direction == "vertical":
            return tf.image.flip_up_down(image_tensor)

        raise ValueError(
            "Invalid mirror direction. Choose 'horizontal' or 'vertical'."
        )


if __name__ == "__main__":
    step = Mirrorer()
    print(step.get_step_json_representation())
