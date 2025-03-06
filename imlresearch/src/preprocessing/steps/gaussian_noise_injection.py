import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class GaussianNoiseInjector(StepBase):
    """
    A data augmentation step that injects Gaussian noise into an image tensor.

    The noise intensity is specified by the mean and standard deviation of the
    Gaussian distribution. The output tensor type is `tf.float32`. Optionally,
    the values of the output tensor can be clipped to a valid range.
    """

    arguments_datatype = {
        "mean": float,
        "sigma": float,
        "apply_clipping": bool,
        "seed": int,
    }
    name = "Gaussian Noise Injector"

    def __init__(self, mean=0.0, sigma=0.05, apply_clipping=True, seed=42):
        """
        Initialize the GaussianNoiseInjector for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        mean : float, optional
            The mean of the Gaussian noise distribution. Default is 0.0.
        sigma : float, optional
            The standard deviation of the Gaussian noise distribution. Default
            is 0.05.
        apply_clipping : bool, optional
            If True, clips the output values to be within a valid range.
            Default is True.
        seed : int, optional
            Random seed for reproducibility. Default is 42.
        """
        super().__init__(locals())

    def _setup(self, dataset):
        """
        Set up the GaussianNoiseInjector with a fixed random seed for
        reproducibility.

        Parameters
        ----------
        dataset : Any
            The dataset being processed.

        Returns
        -------
        Any
            The result of the superclass setup method.
        """
        tf.random.set_seed(self.parameters["seed"])
        return super()._setup(dataset)

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Inject Gaussian noise into an image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The noisy image tensor with the Gaussian noise injected.
        """
        shape = tf.shape(image_tensor)
        image_tensor = tf.cast(image_tensor, self.output_datatype)
        gaussian_noise = tf.random.normal(
            shape,
            mean=self.parameters["mean"],
            stddev=self.parameters["sigma"],
        )
        gaussian_noise = tf.cast(gaussian_noise, self.output_datatype)
        noisy_image = image_tensor + gaussian_noise

        if self.parameters["apply_clipping"]:
            if self.output_datatype == tf.uint8:
                noisy_image = tf.clip_by_value(noisy_image, 0, 255)
            else:
                noisy_image = tf.clip_by_value(noisy_image, 0.0, 1.0)

        return noisy_image


if __name__ == "__main__":
    step = GaussianNoiseInjector()
    print(step.get_step_json_representation())
