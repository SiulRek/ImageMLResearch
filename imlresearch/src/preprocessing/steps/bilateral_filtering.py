import cv2

from imlresearch.src.preprocessing.steps.step_base import StepBase


class BilateralFilter(StepBase):
    """
    Applies a bilateral filter to an image for edge-preserving smoothing.
    """

    arguments_datatype = {
        "diameter": int,
        "sigma_color": float,
        "sigma_space": float,
    }
    name = "Bilateral Filter"

    def __init__(self, diameter=9, sigma_color=75, sigma_space=75):
        """
        Initializes the BilateralFilter object for integration in an image
        preprocessing pipeline.

        Parameters
        ----------
        diameter : int, optional
            Diameter of each pixel neighborhood used during filtering
            (default is 9).
        sigma_color : float, optional
            Filter sigma in the color space. Larger values mean farther colors
            mix together (default is 75).
        sigma_space : float, optional
            Filter sigma in the coordinate space. Larger values mean farther
            pixels influence each other (default is 75).
        """
        super().__init__(locals())

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Applies a bilateral filter to the input image.

        Parameters
        ----------
        image_nparray : np.ndarray
            The input image array.

        Returns
        -------
        np.ndarray
            The filtered image.
        """
        return cv2.bilateralFilter(
            src=image_nparray,
            d=self.parameters["diameter"],
            sigmaColor=self.parameters["sigma_color"],
            sigmaSpace=self.parameters["sigma_space"],
        )


if __name__ == "__main__":
    step = BilateralFilter()
    print(step.get_step_json_representation())
