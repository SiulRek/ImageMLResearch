import tensorflow as tf

from imlresearch.src.preprocessing.steps.step_base import StepBase


class MeanNormalizer(StepBase):
    """
    A preprocessing step that applies mean normalization to an image tensor.

    This normalization ensures that pixel values are centered around zero
    and scaled based on the dataset's range.

    Note
    ----
    The data type of the output image tensor is `tf.float16`.
    """

    arguments_datatype = {}
    name = "Mean Normalizer"

    def __init__(self):
        """
        Initialize the MeanNormalizer for integration into an image
        preprocessing pipeline.
        """
        super().__init__({})
        self.output_datatype = tf.float16
        self._mean_val = None
        self._range_val = None

    def _setup(self, dataset):
        """
        Compute the mean and range (max - min) of the dataset.

        Parameters
        ----------
        dataset : tf.data.Dataset
            The dataset on which statistics are computed.
        """
        mean_vals = []
        range_vals = []
        for sample in dataset:
            sample = tf.cast(sample, self.output_datatype)
            mean_vals.append(tf.reduce_mean(sample))
            range_vals.append(tf.reduce_max(sample) - tf.reduce_min(sample))

        self._mean_val = tf.reduce_mean(mean_vals)
        self._range_val = tf.reduce_mean(range_vals)

        self._mean_val = tf.cast(self._mean_val, self.output_datatype)
        self._range_val = tf.cast(self._range_val, self.output_datatype)

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Apply mean normalization to an image tensor.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The mean-normalized image tensor.
        """
        image_tensor = tf.cast(image_tensor, self.output_datatype)
        normalized_image = (
            (image_tensor - self._mean_val) / (self._range_val + 1e-4)
        )
        return normalized_image


if __name__ == "__main__":
    step = MeanNormalizer()
    print(step.get_step_json_representation())
