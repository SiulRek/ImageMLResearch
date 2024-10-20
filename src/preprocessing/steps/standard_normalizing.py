import tensorflow as tf

from src.preprocessing.helpers.step_utils import reduce_std
from src.preprocessing.steps.step_base import StepBase


class StandardNormalizer(StepBase):
    """
    A preprocessing step that applies standard normalization (Z-score
    normalization) to an image tensor.

    Note: The data type of the output image tensor is tf.float16.
    """

    arguments_datatype = {}
    name = "Standard Normalizer"

    def __init__(self):
        """ Initializes the StandardNormalizer object for integration into an image
        preprocessing pipeline. """
        super().__init__({})
        self.output_datatype = tf.float16
        self._mean_val = None
        self._std_val = None

    def _compute_dataset_statistic(self, dataset):
        """
        Computes the mean and standard deviation of the dataset.

        Args:
            - dataset (tf.data.Dataset): The dataset to compute the
                statistic on.
        """
        mean_vals = []
        std_vals = []
        for sample in dataset:
            sample = tf.cast(sample, self.output_datatype)
            mean_vals.append(tf.reduce_mean(sample))
            std_vals.append(reduce_std(sample))
        self._mean_val = tf.reduce_mean(mean_vals)
        self._std_val = tf.reduce_mean(std_vals)

        self._mean_val = tf.cast(self._mean_val, self.output_datatype)
        self._std_val = tf.cast(self._std_val, self.output_datatype)

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        image_tensor = tf.cast(image_tensor, self.output_datatype)
        normalized_image = (image_tensor - self._mean_val) / (self._std_val + 1e-8)
        return normalized_image


if __name__ == "__main__":
    step = StandardNormalizer()
    print(step.get_step_json_representation())