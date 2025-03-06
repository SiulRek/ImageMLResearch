import cv2
import numpy as np

from imlresearch.src.preprocessing.steps.step_base import StepBase


class RandomElasticTransformer(StepBase):
    """
    A data augmentation step that applies a random elastic transformation
    to an image.

    This transformation distorts the image locally using displacement fields
    smoothed with a Gaussian filter, simulating elastic deformations.
    """

    arguments_datatype = {"alpha": float, "sigma": float, "seed": int}
    name = "Random Elastic Transformer"

    def __init__(self, alpha=34, sigma=4, seed=42):
        """
        Initialize the RandomElasticTransformer for integration into an
        image preprocessing pipeline.

        Parameters
        ----------
        alpha : float, optional
            Intensity of the transformation. Higher values result in stronger
            distortions. Default is 34.
        sigma : float, optional
            Standard deviation of the Gaussian filter used to smooth the
            displacement fields. Default is 4.
        seed : int, optional
            Random seed for reproducibility. Default is 42.
        """
        super().__init__(locals())

    def _setup(self, dataset):
        """
        Set up the transformer with a fixed random seed for reproducibility.

        Parameters
        ----------
        dataset : Any
            The dataset being processed.

        Returns
        -------
        Any
            The result of the superclass setup method.
        """
        np.random.seed(self.parameters["seed"])
        return super()._setup(dataset)

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply random elastic transformation to an image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image as a NumPy array.

        Returns
        -------
        numpy.ndarray
            The transformed image with elastic distortions.
        """
        row, col, _ = image_nparray.shape

        alpha = self.parameters["alpha"]
        dx = np.random.uniform(-1, 1, size=(row, col)) * alpha
        dy = np.random.uniform(-1, 1, size=(row, col)) * alpha

        kernel_size = int(6 * self.parameters["sigma"]) + 1
        kernel_size = (kernel_size, kernel_size)  # Making it a tuple

        sdx = cv2.GaussianBlur(dx, kernel_size, 0)
        sdy = cv2.GaussianBlur(dy, kernel_size, 0)

        x, y = np.meshgrid(np.arange(col), np.arange(row))
        map_x = np.float32(x + sdx)
        map_y = np.float32(y + sdy)

        return cv2.remap(
            image_nparray,
            map_x,
            map_y,
            interpolation=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_REFLECT_101,
        )


if __name__ == "__main__":
    step = RandomElasticTransformer()
    print(step.get_step_json_representation())
