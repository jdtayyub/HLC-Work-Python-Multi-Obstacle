

class Object:
    """Class defining any physical object in 3 dimensions
    Values of the abstract properties
        * **_x,_y,_z** = "Center point of an object"
        * **_objects** = "a dictionary of objects of the 'physical object' class"
    Members
        * ** ** ():
    """
    dimension = []  # Static property of each object
    _name = ''
    _x = 0
    _y = 0

    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y

    def get_name(self):
        return self._name



