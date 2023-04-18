Ground Module
=============

The GroundClassification module contains a class GP_class which implements an algorithm for ground plane classification in LiDAR point cloud data.

To import the module

.. code-block:: python

    import terravide.src.GroundClassification as GP

Module Dependencies
-------------------

The `GroundClassification` module has the following dependencies:

* :mod:`numpy`

These modules must be installed before using the functions in this module.


API
---

GP Class
~~~~~~~~

.. autoclass:: GroundClassification.GP_class
   :members:
   :undoc-members:

   The GP class provides methods for ground plane classification using LiDAR point cloud data. The constructor takes one argument, `ground_H_thresh_perc`, which is the height threshold of the region to look at from the lowest point in the tileset. The default value is 0.1.

   The class provides the following method:

   Extract_GroundPoints(lidarSubtilePoints)
      Extract ground points from a tile points.

      :param lidarSubtilePoints: Numpy array of size Nx3 containing the coordinates of LiDAR points.
      :type lidarSubtilePoints: numpy array
      :returns: Two numpy arrays: `Ground_Points` containing classified ground points and `Not_ground_points` containing non ground points.
   
   
Here is an example of how to use the `GP_class` class:

.. code-block:: python

   import numpy as np
   from terravide.src.GroundClassification import GP_class as GP
   
   # Create an instance of the GP_class
   gp = GP(ground_H_thresh_perc=0.2)
   
   # Create a numpy array of LiDAR points
   lidarSubtilePoints = np.random.rand(100, 3)
   
   # Call the Extract_GroundPoints method to classify ground points
   ground_points, not_ground_points = gp.Extract_GroundPoints(lidarSubtilePoints)
   
   # Print the classified ground and non ground points
   print("Ground Points: ", ground_points)
   print("Not Ground Points: ", not_ground_points)
