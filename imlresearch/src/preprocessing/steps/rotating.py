import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class Rotator(StepBase):
    """
    A preprocessing step that rotates an image tensor by a specified angle.

    The angle of rotation is specified as an input parameter. The angle must
    be a multiple of 90 degrees; otherwise, it will be rounded to the nearest
    multiple of 90 degrees.
    """

    arguments_datatype = {"angle": float}
    name = "Rotator"

    def __init__(self, angle=90.0):
        """
        Initialize the Rotator for integration into an image preprocessing
        pipeline.

        Parameters
        ----------
        angle : float, optional
            The angle of rotation in degrees. Must be a multiple of 90.
            Default is 90.0.
        """
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Apply rotation to an image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The rotated image tensor.
        """
        return tf.image.rot90(
            image_tensor, k=int(self.parameters["angle"] / 90)
        )


if __name__ == "__main__":
    step = Rotator()
    print(step.get_step_json_representation())
