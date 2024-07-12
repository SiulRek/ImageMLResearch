from src.data_handling.data_handler import DataHandler
from src.experimenting.experiment import Experiment
from src.plotting.plotters.binary_plotter import BinaryPlotter
from src.plotting.plotters.multi_class_plotter import MultiClassPlotter
from src.research.attributes.research_attributes import ResearchAttributes
from src.training.trainer import Trainer


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
        ResearchAttributes.__init__(self, label_type, class_names)
        DataHandler.__init__(self)
        Trainer.__init__(self)

    def run_experiment(self, directory, name, description, report_kwargs):
        """
        Sets up and runs an experiment within a context manager.

        Args:
            - directory (str): The directory to save the experiment data.
            - name (str): The name of the experiment.
            - description (str): The description of the experiment.
            - report_kwargs (dict, optional): Additional keyword arguments
                for the report.

        Returns:
            - Experiment: The Experiment context manager instance.
        """
        return Experiment(self, directory, name, description, report_kwargs)


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
        _ResearcherBase.__init__(self, "binary", class_names)
        BinaryPlotter.__init__(self)


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
        _ResearcherBase.__init__(self, "multi_class", class_names)
        MultiClassPlotter.__init__(self)
