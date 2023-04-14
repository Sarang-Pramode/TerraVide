# TerraVide

TerraVide is an open source python package to process large urban environments mapped with LiDAR(Light Detection and Ranging) data.

It offers the ability to enrich raw lidar data and extract individual tree canopies from raw point clouds. Additionally it offers a suite of modules to simulate and analyze the classified enviroment and quantify shade impacts through interactive visualiztions

TerraVide aims to facilitate large-scale forest management and make more robust and generic tree extraction methods with equitable tree planting decisions. The package is designed to be scalable and can handle large datasets with minimal computational overhead.

# Installation

```python
pip install terravide
```

# Usage

### Dataset module
```python
import terravide.src.dataset as dataset

# The dataset module allows you to build a dataset by downloading data from an FTP server

# Default FTP Server - NYC Topobathymetric LiDAR Data (2017)

# List Files in FTP server
FileList = dataset.FTP_list_files(datayear=2021)

# Download Files from FTP server
dataset.FTP_download_lasfile('25192.las')

```

# License

TerraVide is released under the MIT license.



