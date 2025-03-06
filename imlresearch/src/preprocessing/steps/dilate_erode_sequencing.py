import random

import cv2
import numpy as np

from imlresearch.src.preprocessing.steps.step_base import StepBase


class DilateErodeSequencer(StepBase):
    """
    A preprocessing step that applies a sequence of dilation and erosion
    operations to an image.

    This class can automatically generate an operation sequence based on the
    provided iterations and erosion probability.
    """

    arguments_datatype = {
        "kernel_size": int,
        "sequence": str,
        "iterations": int,
        "erosion_probability": float,
    }
    name = "Dilate Erode Sequencer"

    def __init__(
        self,
        kernel_size=3,
        sequence="de",
        iterations=-1,
        erosion_probability=0.5,
    ):
        """
        Initialize the DilateErodeSequencer for use in an image preprocessing
        pipeline.

        Parameters
        ----------
        kernel_size : int, optional
            Size of the kernel for dilation and erosion operations.
            Default is 3.
        sequence : str, optional
            The sequence of operations ('d' for dilation, 'e' for erosion).
            Default is "de".
        iterations : int, optional
            Number of times the sequence is repeated. If positive, a sequence
            is generated automatically. Default is -1.
        erosion_probability : float, optional
            Probability of choosing erosion when generating a random sequence.
            Must be between 0 and 1. Default is 0.5.

        Raises
        ------
        ValueError
            If erosion probability is not in the range [0,1].
        """
        if not 0 <= erosion_probability <= 1:
            raise ValueError("Erosion probability must be between 0 and 1.")

        sequence = self.generate_sequence(
            sequence, iterations, erosion_probability
        )

        parameters = {
            "kernel_size": kernel_size,
            "sequence": sequence,
            "iterations": iterations,
            "erosion_probability": erosion_probability,
        }

        super().__init__(parameters)

    def generate_sequence(self, sequence, iterations, erosion_probability):
        """
        Generate a sequence of operations based on the specified probability
        and iterations.

        Parameters
        ----------
        sequence : str
            Initial sequence of operations.
        iterations : int
            Number of iterations to extend the sequence.
        erosion_probability : float
            Probability of choosing erosion in the generated sequence.

        Returns
        -------
        str
            The generated sequence of operations.
        """
        if iterations > 1:
            return "".join(
                self._choose_operation(erosion_probability)
                for _ in range(iterations)
            )
        return sequence

    def _choose_operation(self, erosion_probability):
        """
        Randomly choose between dilation ('d') and erosion ('e') based on the
        specified probability.

        Parameters
        ----------
        erosion_probability : float
            Probability of choosing erosion.

        Returns
        -------
        str
            'd' for dilation or 'e' for erosion.
        """
        return "e" if random.random() < erosion_probability else "d"

    @StepBase._nparray_pyfunc_wrapper
    def __call__(self, image_nparray):
        """
        Apply the preprocessing steps to the given image.

        Parameters
        ----------
        image_nparray : numpy.ndarray
            The input image to be processed.

        Returns
        -------
        numpy.ndarray
            The processed image after applying the dilation and erosion
            sequence.
        """
        kernel = np.ones(
            (self.parameters["kernel_size"], self.parameters["kernel_size"]),
            np.uint8,
        )
        processed_image = image_nparray

        for operation in self.parameters["sequence"]:
            if operation == "d":
                processed_image = cv2.dilate(
                    processed_image,
                    kernel,
                    iterations=self.parameters["iterations"],
                )
            elif operation == "e":
                processed_image = cv2.erode(
                    processed_image,
                    kernel,
                    iterations=self.parameters["iterations"],
                )
            else:
                raise ValueError(
                    "Invalid operation in sequence. "
                    "Only 'd' (dilation) and 'e' (erosion) are allowed."
                )

        return processed_image


if __name__ == "__main__":
    step = DilateErodeSequencer()
    print(step.get_step_json_representation())
