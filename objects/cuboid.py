from rectangle import Rectangle
import pandas as pd
class Cuboid(Rectangle):
    """Class defining any physical object in 3 dimensions
            Values of the abstract properties
                * **_x,_y,_z** = "Center point of an object"
                * **_objects** = "a dictionary of objects of the 'physical object' class"
            Members
                * ** ** ():
    """
    dimension = ['3d']
    _z = 0
    _depth = 0
    _track_df = pd.DataFrame()

    def __init__(self, name, x, y, z, width, height, depth):
        Rectangle.__init__(self, name, x, y, width, height)
        self._z = z
        self._depth = depth

    def get_3D_info(self):
        return {'x':self._x, 'y':self._y, 'z':self._z, 'width':self._width, 'height':self._height, 'depth':self._depth}

    def set_coords(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def add_track(self, track_df):
        # A function to optionally add the track of the object. Track to be added as a pandas data frame of coords and
        # dimensions for each frame.
        self._track_3D_df = track_df

        # Add a 2D version of the track to the super rectangle class as well, so it can be retrieved alter
        Rectangle.add_track(self,track_df[['x','y','width','height']])

    def get_3D_track(self):
        return self._track_3D_df

