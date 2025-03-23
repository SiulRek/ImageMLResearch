.. _Modules_Shared_Attributes:

Shared Attributes
-----------------------------------------------

Description
+++++++++++


The seamless interaction between research modules is enabled by shared attributes defined in the ``ResearchAttributes`` class. This class contains attributes that are used across the research modules through inheritance.


Class
++++++++++++++++++++++++

.. class:: ResearchAttributes(label_type=None, class_names=None)

    Store attributes shared between modules in the research package.

    .. method:: __init__(label_type=None, class_names=None)

        Initialize the ResearchAttributes class.

        :param label_type: The type of labels used: 'binary', 'multi_class', 'multi_label',
                           'multi_label_multi_class', 'object_detection'. If None, label_manager is set to None.
        :type label_type: str or None
        :param class_names: The list of class names.
        :type class_names: list or None

    .. _ResearchAttributes_datasets_container:
    .. attribute:: datasets_container

        Dictionary containing datasets. When creating new datasets, 'complete_dataset' is added;
        when split, 'train_dataset', 'val_dataset', and 'test_dataset' are added.

        :type: dict

    .. _ResearchAttributes_label_manager:
    .. attribute:: label_manager

        LabelManager instance for handling labels.

        :type: LabelManager

    .. _ResearchAttributes_outputs_container:
    .. attribute:: outputs_container

        Dictionary containing outputs in the form of tuples (y_true, y_pred).  
        Keys follow the pattern: dataset name with 'dataset' replaced by 'outputs'.

        :type: dict

    .. _ResearchAttributes_model:
    .. attribute:: model

        The Keras model instance.

        :type: tf.keras.Model

    .. _ResearchAttributes_training_history:
    .. attribute:: training_history

        Dictionary tracking the training history of the model after fitting.

        :type: dict

    .. _ResearchAttributes_evaluation_metrics:
    .. attribute:: evaluation_metrics

        Tracked evaluation metrics of the model after evaluating.
        Format: {Set_Name: {Metric: Value}}.

        :type: dict

    .. _ResearchAttributes_figures:
    .. attribute:: figures

        Dictionary containing tracked figures.
        Format: {figure_name: figure}.

        :type: dict

    .. _ResearchAttributes_synchronize_research_attributes:
    .. method:: synchronize_research_attributes(research_attributes)

        Synchronize research attributes with another ResearchAttributes instance.

        :param research_attributes: The instance to synchronize with.
        :type research_attributes: ResearchAttributes

    .. _ResearchAttributes_reset_research_attributes:
    .. method:: reset_research_attributes(except_datasets=False)

        Reset research attributes while preserving the label manager.

        :param except_datasets: If True, datasets are not reset. Defaults to False.
        :type except_datasets: bool
