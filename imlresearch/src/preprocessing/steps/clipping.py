import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class Clipper(StepBase):
    """
    A preprocessing step that clips the pixel values of an image tensor
    to a specified range.

    This operation ensures that all pixel values fall within the defined
    minimum and maximum limits.
    """

    arguments_datatype = {"min_value": float, "max_value": float}
    name = "Clipper"

    def __init__(self, min_value=0.0, max_value=1.0):
        """
        Initialize the Clipper for integration into an image preprocessing
        pipeline.

        Parameters
        ----------
        min_value : float, optional
            The minimum value to clip to. Default is 0.0.
        max_value : float, optional
            The maximum value to clip to. Default is 1.0.
        """
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Clip the pixel values of an image tensor to the specified range.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The clipped image tensor, with pixel values limited to the
            specified range.
        """
        image_tensor = tf.cast(image_tensor, self.output_datatype)
        min_value = tf.cast(
            self.parameters["min_value"], dtype=self.output_datatype
        )
        max_value = tf.cast(
            self.parameters["max_value"], dtype=self.output_datatype
        )
        return tf.clip_by_value(image_tensor, min_value, max_value)


if __name__ == "__main__":
    step = Clipper()
    print(step.get_step_json_representation())
