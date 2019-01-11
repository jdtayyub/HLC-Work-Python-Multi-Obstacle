

class Scene2D:
    """Class defining the environment
    Values of the abstract properties
        * **_x,_y,_z,_width,_height,_depth** = "Dimensions of the scene"
        * **_objects** = "a dictionary of objects of the 'physical object' class"
    Members
        * **_visualise** ():
    """
    _x = 0
    _y = 0

    _width = 0
    _height = 0

    _objects = []

    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def add_object(self, obj):
        if "2d" not in obj.dimension:
            print('Only 2D objects can be added in a 2D scene')
            return
        self._objects.append(obj)
        return self


    def get_2D_info(self):
        # Function returning only 2D information (coords & dims) of the scene, In case of calling the function from the
        # Scene3D class, z and depth are omitted and only a projection over x,y is returned
        return {'x':self._x, 'y':self._y,
                'width':self._width, 'height':self._height}

    def get_objects(self):
        return self._objects

    def get_obj_names(self):
        # Display function to output the names of the objects currently in the present scene object for 2d and 3d
        # INCOMPLETE
        return self

    def visualise(self):
        return self


class Scene3D(Scene2D):
    """Class defining the 3D environment
        Inheritance: Scene2D class which defines the 2D Environment

        Values of the abstract properties
            * **_x,_y,_z,_width,_height,_depth** = "Dimensions of the scene"
            * **_objects** = "a dictionary of objects of the 'physical object' class"
        Members
            * **_visualise** ():
    """

    _z = 0
    _depth = 0

    _objects = [] #List of objects in the scene as objects of objects

    def __init__(self, x, y, z, width, height, depth):
        Scene2D.__init__(self, x, y, width, height)
        self._z = z
        self._depth = depth

    def add_object(self, obj):

        if "3d" not in obj.dimension:
            print('Errors: Only 3D objects can be added in a 3D scene.')
            return

        self._objects.append(obj)

    def get_3D_info(self):
        #Function returning 3D information (coords & dims) of the scene
        return {'x':self._x, 'y':self._y, 'z':self._z,
                'width':self._width, 'height':self._height, 'depth':self._depth}



    def visualise(self):
        return self
