import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class MinMaxNormalizer(StepBase):
    """
    Applies min-max normalization to an image tensor.

    The normalization rescales pixel values to the range [0, 1], ensuring
    the data is scaled appropriately for deep learning models.
    """

    arguments_datatype = {}
    name = "Min Max Normalizer"

    def __init__(self):
        """
        Initializes the MinMaxNormalizer for integration into an image
        preprocessing pipeline.
        """
        super().__init__({})
        self.output_datatype = tf.float16
        self._min_val = None
        self._max_val = None

    def _setup(self, dataset):
        """
        Computes the minimum and maximum values of the dataset.

        Parameters
        ----------
        dataset : tf.data.Dataset
            The dataset to compute the min-max statistics.
        """
        min_vals = []
        max_vals = []
        for sample in dataset:
            min_vals.append(tf.reduce_min(sample))
            max_vals.append(tf.reduce_max(sample))

        self._min_val = tf.cast(tf.reduce_min(min_vals), self.output_datatype)
        self._max_val = tf.cast(tf.reduce_max(max_vals), self.output_datatype)

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Applies min-max normalization to the input image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The normalized image tensor.
        """
        image_tensor = tf.cast(image_tensor, self.output_datatype)
        normalized_image = (
            (image_tensor - self._min_val) / (self._max_val - self._min_val)
        )
        return normalized_image


if __name__ == "__main__":
    step = MinMaxNormalizer()
    print(step.get_step_json_representation())
