class Circle(Object):
    """Class defining any physical object in 3 dimensions
            Values of the abstract properties
                * **_x,_y,_z** = "Center point of an object"
                * **_objects** = "a dictionary of objects of the 'physical object' class"
            Members
                * ** ** ():
        """
    dimension = ['2d', '3d']
    _radius = 0

    def __init__(self, x, y, radius):
        Object.__init__(self, x, y)
        _radius = radius

