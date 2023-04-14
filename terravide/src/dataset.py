# Notes : Script to Download FTP files and store in a directory

from multiprocessing import Pool
from ftplib import FTP
import os
from os import path

########################################################################################################
#    FTP functions
########################################################################################################

def FTP_download_lasfile(filename, datayear=2017, folderpath="FTP_files/"):
    """Downlaod a las file from ftp.gis.ny.gov

    Args:
        filename (string): lasfile to download from ftp server
        datayear (_type_): which year to look at , 2017, 2021
        folderpath (_type_): where to download the file into

    Returns:
        None
    """

    assert datayear in [2017,2021], "NYC recorded lidar data only during 2017 and 2021, default is 2021"

    domain = 'ftp.gis.ny.gov'
    ftp_datadir = None
    if datayear == 2017:
        ftp_datadir =  'elevation/LIDAR/NYC_TopoBathymetric2017'
        folderpath_subdir = folderpath + "NYC_2017/"
    elif datayear == 2021:
        ftp_datadir =  'elevation/LIDAR/NYC_2021'
        folderpath_subdir = folderpath + "NYC_2021/" 
    
    # Create a new directory because it does not exist
    if not os.path.exists(folderpath_subdir):
        os.makedirs(folderpath_subdir)
        print("FTP Dataset Directory created!")
    
    #Added blocker to not redownload file if already exists
    if (path.exists(folderpath_subdir+filename)):
        print("Filename : ",filename," Exits")
    
    else:
        print("Downloading ",filename," from FTP server")

        #Login to server
        ftp = FTP(domain)  # connect to host, default port
        ftp.login()        # user anonymous, passwd anonymous@ - Loggin in as guest

        #enter data directory
        ftp.cwd(ftp_datadir)

        #download and save file to specified path
        with open(folderpath_subdir+filename, "wb") as file:
            # use FTP's RETR command to download the file
            ftp.retrbinary(f"RETR {filename}", file.write)

        #Close FTP connection
        ftp.close()

    return None

def FTP_GetFileList(datayear=2017):

    assert datayear in [2017,2021], "NYC recorded lidar data only during 2017 and 2021, default is 2021"

    domain = 'ftp.gis.ny.gov'
    ftp_datadir = None
    if datayear == 2017:
        ftp_datadir =  'elevation/LIDAR/NYC_TopoBathymetric2017'
        
    elif datayear == 2021:
        ftp_datadir =  'elevation/LIDAR/NYC_2021'

    #Login to server
    ftp = FTP(domain)  # connect to host, default port
    ftp.login()        # user anonymous, passwd anonymous@ - Loggin in as guest

    #enter data directory
    ftp.cwd(ftp_datadir)
    

    filenames = ftp.nlst() # get filenames within the directory
    return filenames

def FTP_list_files(datayear=2021):
    """List all files in the lidar directory of NYC scans

    Args:
        datayear (int, optional): _description_. Defaults to 2021.

    Returns:
        None: _description_
    """

    assert datayear in [2017,2021], "NYC recorded lidar data only during 2017 and 2021, default is 2021"

    domain = 'ftp.gis.ny.gov'
    ftp_datadir = None
    if datayear == 2017:
        ftp_datadir =  'elevation/LIDAR/NYC_TopoBathymetric2017'
    elif datayear == 2021:
        ftp_datadir =  'elevation/LIDAR/NYC_2021'
    
    #Login to server
    ftp = FTP(domain)  # connect to host, default port
    ftp.login()                     # user anonymous, passwd anonymous@

    #enter data directory
    ftp.cwd(ftp_datadir)

    ftp.retrlines('LIST')

    return None


if __name__ == '__main__':

    DEFAULT_FOLDER_PATH = "Datasets/FTP_files/LiDAR/"
    # Get Year Input from User
    year = int(input("Enter Desired YEAR [2017 and 2021 supported] : "))
    # Get List of filnames on FTP server
    filenames = FTP_GetFileList(year)

    # Prepare arguments

    #Download all files
    #NOTE: This is a very slow process, use only if you want to download all files
    #args = [(i, year,DEFAULT_FOLDER_PATH) for i in filenames]

    #Download a single file
    args = [('25192.las', year,DEFAULT_FOLDER_PATH)]

    print("-------------------------")
    print("--DOWNLOADING FTP FILES--")
    print("-------------------------")

    with Pool(1) as p:

        p.starmap(FTP_download_lasfile,args)


