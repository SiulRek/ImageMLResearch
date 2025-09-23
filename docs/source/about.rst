.. include:: header.rst

.. _About:


.. _About_Installation:

Installation
-----------------------------------------------
This library supports Python 3.10–3.12.

To install the library, use the following command:

.. code-block:: bash

  pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ imlresearch

----

.. _About_Architecture:

Architecture
-----------------------------------------------

.. figure:: images/framework_uml.jpg
    :alt: Framework Architecture
    :align: center

The framework allocates its low-level responsibilities to five research modules listed below:
  
* :ref:`Data Handling <Modules_Data_Handling>`  
  Converts raw input data into a format suitable for model training.

* :ref:`Preprocessing <Modules_Preprocessing>`  
  Prepares data for training, including operations like resizing, normalization, and augmentation.

* :ref:`Plotting <Modules_Plotting>`  
  Visualizes data, model performance, and results.

* :ref:`Training <Modules_Training>`  
  Manages model training, predictions, and evaluations.

* :ref:`Experimenting <Modules_Experimenting>`  
  Oversees the experiment lifecycle, manages trials, stores assets in an experiment directory, and generates experiment reports.


To facilitate seamless interaction between the research modules, a high-level class named ``Researcher`` is constructed using inheritance or composition.

----

.. _About_License:

License and Copyright
----------------------
|IMLResearch| is available under the open-source :title:`MIT` license. Please read the full text of the :title:`MIT` license agreement, available in the distribution material (file LICENSE) and `here <https://opensource.org/licenses/MIT>`_, to ensure that your use case complies with the guidelines of the license.
