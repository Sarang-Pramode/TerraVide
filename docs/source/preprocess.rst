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


Create_lasFileDataframe
~~~~~~~~~~~~~~~~~~~~~~~

.. function:: Create_lasFileDataframe(lasfileObject: laspy.File) -> pd.DataFrame

Take a lasfile object after reading `<filename>.las` and convert into a Pandas Dataframe. The columns stored in the dataframe are `{'X','Y','Z','return_number','number_of_returns'}`. The coordinates are in feet.

**Args**:

- `lasfileObject` (_type_): lasfile Object after running `Read_lasFile(filepath)` function.

**Returns**:

- `lidar_Dataframe`: Pandas Dataframe of lidar points as well as return number and number of returns for each data point.

Here is an example of how to use the `Create_lasFileDataframe` function:

.. code-block:: python

    import laspy
    import pandas as pd
    from PreProcessing import Create_lasFileDataframe

    # Read a las file using laspy
    las_file = laspy.read('my_las_file.las')

    # Convert las file to Pandas DataFrame
    lidar_df, rawPoints = Create_lasFileDataframe(las_file)

    # Print the lidar data in the Pandas DataFrame
    print(lidar_df)

Get_MRpoints
~~~~~~~~~~~~

.. function:: Get_MRpoints(lidar_Dataframe: pd.DataFrame) -> pd.DataFrame

   Filters Multiple Return points from a LiDAR DataFrame.

   :param lidar_Dataframe: A Pandas DataFrame containing lidar points and the number of returns for each point.
   :type lidar_Dataframe: pd.DataFrame

   :returns: A filtered Pandas DataFrame containing only the points with multiple returns.


Here is an example usage of the `Get_MRpoints` function:

.. code-block:: python

   import pandas as pd
   import terravide.src.PreProcessing as PreProcessing

   # Create a Pandas DataFrame of LiDAR points
   lidar_df = pd.read_csv("lidar_data.csv")

   # Call the Get_MRpoints function to filter the DataFrame by multiple return points
   filtered_df = PreProcessing.Get_MRpoints(lidar_df)

   # Print the filtered DataFrame
   print(filtered_df)

