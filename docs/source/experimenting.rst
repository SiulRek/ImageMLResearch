.. _Modules_Experimenting:

Experimenting
-----------------------------------------------
The Experimenting module provides tools for managing machine learning 
experiments, organizing trials, and analyzing results. It includes the 
``Experiment`` class, which acts as a context manager for conducting and 
tracking experiments efficiently.

----

.. class:: Experiment

    A context manager for managing experiments and trials.

    The ``Experiment`` class facilitates running multiple trials, sorting 
    results, saving logs, and generating experiment reports. It integrates 
    with research attributes for managing datasets, evaluation metrics, and 
    training histories.

    .. method:: __init__(research_attributes: ResearchAttributes, directory: str, name: str, description: str, sort_metric: str = "accuracy", ask_for_analysis: bool = False)

        Initializes the experiment.

        :param research_attributes: Research attributes to be used in the experiment.
        :type research_attributes: ResearchAttributes
        :param directory: Directory where the experiment outputs will be stored.
        :type directory: str
        :param name: Name of the experiment.
        :type name: str
        :param description: Description of the experiment.
        :type description: str
        :param sort_metric: Metric to sort trials. Defaults to "accuracy".
        :type sort_metric: str
        :param ask_for_analysis: Whether to request AI-based experiment analysis.
                                 Defaults to False.
        :type ask_for_analysis: bool

    .. method:: __enter__()

        Sets up the experiment.

        :returns: *(Experiment)* The experiment instance.

    .. method:: get_results()

        Retrieves the current experiment results.

        :returns: *(dict)* A dictionary containing figures, evaluation metrics, and training history.

    .. method:: run_trial(name: str, hyperparameters: dict)

        Runs a trial within the experiment context.

        :param name: The name of the trial.
        :type name: str
        :param hyperparameters: The hyperparameters for the trial.
        :type hyperparameters: dict
        :returns: *(Trial)* The trial instance.

    .. method:: __exit__(exc_type, exc_value, traceback)

        Cleans up and finalizes the experiment.
