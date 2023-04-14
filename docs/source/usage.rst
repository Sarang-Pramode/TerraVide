Usage
=====

.. _installation:

Installation
------------

To use TerraVide, first install it using pip:

.. code-block:: console

   (.venv) $ pip install TerraVide

.. _usage:

Usage
-----

To use TerraVide, first import it:

.. code-block:: python

   import terravide.src.dataset as dataset

   # The dataset module allows you to build a dataset by downloading data from an FTP server

   # Default FTP Server - NYC Topobathymetric LiDAR Data (2017)

   # List Files in FTP server
   FileList = dataset.FTP_list_files(datayear=2021)

   # Download Files from FTP server
   dataset.FTP_download_lasfile('25192.las')