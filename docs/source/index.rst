.. include:: header.rst

.. This is the TOC in the sidebar!

.. raw:: html

   <style>

      .toc-drawer {
         display: none;
      }

      .main .content {
         width:  100% !important;
      }

   </style>

Welcome to |IMLResearch| |version|
===================================

|IMLResearch| is a toolkit to help with image-based machine learning projects using Python. Built on `Keras <https://keras.io/>`_ with `TensorFlow <https://www.tensorflow.org/>`_, this library provides functions for data handling, preprocessing, visualization, and more. These functions are combined into a single ``Researcher`` class to make experimentation easier and more efficient. Key features include hyperparameter tuning and experiment report generation. Note that this toolkit is specifically tailored for image classification tasks and does not support regression problems.

|IMLResearch| is hosted on `GitHub <https://github.com/SiulRek/ImageMLResearch/tree/api-development>`_ and registered on `PyPI <https://test.pypi.org/project/imlresearch/>`_. This project was developed under the FFG Coin ENDLESS Research Project.

.. .. toctree::
..    :maxdepth: 2
..    :caption: Contents:


.. toctree::
   :caption: About
   :maxdepth: 1

   about.rst


.. toctree::
   :caption: Low-Level Modules
   :maxdepth: 1

   shared_attributes
   data_handling
   preprocessing
   plotting
   training
   experimenting

.. toctree::
   :caption: High-Level API
   :maxdepth: 1
   
   research

.. toctree::
   :caption: How to Guide
   :maxdepth: 1

   recipes.rst


.. toctree::
   :caption: Other
   :maxdepth: 1

   other.rst
