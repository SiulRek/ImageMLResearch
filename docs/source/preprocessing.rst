.. _Modules_Preprocessing:

Image Preprocessing
-----------------------------------------------
The Image Preprocessing module manages and applies a sequence of preprocessing
steps to image datasets using the ``ImagePreprocessor`` class.

Key Definitions:

1. **Preprocessing Step**: A discrete action applied to an image dataset, such as
    noise reduction or normalization. Each step is implemented as a subclass of
    the abstract class ``StepBase``.
2. **Pipeline**: An ordered list of preprocessing steps applied sequentially to an image dataset.

----

.. class:: ImagePreprocessor

    Manages and processes a pipeline of image preprocessing steps.

    The ``ImagePreprocessor`` class encapsulates a sequence of preprocessing
    operations defined as steps. Each step is a discrete preprocessing action,
    such as noise reduction or normalization, applied in sequence to an input
    dataset of images.

    .. method:: __init__(raise_step_process_exception: bool = True)

        Initializes the ImagePreprocessor with an empty pipeline.

        :param raise_step_process_exception: Determines whether exceptions during
                                             step processing are raised or logged.
        :type raise_step_process_exception: bool

    .. method:: set_default_datatype(datatype: tf.DType)

        Sets the default datatype for pipeline steps.

        :param datatype: The default output datatype for the pipeline steps.
        :type datatype: tf.dtypes.DType

    .. method:: set_pipe(pipeline: list[StepBase])

        Sets the preprocessing pipeline with a deep copy of the provided steps.

        :param pipeline: List of preprocessing steps to be set in the pipeline.
        :type pipeline: list[StepBase]

    .. method:: pipe_append(step: StepBase)

        Appends a new step to the pipeline.

        :param step: The preprocessing step to be appended.
        :type step: StepBase

    .. method:: pipe_pop() -> StepBase

        Removes and returns the last step from the pipeline.

        :returns: *(StepBase)* - The last step that was removed from the pipeline.

    .. method:: pipe_clear()

        Clears all steps from the pipeline.

    .. method:: process(image_dataset: tf.data.Dataset) -> tf.data.Dataset

        Applies each preprocessing step to the provided dataset.

        If ``_raise_step_process_exception`` is True, exceptions occurring in a step
        will be caught and logged, and the process will return None. Otherwise, the
        process continues without exception handling.

        :param image_dataset: The TensorFlow dataset to be processed.
        :type image_dataset: tf.data.Dataset

        :returns: *(tf.data.Dataset)* - The processed dataset after applying all the steps in the pipeline.

    .. method:: save_pipe_to_json(json_path: str)

        Serializes the preprocessing pipeline to the specified JSON file.

        :param json_path: File path where the pipeline configuration will be saved.
        :type json_path: str

    .. method:: load_pipe_from_json(json_path: str)

        Loads and reconstructs a preprocessing pipeline from a JSON file.

        :param json_path: File path from which the pipeline configuration will be loaded.
        :type json_path: str

    .. method:: load_randomized_pipe_from_json(json_path: str)

        Loads and reconstructs a preprocessing pipeline from a JSON file with randomized parameters.

        :param json_path: File path from which the pipeline configuration will be loaded.
        :type json_path: str

    .. method:: get_pipe_code_representation() -> str

        Generates a text representation of the pipeline's configuration.

        :returns: *(str)* A string representation of the pipeline in a code-like format.

----

The following preprocessing steps are available in the module:

.. list-table::
   :widths: 30 65
   :header-rows: 1

   * - **Category**
     - **Preprocessing Steps**
   * - Histogram Equalization
     - ``AdaptiveHistogramEqualizer``, ``GlobalHistogramEqualizer``
   * - Blurring & Smoothing
     - ``GaussianBlurFilter``, ``MedianBlurFilter``, ``BilateralFilter``, ``AverageBlurFilter``
   * - Thresholding
     - ``OtsuThresholding``, ``AdaptiveThresholding``, ``BinaryThresholding``, ``TruncatedThresholding``, ``ThresholdToZero``
   * - Noise Reduction & Injection
     - ``NonLocalMeanDenoiser``, ``GaussianNoiseInjector``
   * - Color Space Conversion
     - ``RGBToGrayscale``, ``GrayscaleToRGB``
   * - Geometric Transformations
     - ``Rotator``, ``Mirrorer``, ``ShapeResizer``, ``SquareShapePadder``
   * - Morphological Operations
     - ``ErosionFilter``, ``DilationFilter``, ``DilateErodeSequencer``
   * - Normalization
     - ``MinMaxNormalizer``, ``StandardNormalizer``, ``MeanNormalizer``, ``LocalContrastNormalizer``
   * - Random Augmentations
     - ``RandomColorJitterer``, ``RandomSharpening``, ``RandomRotator``, ``RandomFlipper``, ``RandomCropper``, ``RandomPerspectiveTransformer``, ``RandomElasticTransformer``
   * - Miscellaneous
     - ``TypeCaster``, ``Clipper``, ``Scaler``