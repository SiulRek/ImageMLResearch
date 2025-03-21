.. _Modules_Researcher:

Researcher
-----------------------------------------------

Description
+++++++++++

The ``Researcher`` class serves as the high-level API that integrates the core research modules through either inheritance or composition. This design provides flexibility and a structured workflow for users.

The ``Researcher`` class integrates the following submodules (as listed above):

* :ref:`Data Handling <Modules_Data_Handling>` (inheritance)
* :ref:`Preprocessing <Modules_Preprocessing>` (composition)
* :ref:`Plotting <Modules_Plotting>` (inheritance)
* :ref:`Training <Modules_Training>` (inheritance)
* :ref:`Experimenting <Modules_Experimenting>` (composition)

Depending on the classification type, the implementation differs. The framework provides two specialized classes for binary and multi-class classification, namely ``BinaryResearcher`` and ``MultiClassResearcher``. For simplicity, the name ``Researcher`` is used to refer to both classes in this documentation.

Main class
++++++++++

.. class:: Researcher

    A high-level API that integrates core research modules.

    The ``Researcher`` class simplifies machine learning workflows by managing 
    data handling, preprocessing, training, visualization, and experimentation 
    in a unified interface.

    .. method:: __init__()

        Initializes the ``Researcher`` class by integrating all research modules.

    .. _Researcher_run_experiment:
    .. method:: run_experiment(*args, **kwargs)

        Conducts and manages machine learning experiments using the ``Experimenting`` module.

        :param args: Additional arguments for experiment configuration.
        :type args: tuple
        :param kwargs: Keyword arguments for defining experiment parameters.
        :type kwargs: dict
        :returns: *(Experiment)* The experiment instance.

    .. _Researcher_apply_preprocessing_pipeline:
    .. method:: apply_preprocessing_pipeline(*args, **kwargs)

        Applies a sequence of preprocessing steps using the ``Preprocessing`` module.

        :param args: Additional arguments for preprocessing configuration.
        :type args: tuple
        :param kwargs: Keyword arguments defining preprocessing parameters.
        :type kwargs: dict
        :returns: *(Any)* The processed dataset after applying the preprocessing pipeline.


Class Methods
+++++++++++++

For recap, here are all the methods included in the ``Researcher`` class:

- `load_dataset() <DataHandler_load_dataset>`
- `prepare_datasets() <DataHandler_prepare_datasets>`
- `split_dataset() <DataHandler_split_dataset>`
- `save_images() <DataHandler_save_images>`
- `backup_datasets() <DataHandler_backup_datasets>`
- `restore_datasets() <DataHandler_restore_datasets>`
- `apply_preprocessing_pipeline() <Researcher_apply_preprocessing_pipeline>`
- `plot_text() <Plotter_plot_text>`
- `plot_model_summary() <Plotter_plot_model_summary>`
- `plot_training_history() <Plotter_plot_training_history>`
- `set_compiled_model() <Trainer_set_compiled_model>`
- `fit_predict_evaluate() <Trainer_fit_predict_evaluate>`
- `run_experiment() <Researcher_run_experiment>`

For binary classification, the following plotting methods are available:

- `plot_images() <BinaryPlotter_plot_images>`
- `plot_confusion_matrix() <BinaryPlotter_plot_confusion_matrix>`
- `plot_roc_curve() <BinaryPlotter_plot_roc_curve>`
- `plot_pr_curve() <BinaryPlotter_plot_pr_curve>`
- `plot_results() <BinaryPlotter_plot_results>`

For multi-class classification, the following plotting methods are available:

- `plot_images() <MultiClassPlotter_plot_images>`
- `plot_confusion_matrix() <MultiClassPlotter_plot_confusion_matrix>`
- `plot_results() <MultiClassPlotter_plot_results>`