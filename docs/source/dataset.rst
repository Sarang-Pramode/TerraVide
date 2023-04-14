Dataset Module
==============

This module is used to download anf manipulate the data downloaded from an FTP server

It prepares the data to be used by the other modules

The data is downloaded from the FTP server and stored in a local directory

Usage
-----

To import the module

.. code-block:: python

    import terravide.src.dataset as dataset

API
---

Delete_File
~~~~~~~~~~~

.. function:: Delete_File(file_path: str) -> None

   Deletes the file at the specified file path. If the file does not exist, a message is printed indicating that the file was not found.

   :param file_path: The path to the file that should be deleted.
   :type file_path: str

   :returns: None

Usage
-----

Here is an example usage of the `Delete_File` function:

.. code-block:: python

   import terravide.src.dataset as dataset

   file_path = "/path/to/myfile.txt"
   dataset.Delete_File(file_path)

This will delete the file located at `file_path`, or print a message indicating that the file was not found if it does not exist.
