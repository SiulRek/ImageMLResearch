import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class ShapeResizer(StepBase):
    """
    A preprocessing step that resizes an image to a specified shape,
    potentially altering its aspect ratio.

    The image can be resized using different methods such as bilinear,
    nearest neighbor, bicubic, and others.
    """

    arguments_datatype = {"desired_shape": (int, int), "resize_method": str}
    name = "Shape Resizer"
    resize_methods = {
        "bilinear": tf.image.ResizeMethod.BILINEAR,
        "nearest": tf.image.ResizeMethod.NEAREST_NEIGHBOR,
        "bicubic": tf.image.ResizeMethod.BICUBIC,
        "lanczos3": tf.image.ResizeMethod.LANCZOS3,
        "lanczos5": tf.image.ResizeMethod.LANCZOS5,
        "area": tf.image.ResizeMethod.AREA,
    }

    def __init__(self, desired_shape=(2000, 2000), resize_method="bilinear"):
        """
        Initialize the ShapeResizer for integration into an image preprocessing
        pipeline.

        Parameters
        ----------
        desired_shape : tuple of int, optional
            The desired height and width of the image after resizing. Default
            is (2000, 2000).
        resize_method : str, optional
            The method used for resizing. Options are 'bilinear', 'nearest',
            'bicubic', 'lanczos3', 'lanczos5', and 'area'.
            Default is 'bilinear'.
        """
        self.assert_resize_method(resize_method)
        super().__init__(locals())

    def assert_resize_method(self, resize_method):
        """
        Ensure that the specified resize method is valid.

        Parameters
        ----------
        resize_method : str
            The method used for resizing.
        """
        if resize_method not in self.resize_methods:
            raise ValueError(
                f"Resize method '{resize_method}' is not supported. "
                f"Choose from {list(self.resize_methods.keys())}."
            )

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Apply resizing to an image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The resized image tensor.
        """
        channels = image_tensor.shape[2]
        image_tensor_with_batch = tf.expand_dims(image_tensor, axis=0)

        method = self.resize_methods[self.parameters["resize_method"]]
        resized_image_with_batch = tf.image.resize(
            image_tensor_with_batch,
            self.parameters["desired_shape"],
            method=method,
        )

        resized_image = tf.squeeze(resized_image_with_batch, axis=0)
        resized_image = tf.ensure_shape(
            resized_image, [*self.parameters["desired_shape"], channels]
        )

        return resized_image


if __name__ == "__main__":
    step = ShapeResizer()
    print(step.get_step_json_representation())
