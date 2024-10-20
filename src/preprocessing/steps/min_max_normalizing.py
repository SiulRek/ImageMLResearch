import tensorflow as tf

from src.preprocessing.steps.step_base import StepBase


class MinMaxNormalizer(StepBase):
    """
    A preprocessing step that applies a min max normalization an image tensor.

    Note: The data type of the output image tensor is tf.float16.
    """

    arguments_datatype = {}
    name = "Min Max Normalizer"

    def __init__(self):
        """ Initializes the MinMaxNormalizer object for integration into an image
        preprocessing pipeline. """
        super().__init__({})
        self.output_datatype = tf.float16
    def _compute_dataset_statistic(self, dataset):
        """
        Computes the minimum and maximum values of the dataset.

        Args:
            - dataset (tf.data.Dataset): The dataset to compute the
                statistic on.
        """
        min_vals = []
        max_vals = []
        for sample in dataset:
            min_vals.append(tf.reduce_min(sample))
            max_vals.append(tf.reduce_max(sample))
        min_val = tf.reduce_min(min_vals)
        max_val = tf.reduce_max(max_vals)
        self._min_val = tf.cast(min_val, self.output_datatype)
        self._max_val = tf.cast(max_val, self.output_datatype)

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        image_tensor = tf.cast(image_tensor, self.output_datatype)
        normalized_image = (image_tensor - self._min_val) / (
            self._max_val - self._min_val
        )
        return normalized_image


if __name__ == "__main__":
    step = MinMaxNormalizer()
    print(step.get_step_json_representation())