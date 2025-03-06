import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class RandomCropper(StepBase):
    """
    A data augmentation step that randomly crops a portion of the image.

    The crop size is defined by the specified width and height, and the crop
    is randomly placed within the image.
    """

    arguments_datatype = {"crop_size": (int, int), "seed": int}
    name = "Random Cropper"

    def __init__(self, crop_size=(256, 256), seed=42):
        """
        Initialize the RandomCropper for integration into an image
        preprocessing pipeline.

        Parameters
        ----------
        crop_size : tuple of int, optional
            The size of the crop (width, height) in pixels.
            Default is (256, 256).
        seed : int, optional
            A seed for the random number generator for reproducible results.
            Default is 42.
        """
        super().__init__(locals())

    def _setup(self, dataset):
        """
        Set up the RandomCropper with a fixed random seed for reproducibility.

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
        Apply random cropping to an image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The cropped image tensor.
        """
        image_shape = tf.shape(image_tensor)
        crop_height, crop_width = self.parameters["crop_size"]

        crop_height = tf.minimum(crop_height, image_shape[0])
        crop_width = tf.minimum(crop_width, image_shape[1])

        random_top = tf.random.uniform(
            shape=(),
            maxval=image_shape[0] - crop_height + 1,
            dtype=tf.int32,
        )
        random_left = tf.random.uniform(
            shape=(),
            maxval=image_shape[1] - crop_width + 1,
            dtype=tf.int32,
        )

        cropped_image = tf.image.crop_to_bounding_box(
            image_tensor, random_top, random_left, crop_height, crop_width
        )
        return cropped_image


if __name__ == "__main__":
    step = RandomCropper()
    print(step.get_step_json_representation())
