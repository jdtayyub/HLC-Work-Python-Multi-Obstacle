from object import Object
import pandas as pd
class Rectangle(Object):
    """Class defining any physical object in 3 dimensions
        Values of the abstract properties
            * **_x,_y,_z** = "Center point of an object"
            * **_objects** = "a dictionary of objects of the 'physical object' class"
        Members
            * ** ** ():
    """
    dimension = ['2d']
    _width = 0
    _height = 0

    _track_2D_df = pd.DataFrame()

    def __init__(self, name, x, y, width, height):
        Object.__init__(self, name, x, y)
        self._width = width
        self._height = height

    def get_2D_info(self):
        # Function returning only 2D information (coords & dims) of the scene, In case of calling the function from the
        # Scene3D class, z and depth are omitted and only a projection over x,y is returned
        return {'x': self._x, 'y': self._y,
                'width': self._width, 'height': self._height}

    def add_track(self, track_df):
        # A function to optionally add the track of the object. Track to be added as a pandas data frame of coords and
        # dimensions for each frame.
        self._track_2D_df = track_df

    def get_2D_track(self):
        return self._track_2D_df