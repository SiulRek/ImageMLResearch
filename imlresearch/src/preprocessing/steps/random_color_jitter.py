import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class RandomColorJitterer(StepBase):
    """
    A data augmentation step that randomly alters the brightness, contrast,
    saturation, and hue of an image tensor.

    Each attribute is adjusted within a specified range. For grayscale images,
    only brightness and contrast adjustments are applied, as saturation and
    hue changes are not applicable.
    """

    arguments_datatype = {
        "brightness": float,
        "contrast": float,
        "saturation": float,
        "hue": float,
        "seed": int,
    }
    name = "Random Color Jitterer"

    def __init__(
        self, brightness=0.3, contrast=0.3, saturation=0.3, hue=0.1, seed=42
    ):
        """
        Initialize the RandomColorJitterer for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        brightness : float, optional
            Maximum delta for brightness adjustment. Must be non-negative.
            Default is 0.3.
        contrast : float, optional
            Contrast factor range (lower, upper). Must be non-negative.
            Default is 0.3.
        saturation : float, optional
            Saturation factor range (lower, upper). Must be non-negative.
            Default is 0.3.
        hue : float, optional
            Maximum delta for hue adjustment. Must be in the range [0, 0.5].
            Default is 0.1.
        seed : int, optional
            An optional integer seed for random operations. Default is 42.
        """
        super().__init__(locals())

    def _setup(self, dataset):
        """
        Set up the jitterer with a fixed random seed for reproducibility.

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
        Apply random color jittering to an image.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The color-jittered image tensor.
        """
        is_grayscale = tf.shape(image_tensor)[-1] == 1

        image_tensor = tf.image.random_brightness(
            image_tensor,
            max_delta=self.parameters["brightness"],
            seed=self.parameters["seed"],
        )
        image_tensor = tf.image.random_contrast(
            image_tensor,
            lower=1 - self.parameters["contrast"],
            upper=1 + self.parameters["contrast"],
        )

        if not is_grayscale:
            image_tensor = tf.image.random_saturation(
                image_tensor,
                lower=1 - self.parameters["saturation"],
                upper=1 + self.parameters["saturation"],
            )
            image_tensor = tf.image.random_hue(
                image_tensor,
                max_delta=self.parameters["hue"],
            )

        return image_tensor


if __name__ == "__main__":
    step = RandomColorJitterer()
    print(step.get_step_json_representation())
