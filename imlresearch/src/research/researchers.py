import warnings

from imlresearch.src.data_handling.data_handler import DataHandler
from imlresearch.src.experimenting.experiment import Experiment
from imlresearch.src.plotting.plotters.binary_plotter import BinaryPlotter
from imlresearch.src.plotting.plotters.multi_class_plotter import (
    MultiClassPlotter,
)
from imlresearch.src.preprocessing.image_preprocessor import ImagePreprocessor
from imlresearch.src.research.attributes.research_attributes import (
    ResearchAttributes,
)
from imlresearch.src.training.trainer import Trainer
from imlresearch.src.utils.general.batch_utils import is_batched


class _ResearcherBase(DataHandler, Trainer):
    """
    A high-level interface for conducting image-based machine learning
    experiments.

    This class inherits functionalities from DataHandler, Trainer, and
    ResearchAttributes. It also synchronizes research attributes from a
    source instance during initialization.
    """

    def __init__(self, label_type, class_names):
        """
        Initialize the Researcher with necessary attributes and dependencies.

        Parameters
        ----------
        label_type : str
            The label type for the research attributes.
        class_names : list
            The class names for the research attributes.
        """
        assert label_type is not None, (
            "It is recommended to provide a label type."
        )
        # Last one to be initialized overwrites the previous ones in case of
        # conflicts. This should only occur in the case of label_manager.
        Trainer.__init__(self)
        DataHandler.__init__(self)
        ResearchAttributes.__init__(self, label_type, class_names)

        self._preprocessor = ImagePreprocessor()

    @property
    def preprocessor(self):
        """
        Get the image preprocessor instance.

        Returns
        -------
        ImagePreprocessor
            The image preprocessor instance.
        """
        return self._preprocessor

    def run_experiment(
        self,
        directory,
        name,
        description,
        sort_metric="accuracy",
        ask_for_analysis=False,
    ):
        """
        Set up and run an experiment within a context manager.

        Parameters
        ----------
        directory : str
            The directory to save the experiment data.
        name : str
            The name of the experiment.
        description : str
            The description of the experiment for the report.
        sort_metric : str, optional
            The metric to sort the results by, by default "accuracy".
        ask_for_analysis : bool, optional
            Whether to ask AI for analysis, by default False.

        Returns
        -------
        Experiment
            The Experiment context manager instance.
        """
        return Experiment(
            self,
            directory=directory,
            name=name,
            description=description,
            sort_metric=sort_metric,
            ask_for_analysis=ask_for_analysis,
        )

    def apply_preprocessing_pipeline(
        self, pipeline, dataset_names=None, backup=False
    ):
        """
        Apply a preprocessing pipeline to the datasets.

        Parameters
        ----------
        pipeline : list of StepBase
            List of preprocessing steps.
        dataset_names : list, optional
            The dataset names to apply the pipeline to, by default None.
        backup : bool, optional
            Whether to backup all datasets before applying the pipeline,
            by default False.

        Notes
        -----
        It is not supported to apply a preprocessing pipeline on batched
        datasets.
        """
        preprocessor = self._preprocessor
        preprocessor.set_pipe(pipeline)

        if dataset_names is None:
            dataset_names = self._datasets_container.keys()

        if hasattr(self, "backup_datasets") and backup:
            self.backup_datasets()
        elif backup:
            warnings.warn("No backup_datasets method found. Skipping backup.")

        for dataset_name in dataset_names:
            dataset = self._datasets_container[dataset_name]

            if is_batched(dataset):
                raise ValueError(
                    "Applying a preprocessing pipeline on a batched dataset "
                    "is not supported."
                )

            preprocessed_dataset = preprocessor.process(dataset)
            self._datasets_container[dataset_name] = preprocessed_dataset


class BinaryResearcher(_ResearcherBase, BinaryPlotter):
    """
    A researcher class for binary image classification.

    This class inherits from _ResearcherBase and BinaryPlotter to provide
    functionalities for binary image classification research.
    """

    def __init__(self, class_names):
        """
        Initialize the BinaryResearcher.

        Parameters
        ----------
        class_names : list
            The class names for the research attributes.
        """
        BinaryPlotter.__init__(self)
        _ResearcherBase.__init__(self, "binary", class_names)


class MultiClassResearcher(_ResearcherBase, MultiClassPlotter):
    """
    A researcher class for multi-class image classification.

    This class inherits from _ResearcherBase and MultiClassPlotter to
    provide functionalities for multi-class image classification research.
    """

    def __init__(self, class_names):
        """
        Initialize the MultiClassResearcher.

        Parameters
        ----------
        class_names : list
            The class names for the research attributes.
        """
        MultiClassPlotter.__init__(self)
        _ResearcherBase.__init__(self, "multi_class", class_names)
