Dataset Module
==============

This module is used to download anf manipulate the data downloaded from an FTP server

It prepares the data to be used by the other modules

The data is downloaded from the FTP server and stored in a local directory

To import the module

.. code-block:: python

    import terravide.src.dataset as dataset

Module Dependencies
-------------------

The `terrvide.src.dataset` module has the following dependencies:

* :mod:`multiprocessing.Pool`
* :mod:`ftplib.FTP`
* :mod:`os`
* :mod:`os.path`

These modules must be installed before using the functions in this module.

API
---

FTP_download_lasfile
~~~~~~~~~~~~~~~~~~~~

.. function:: FTP_download_lasfile(filename, datayear=2017, folderpath="FTP_files/") -> None

   Downloads a las file from ftp.gis.ny.gov.

   :param filename: The name of the las file to download from the FTP server.
   :type filename: str
   :param datayear: The year of the data (2017 or 2021). Defaults to 2017.
   :type datayear: int
   :param folderpath: The path to the folder where the file should be downloaded. Defaults to "FTP_files/".
   :type folderpath: str

   :returns: None.


Here is an example usage of the `FTP_download_lasfile` function:

.. code-block:: python

   import terravide.src.dataset as dataset

   filename = "myfile.las"
   datayear = 2017
   folderpath = "/path/to/my/folder/"
   dataset.FTP_download_lasfile(filename, datayear, folderpath)

This will download the specified las file from the FTP server and save it to the folder located at `folderpath/NYC_2017/`, or `folderpath/NYC_2021/` if `datayear` is set to 2021.


FTP_GetFileList
~~~~~~~~~~~~~~~

.. function:: FTP_GetFileList(datayear=2017) -> list

   Gets a list of all files in the FTP directory of NYC scans for the specified year.

   :param datayear: The year of the data (2017 or 2021). Defaults to 2017.
   :type datayear: int

   :returns: A list of filenames in the FTP server.


Here is an example usage of the `FTP_GetFileList` function:

.. code-block:: python

   import terravide.src.dataset as dataset

   datayear = 2017
   filenames = dataset.FTP_GetFileList(datayear)
   print(filenames)

This will print a list of all files in the FTP directory of NYC scans for the year 2017.


FTP_list_files
~~~~~~~~~~~~~~

.. function:: FTP_list_files(datayear=2021) -> None

   Lists all files in the lidar directory of NYC scans for the specified year.

   :param datayear: The year of the data (2017 or 2021). Defaults to 2021.
   :type datayear: int

   :returns: Prints to console.


Here is an example usage of the `FTP_list_files` function:

.. code-block:: python

   import terravide.src.dataset as dataset

   datayear = 2021
   dataset.FTP_list_files(datayear)

This will list all files in the lidar directory of NYC scans for the year 2021.

Get_filenames
~~~~~~~~~~~~~

.. function:: Get_filenames(folder_path: str, year: int) -> list

   Gets a list of filenames in a folder generated by the `FTP_download_lasfile` function for the specified year.

   :param folder_path: The path to the folder containing the files.
   :type folder_path: str
   :param year: The subfolder name designated by the year of the data (e.g. 2017, 2021).
   :type year: int

   :returns: A list of filenames in the specified folder.

Here is an example usage of the `Get_filenames` function:

.. code-block:: python

   import terravide.src.dataset as dataset

   folder_path = "/path/to/my/folder"
   year = 2021
   filenames = dataset.Get_filenames(folder_path, year)
   print(filenames)

This will print a list of filenames in the folder located at `folder_path/NYC_2021/`, which were generated by the `FTP_download_lasfile` function.

Delete_File
~~~~~~~~~~~

.. function:: Delete_File(file_path: str) -> None

   Deletes the file at the specified file path. If the file does not exist, a message is printed indicating that the file was not found.

   :param file_path: The path to the file that should be deleted.
   :type file_path: str

   :returns: None

Here is an example usage of the `Delete_File` function:

.. code-block:: python

   import terravide.src.dataset as dataset

   file_path = "/path/to/myfile.txt"
   dataset.Delete_File(file_path)

This will delete the file located at `file_path`, or print a message indicating that the file was not found if it does not exist.
