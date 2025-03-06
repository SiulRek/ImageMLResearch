import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class TypeCaster(StepBase):
    """
    A preprocessing step that casts an image tensor to a specified data type.
    """

    arguments_datatype = {"output_dtype": str}
    name = "Type Caster"

    def __init__(self, output_dtype="float16"):
        """
        Initialize the TypeCaster for integration into an image preprocessing
        pipeline.

        Parameters
        ----------
        output_dtype : str, optional
            The desired data type to cast the image tensor to. Must be an
            attribute in TensorFlow. Default is 'float16'.
        """
        super().__init__(locals())
        self.output_datatype = getattr(tf, output_dtype)

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Apply type casting to an image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The image tensor cast to the specified data type.
        """
        # Casting is handled by the wrapper, so no explicit operation needed.
        return image_tensor


if __name__ == "__main__":
    step = TypeCaster()
    print(step.get_step_json_representation())
