import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class LocalContrastNormalizer(StepBase):
    """
    A preprocessing step that applies local contrast normalization to an
    image tensor.

    This process normalizes the local contrast of an image to enhance
    features in the image. It is typically applied after standard image
    normalization to improve the visibility of local features.

    Note
    ----
    The data type of the output image tensor is `tf.float16`.
    """

    arguments_datatype = {
        "depth_radius": int,
        "bias": float,
        "alpha": float,
        "beta": float,
    }
    name = "Local Contrast Normalizer"

    def __init__(self, depth_radius=5, bias=1.0, alpha=1e-4, beta=0.75):
        """
        Initialize the LocalContrastNormalizer for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        depth_radius : int, optional
            Depth radius for normalization. Default is 5.
        bias : float, optional
            Bias to avoid division by zero. Default is 1.0.
        alpha : float, optional
            Scale factor. Default is 1e-4.
        beta : float, optional
            Exponent for normalization. Default is 0.75.

        Note
        ----
        This step is ideally applied to images that have already undergone
        standard normalization to ensure appropriate centering and scaling
        of the image data before local contrast enhancement.
        """
        super().__init__(locals())
        self.output_datatype = tf.float16

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Apply local contrast normalization to an image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The image tensor after local contrast normalization.
        """
        image_tensor = tf.cast(image_tensor, tf.float16)

        # Add a batch dimension to image_tensor if it doesn't have one
        if len(image_tensor.shape) == 3:
            image_tensor = tf.expand_dims(image_tensor, axis=0)

        image_lcn = tf.nn.local_response_normalization(
            image_tensor,
            depth_radius=self.parameters["depth_radius"],
            bias=self.parameters["bias"],
            alpha=self.parameters["alpha"],
            beta=self.parameters["beta"],
        )

        # Remove the batch dimension if it was added earlier
        if len(image_lcn.shape) == 4 and image_lcn.shape[0] == 1:
            image_lcn = tf.squeeze(image_lcn, axis=0)

        return image_lcn


if __name__ == "__main__":
    step = LocalContrastNormalizer()
    print(step.get_step_json_representation())
