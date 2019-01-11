import helpers
def compute_Indu_relations(scene):
    # Takes as input a scene object from the Scene class and computes INDU relations between every pairwise object
    # within that scene. RETURNS: a dictionary of object pair as key and corresponding INDU relation in x direction
    # and y direction. CURRENTLY ONLY COMPUTING IN 2D plane.

    obj_pairs = []
    objs = scene.get_objects()
    for i in range(len(objs)):
        for j in range(i+1 , len(objs)):
            obj_pairs.append((objs[i],objs[j]))

    relations = {}
    for obj1, obj2 in obj_pairs:
        # Call the 3d version of the get info method to return x y z when needed
        obj1_info = obj1.get_2D_info()
        obj2_info = obj2.get_2D_info()

        is1x, ie1x, is2x, ie2x, is1y, ie1y, is2y, ie2y = helpers.rec2intervals(obj1_info,obj2_info)

        relX = _Indu_relations(is1x, ie1x, is2x, ie2x, type = 'numeric')
        relY = _Indu_relations(is1y, ie1y, is2y, ie2y, type = 'numeric')

        rel_key = obj1.get_name()+'/'+obj2.get_name()
        relations[rel_key] = [relX,relY]
        # returned as a tuple with first element as numeric and the second as categorical string representation

    return relations





def _Indu_relations(is1,ie1,is2,ie2, type):
#COMPUTEINDUREL Basic indu relations, where relative lengths of two
#intervals decide on the corresponding qualitative relation as either being
#equal , larger or shorter
#   Detailed explanation goes here
# induS : string categorical variable

    if abs(is1-ie1) == abs(is2-ie2):
        indu = 1
        induS = '='
    elif abs(is1-ie1) < abs(is2-ie2):
        indu = 2
        induS = '<'
    else:
        indu = 3
        induS = '>'

    if type == 'numeric':
        return indu
    elif type == 'categorical':
        return induS
