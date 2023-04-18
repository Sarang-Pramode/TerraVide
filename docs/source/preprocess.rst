PreProcessing Module
=====================

The PreProcessing module contains functions for preprocessing LiDAR data in LAS format.

To import the module

.. code-block:: python

    import terravide.src.PreProcessing as LFP

Module Dependencies
-------------------

The PreProcessing module has the following dependencies:

* :mod:`numpy`
* :mod:`pandas`
* :mod:`laspy`

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

Get_SRpoints
~~~~~~~~~~~~

.. function:: Get_SRpoints(lidar_Dataframe: pd.DataFrame) -> pd.DataFrame

   Filter Single Return points from a lidar data frame.

   :param lidar_Dataframe: Pandas DataFrame of lidar points as well as return number and number of returns for each data point.
   :type lidar_Dataframe: pandas DataFrame

   :returns: Filtered points with number of returns = 1 as a pandas DataFrame.


LasTile Class
~~~~~~~~~~~~~

.. autoclass:: PreProcessing.lasTile
   :members:
   :undoc-members:

   The `lasTile` class provides methods for preprocessing and dividing a LiDAR point cloud data tile into sub-tiles. The constructor takes two arguments: 
   
   `LiDAR_Dataframe`: A Pandas Dataframe object containing the LiDAR point cloud data.
   
   `TileDivision`: An integer specifying the number of divisions to divide the tile into. The default value is 1, which means the tile is not divided.

   Class attributes:
   
    lidar_Dataframe : Pandas DataFrame
      A Pandas Dataframe object containing the LiDAR point cloud data.
      
    TileDivision : int
      An integer specifying the number of divisions to divide the tile into. The default value is 1, which means the tile is not divided.
   
    rows : int
      The number of rows in the `Matrix_Buffer` 2D array.
   
    cols : int
      The number of columns in the `Matrix_Buffer` 2D array.
   
    Matrix_Buffer : 2D list
      A 2D list of `lasTile` objects representing the sub-tiles of the tile.
      
    Matrix_BufferFilled : bool
      A boolean indicating whether the `Matrix_Buffer` 2D list has been filled with `lasTile` objects representing the sub-tiles of the tile. The default value is False.


   Class methods:

    Get_TileBounds()
      Get bounding values of tiles.

      :returns: A tuple `(X_max, X_min, Y_max, Y_min)` containing the maximum and minimum values of X and Y coordinates.

   Get_SubTileDimensions()
      Get the dimensions of the subtiles.

      :returns: A tuple `(X_div_len, Y_div_len)` containing the length and breadth of subtiles.

   Get_subtile(X_div_len, Y_div_len, row_ID, col_ID)
      Get X, Y, Z points of specific lidar tile.

      :param X_div_len: The length of the subtile.
      :type X_div_len: int

      :param Y_div_len: The breadth of the subtile.
      :type Y_div_len: int

      :param row_ID: The row index of the subtile in the tile matrix.
      :type row_ID: int

      :param col_ID: The column index of the subtile in the tile matrix.
      :type col_ID: int

      :returns: A slice of the lidar_Dataframe.

   Get_subtileArray()
      Return a 2D matrix buffer of lidar subtiles indexed by row and column.

      :returns: A 2D numpy array of size Nx3.

Here is an example usage of the `lasTile` class:


.. code-block:: python

   import pandas as pd
   from terravide.src.PreProcessing import lasTile

   # Load the LiDAR data into a Pandas DataFrame
   df = pd.read_csv('lidar_data.csv')

   # Create an instance of the lasTile class
   tile = lasTile(df, TileDivision=10)

   # Get the bounding values of the tiles
   X_max, X_min, Y_max, Y_min = tile.Get_TileBounds()

   # Get the dimensions of the subtiles
   X_div_len, Y_div_len = tile.Get_SubTileDimensions()

   # Get a subtile of the LiDAR data
   subtile_df = tile.Get_subtile(X_div_len, Y_div_len, row_ID=0, col_ID=0)

   # Get a matrix buffer of the LiDAR subtiles
   matrix_buffer = tile.Get_subtileArray()





