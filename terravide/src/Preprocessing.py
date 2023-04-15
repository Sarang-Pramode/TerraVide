import laspy
import numpy as np
import pandas as pd
#import open3d as o3d


def Read_lasFile(filepath):
    """Wrapper function which runs laspy.read(lasfilepath)

    Args:
        filepath (string): Where is the .las file located

    Returns:
        las object: las object to read
    """
    return laspy.read(filepath)

def Create_lasFileDataframe(lasfileObject):
    """Take a lasfile object after reading <filename>.las and convert into a Pandas Dataframe
    Columns Stored = {'X','Y','Z','return_number','number_of_returns'}
    Coordinates are in ft 

    Args:
        lasfileObject (_type_): lasfile Object after running Read_lasFile(filepath) function

    Returns:
        lidar_Dataframe: Pandas Dataframe of lidar points as well as return number and number of returns for each data point
    """

    #Making a datframe from the lidar data
    Xscale = lasfileObject.header.x_scale
    Yscale = lasfileObject.header.y_scale
    Zscale = lasfileObject.header.z_scale

    Xoffset = lasfileObject.header.x_offset
    Yoffset = lasfileObject.header.y_offset
    Zoffset = lasfileObject.header.z_offset

    lidarPoints = np.array(
        ( 
        (lasfileObject.X*Xscale)/3.28 + Xoffset,  # convert ft to m and correct measurement
        (lasfileObject.Y*Yscale)/3.28 + Yoffset,
        (lasfileObject.Z*Zscale)/3.28 + Zoffset,
        lasfileObject.classification,
        lasfileObject.return_number, 
        lasfileObject.number_of_returns)).transpose()
    lidar_df = pd.DataFrame(lidarPoints , columns=['X','Y','Z','classification','return_number','number_of_returns'])

    #Filtering out noise
    lidar_df = lidar_df[lidar_df["classification"] != 18] #removing high noise
    lidar_df = lidar_df[lidar_df["classification"] != 7] #removing  noise

    #Raw point cloud data
    rawPoints = np.array((
        ((lidar_df.X)*(Xscale)) + Xoffset, # convert ft to m
        (lidar_df.Y)*(Yscale) + Yoffset, #convert ft to m
        (lidar_df.Z)*(Zscale) + Zoffset
    )).transpose()

    return lidar_df, rawPoints

def Get_MRpoints(lidar_Dataframe):
    """Filter Multiple Return points from lidar Dataframe

    Args:
        lidar_Dataframe (Pandas Dataframe): lidar_Dataframe: Pandas Dataframe of lidar points as well as return number and number of returns for each data point

    Returns:
        Pandas Dataframe: Filtered points with number of returns > 0
    """
    return lidar_Dataframe[lidar_Dataframe['number_of_returns'] - lidar_Dataframe['return_number'] > 0 ]

def Get_SRpoints(lidar_Dataframe):
    """Filter Single Return points from lidar Dataframe

    Args:
        lidar_Dataframe (Pandas Dataframe): lidar_Dataframe: Pandas Dataframe of lidar points as well as return number and number of returns for each data point

    Returns:
        Pandas Dataframe: Filtered points with number of returns = 1
    """
    return lidar_Dataframe[lidar_Dataframe['number_of_returns'] - lidar_Dataframe['return_number'] == 0 ]


class lasTile:

    #initialize the raw tile by default unless specified
    def __init__(self,LiDAR_Dataframe, TileDivision) -> None:
        """Initialize lasTile class object to perform preprocessing

        Args:
            LiDAR_Dataframe (Pandas Dataframe): input a pandas dataframe with lidar data
            TileDivision (int, optional): Number of divisions to divide the tile into, TileDivision= 10 divides the Tile into 100 smaller tiles. Defaults to 1.
        """
        self.lidar_Dataframe = LiDAR_Dataframe
        self.TileDivision = TileDivision

        #store Get_subtileArray() result
        self.rows, self.cols = (self.TileDivision, self.TileDivision)
        self.Matrix_Buffer =  [[0]*self.cols for _ in range(self.rows)]

        self.Matrix_BufferFilled = False

    def Get_TileBounds(self):
        """Get bounding values of tiles

        Returns:
            X.max, X.min, Y.max, Y.min: Bounding Values in XY plane
        """
        #Get Max and Min Bounds of Current Las_Dataframe
        return self.lidar_Dataframe.X.max(), self.lidar_Dataframe.X.min(), self.lidar_Dataframe.Y.max(), self.lidar_Dataframe.Y.min()
    

    def Get_SubTileDimensions(self):
        """Get dimensions of subtile

        Returns:
            X_div_len, Y_div_len: length, breadth of subtile
        """

        #Taking a smaller portion of the lidar tile
        
        #Get Max and Min Bounds of Current Las_Dataframe
        X_max , X_min, Y_max , Y_min = self.Get_TileBounds()

        #Store how many subtiles the Las_Dataframe has to be divided into
        X_axis_tile_divisor = self.TileDivision #in m - indicates the number of tiles you want to divide the tiles into
        Y_axis_tile_divisor = self.TileDivision #in m

        #Get X, Y axis Length and Breadth of the Tile respectively 
        X_diff = X_max - X_min
        Y_diff = Y_max - Y_min

        #Get dimensions of each subtile
        X_div_len = X_diff/X_axis_tile_divisor
        Y_div_len = Y_diff/Y_axis_tile_divisor


        return X_div_len, Y_div_len



    def Get_subtile(self, X_div_len, Y_div_len, row_ID, col_ID):
        """Get X,Y,Z points of specific lidar tile

        Args:
            X_div_len (int): Length of subtile
            Y_div_len (int): Breadth of subtile
            row_ID (int): row index of subtile in Tile Matrix
            col_ID (int): column index of subtile

        Returns:
            Slice of lidar_Dataframe
        """

        #Get Max and Min Bounds of Entire Las_Dataframe
        _ , X_min, _ , Y_min = self.Get_TileBounds()

        #Set Subtile Bounds
        xsub_min = X_min + row_ID*X_div_len
        xsub_max = X_min + row_ID*X_div_len + X_div_len
        ysub_min = Y_min + col_ID*Y_div_len
        ysub_max = Y_min + col_ID*Y_div_len + Y_div_len

        subtile_df = self.lidar_Dataframe[ #Store each subset of the tile
            (
                self.lidar_Dataframe['X'].between(xsub_min, xsub_max, inclusive=False) & 
                self.lidar_Dataframe['Y'].between(ysub_min, ysub_max, inclusive=False)
            )
        ]


        return subtile_df

    def Get_subtileArray(self):
        """Return a 2D matrix buffer of lidar subtiles indexed by row and column

        Returns:
            Matrix Buffer: 2d numpy array of size Nx3 
        """

        X_div_len, Y_div_len = self.Get_SubTileDimensions()

        for row_ID in range(self.rows):
            for col_ID in range(self.cols):

                self.Matrix_Buffer[row_ID][col_ID] = self.Get_subtile(X_div_len, Y_div_len, row_ID, col_ID)
        
        #Update Matrix Buffer filled
        self.Matrix_BufferFilled = True
        
        return self.Matrix_Buffer
















