import tensorflow as tf

from src.preprocessing.steps.step_base import StepBase


class MeanNormalizer(StepBase):
    """
    A preprocessing step that applies mean normalization to an image tensor.

    Note: The data type of the output image tensor is tf.float16.
    """

    arguments_datatype = {}
    name = "Mean Normalizer"

    def __init__(self):
        """ Initializes the MeanNormalizer object for integration into an image
        preprocessing pipeline. """
        super().__init__({})
        self.output_datatype = tf.float16
        self._mean_val = None
        self._range_val = None

    def _setup(self, dataset):
        """
        Computes the mean and range (max - min) of the dataset.

        Args:
            - dataset (tf.data.Dataset): The dataset to compute the
                statistic on.
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
        image_tensor = tf.cast(image_tensor, self.output_datatype)
        normalized_image = (image_tensor - self._mean_val) / (self._range_val + 1e-8)
        return normalized_image


if __name__ == "__main__":
    step = MeanNormalizer()
    print(step.get_step_json_representation())