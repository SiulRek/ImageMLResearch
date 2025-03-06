from imlresearch.src.preprocessing.steps.step_base import StepBase


class DummyStep(StepBase):
    """
    A dummy preprocessing step that does nothing to the image.

    This step is useful for testing purposes or when no transformation is
    needed.
    """

    name = "Dummy Step"
    arguments_datatype = {}

    def __init__(self):
        """
        Initialize the DummyStep for integration into an image preprocessing
        pipeline.
        """
        super().__init__(locals())

    @StepBase._tensor_pyfunc_wrapper
    def __call__(self, image_tensor):
        """
        Return the input image tensor without any modification.

        Parameters
        ----------
        image_tensor : tf.Tensor
            The input image tensor.

        Returns
        -------
        tf.Tensor
            The unchanged image tensor.
        """
        return image_tensor


if __name__ == "__main__":
    step = DummyStep()
    print(step.get_step_json_representation())
