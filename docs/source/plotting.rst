.. _Modules_Plotting:

Plotting
-----------------------------------------------
The Plotting module provides tools for visualizing images, text, model
summaries, and training history. It includes a general ``Plotter`` class with 
common visualization methods and specialized subclasses like ``BinaryPlotter`` 
and ``MultiClassPlotter`` for binary and multi-class classification.

----

.. class:: Plotter

    A base class for plotting images, text, model summaries, and training history.

    The ``Plotter`` class provides methods for visualizing research attributes,
    including dataset samples, textual outputs, and model performance.

    .. _Plotter_init:
    .. method:: __init__()

        Initializes the Plotter.
        
    .. _Plotter_plot_text:
    .. method:: plot_text(text: str, **general_plot_kwargs)

        Plots the given text.

        :param text: The text to be plotted.
        :type text: str
        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot. Defaults to "Text".
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the text.

    .. _Plotter_plot_model_summary:
    .. method:: plot_model_summary(**general_plot_kwargs)

        Plots the summary of the given model.

        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot. Defaults to "Model Summary".
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the model summary.

    .. _Plotter_plot_training_history:
    .. method:: plot_training_history(**general_plot_kwargs)

        Plots the training history of the model.

        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot.
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the training history.

----

.. class:: BinaryPlotter

    A specialized plotter for binary classification tasks.

    The ``BinaryPlotter`` extends ``Plotter`` to provide visualization tools
    specifically designed for binary classification problems.

    .. _BinaryPlotter_plot_images:
    .. method:: plot_images(grid_size: tuple = (2, 2))

        Plots a grid of images from a dataset, labeling them with class names.

        :param grid_size: Tuple specifying the grid size as (rows, columns).
                          Defaults to (2,2).
        :type grid_size: tuple
        :returns: *(matplotlib.figure.Figure)* The figure containing the images.

    .. _BinaryPlotter_plot_confusion_matrix:
    .. method:: plot_confusion_matrix(**general_plot_kwargs)

        Plots the confusion matrix for binary classification.

        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot. Defaults to "Confusion Matrix".
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the confusion matrix.

    .. _BinaryPlotter_plot_roc_curve:
    .. method:: plot_roc_curve(**general_plot_kwargs)

        Plots the Receiver Operating Characteristic (ROC) curve.

        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot. Defaults to "ROC Curve".
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the ROC curve.

    .. _BinaryPlotter_plot_pr_curve:
    .. method:: plot_pr_curve(**general_plot_kwargs)

        Plots the Precision-Recall (PR) curve.

        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot. Defaults to "PR Curve".
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the PR curve.

    .. _BinaryPlotter_plot_results:
    .. method:: plot_results(grid_size: tuple = (2, 2))

        Plots the results of a binary classification model.

        :param grid_size: Tuple specifying the grid size as (rows, columns).
                          Defaults to (2,2).
        :type grid_size: tuple
        :returns: *(matplotlib.figure.Figure)* The figure containing the classification results.

----

.. class:: MultiClassPlotter

    A specialized plotter for multi-class classification tasks.

    The ``MultiClassPlotter`` extends ``Plotter`` and provides additional
    visualization tools tailored to multi-class classification.

    .. _MultiClassPlotter_plot_images:
    .. method:: plot_images(grid_size: tuple = (2, 2), **general_plot_kwargs)

        Plots a grid of images from a dataset, labeling them with class names.

        :param grid_size: Tuple specifying the grid size as (rows, columns).
                          Defaults to (2,2).
        :type grid_size: tuple
        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot. Defaults to "Images".
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the images.

    .. _MultiClassPlotter_plot_confusion_matrix:
    .. method:: plot_confusion_matrix(**general_plot_kwargs)

        Plots the confusion matrix for multi-class classification.

        :param general_plot_kwargs: Additional plotting arguments.
                                    - title *(str, optional)*: Title of the plot. Defaults to "Confusion Matrix".
                                    - show *(bool, optional)*: Whether to show the plot. Defaults to False.
        :returns: *(matplotlib.figure.Figure)* The figure containing the confusion matrix.

    .. _MultiClassPlotter_plot_results:
    .. method:: plot_results(grid_size: tuple = (2, 2), prediction_bar: bool = False)

        Plots a grid of images with their true and predicted labels.

        If ``prediction_bar`` is set to True, a bar plot is shown alongside the images
        displaying the predicted probabilities.

        :param grid_size: Tuple specifying the grid size as (rows, columns).
                          Defaults to (2,2).
        :type grid_size: tuple
        :param prediction_bar: Whether to show the predicted probabilities as a bar plot.
                               Defaults to False.
        :type prediction_bar: bool
        :returns: *(matplotlib.figure.Figure)* The figure containing the images and labels.
