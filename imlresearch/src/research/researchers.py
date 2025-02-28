import warnings

from imlresearch.src.data_handling.data_handler import DataHandler
from imlresearch.src.experimenting.experiment import Experiment
from imlresearch.src.plotting.plotters.binary_plotter import BinaryPlotter
from imlresearch.src.plotting.plotters.multi_class_plotter import MultiClassPlotter
from imlresearch.src.preprocessing.image_preprocessor import ImagePreprocessor
from imlresearch.src.research.attributes.research_attributes import ResearchAttributes
from imlresearch.src.training.trainer import Trainer
from imlresearch.src.utils.general.batch_utils import is_batched


class _ResearcherBase(DataHandler, Trainer):
    """
    The Researcher class acts as a high-level interface for conducting
    image-based machine learning experiments. It inherits functionalities from
    DataHandler, Trainer, and ResearchAttributes. It also synchronizes research
    attributes from a source instance during initialization.
    """

    def __init__(self, label_type, class_names):
        """
        Initializes the Researcher by calling initializers from inherited
        classes and synchronizing research attributes.

        Args:
            - label_type (str): The label type for the research attributes.
            - class_names (list): The class names for the research
                attributes.
        """
        assert class_names is not None, "It is recommended to provide class names."

        # Last one to be initialized overwrites the previous ones, in case of
        # conflicts. This should only occur in the case of label_manager.
        Trainer.__init__(self)
        DataHandler.__init__(self)
        ResearchAttributes.__init__(self, label_type, class_names)

        self._preprocessor = ImagePreprocessor()

    @property
    def preprocessor(self):
        """ ImagePreprocessor: The image preprocessor instance. """
        return self._preprocessor

    def run_experiment(self, directory, name, description, ask_for_analysis=False):
        """
        Sets up and runs an experiment within a context manager.

        Args:
            - directory (str): The directory to save the experiment data.
            - name (str): The name of the experiment.
            - description (str): The description of the experiment. for the
                report.
            - ask_for_analysis (bool, optional): Whether to ask AI for
                analysis. Defaults to False.

        Returns:
            - Experiment: The Experiment context manager instance.
        """
        return Experiment(
            self, directory, name, description, ask_for_analysis=ask_for_analysis
        )

    def apply_preprocessing_pipeline(self, pipeline, dataset_names=None, backup=False):
        """
        Applies a preprocessing pipeline to the datasets.

        Args:
            - pipeline (list[StepBase]): List of preprocessing steps.
            - dataset_names (list, optional): The dataset names to apply the
                pipeline to. Defaults to None.
            - backup (bool, optional): Whether to backup all the datasets
                before applying the pipeline. Defaults to False.

        NOTE: It is not supported to apply a preprocessing pipeline on batched
        datasets.
        """
        preprocessor = self._preprocessor
        preprocessor.set_pipe(pipeline)
        if dataset_names is None:
            dataset_names = self._datasets_container.keys()
        if hasattr(self, "backup_datasets") and backup:
            self.backup_datasets()
        elif backup:
            msg = "No backup_datasets method found. Skipping backup."
            warnings.warn(msg)
        for dataset_name in dataset_names:
            dataset = self._datasets_container[dataset_name]
            if is_batched(dataset):
                msg = "Applying a preprocessing pipeline on a batched dataset"
                msg += "is not supported."
                raise ValueError(msg)
            preprocessed_dataset = preprocessor.process(dataset)
            self._datasets_container[dataset_name] = preprocessed_dataset


class BinaryResearcher(_ResearcherBase, BinaryPlotter):
    """ The BinaryResearcher class inherits from _ResearcherBase and BinaryPlotter
    to provide functionalities for binary image classification research. """

    def __init__(self, class_names):
        """
        Initializes the BinaryResearcher by calling initializers from inherited
        classes and synchronizing research attributes.

        Args:
            - class_names (list): The class names for the research
                attributes.
        """
        BinaryPlotter.__init__(self)
        _ResearcherBase.__init__(self, "binary", class_names)


class MultiClassResearcher(_ResearcherBase, MultiClassPlotter):
    """
    The MultiClassResearcher class inherits from _ResearcherBase and
    MultiClassPlotter to provide functionalities for multi-class image
    classification research.
    """

    def __init__(self, class_names):
        """
        Initializes the MultiClassResearcher by calling initializers from
        inherited classes and synchronizing research attributes.

        Args:
            - class_names (list): The class names for the research
                attributes.
        """
        MultiClassPlotter.__init__(self)
        _ResearcherBase.__init__(self, "multi_class", class_names)
