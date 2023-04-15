import numpy as np

class GP_class():

    def __init__(self,ground_H_thresh_perc = 0.1) -> None:
        self.ground_H_thresh_perc = ground_H_thresh_perc

    #Ground Plane Classifcation Algorithm
    def Extract_GroundPoints(self,lidarSubtilePoints):
        """Extract ground points from a tile points

        Args:
            lidarSubtilePoints (numpy array of size Nx3): coords of lidar points
            ground_H_thresh_perc (float, optional): height threshold of region to look at from lowest point in tileset. Defaults to 0.1.

        Returns:
            Ground_Points, Not_ground_points: Returns classified ground points and Non ground poitns
        """

        Lpoints = lidarSubtilePoints

        #Ground Seperation Algorithm

        #Get Z values of all points
        z_values = Lpoints[:,2]
        
        if (len(z_values) != 0):
            z_min = np.min(z_values)
            
            #Set Height Threshold for points to consider
            Z_Height_thresh = z_min*self.ground_H_thresh_perc

            #Seperate Ground Points and Non Ground Points
            lowest_points_idx = [idx for idx,record in enumerate(z_values) if record > (z_min) and record < (z_min+Z_Height_thresh) ]
            Ground_Points = Lpoints[lowest_points_idx]

            Other_points_idx =  [idx for idx,record in enumerate(z_values) if record > (z_min+Z_Height_thresh) ]
            Not_ground_points = Lpoints[Other_points_idx]
        
        return Ground_Points, Not_ground_points


    
            