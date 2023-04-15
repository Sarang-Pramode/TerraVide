PreProcessing Module
=====================

The PreProcessing module contains functions for preprocessing LiDAR data in LAS format.

To import the module

.. code-block:: python

    import terravide.src.PreProcessing as LFP

Module Dependencies
-------------------

The PreProcessing module has the following dependencies:

:mod:laspy
:mod:numpy
:mod:pandas

These modules must be installed before using the functions in this module.

API
---

Read_lasFile
~~~~~~~~~~~~

.. function:: Read_lasFile(filepath: str) -> laspy.File

   Reads a LAS file and returns a laspy File object.

   :param filepath: The path to the LAS file to be read.
   :type filepath: str

   :returns: A laspy File object.

Here is an example of how to use the `Read_lasFile` function:

.. code-block:: python

   import terravide.src.PreProcessing as LFP

   filepath = "/path/to/myfile.las"
   lasfile = LFP.Read_lasFile(filepath)

This will read the LAS file located at `filepath` and return a laspy File object.

