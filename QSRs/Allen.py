
import helpers

def compute_allen_relations(scene):
    # Takes as input a scene object from the Scene class and computes Allen relations between every pairwise object
    # within that scene. RETURNS: a dictionary of object pair as key and corresponding allen relation in x direction
    # and y direction. CURRENTLY ONLY COMPUTING IN 2D plane.

    x =  [obj.get_name() for obj in scene.get_objects()]
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

        relX = _allen_relation(is1x, ie1x, is2x, ie2x, type = 'numeric')
        relY = _allen_relation(is1y, ie1y, is2y, ie2y, type = 'numeric')

        rel_key = obj1.get_name()+'/'+obj2.get_name()
        relations[rel_key] = [relX,relY]
        # returned as a tuple with first element as numeric and the second as categorical string representation

    return relations

def _allen_relation(is1, ie1, is2, ie2, type):
    # types (int, int, int, int) -> int, string
    # Takes in two intervals defined by the start and end point is and ie. Return the corresponding allen's relation
    # between the intervals

    if is2 - 1 == ie1:
        rel = 2 # 'meets'
        relS = 'm'

    elif is1 - 1 == ie2:
        rel = 11 # 'metby'
        relS = 'mi'

    elif is1 == is2 and ie1 == ie2:
        rel = 13 # 'equal'
        relS = 'e'

    elif is2 > ie1:
        rel = 1 # 'before'
        relS = 'b'

    elif is1 > ie2:
        rel = 12 # 'after'
        relS = 'a'

    elif ie1 >= is2 and ie1 < ie2 and is1 < is2:
        rel = 3 # 'overlaps'
        relS = 'o'

    elif ie2 >= is1 and ie2 < ie1 and is2 < is1:
        rel = 10 # 'overlapped_by'
        relS = 'oi'

    elif is1 > is2 and ie1 < ie2:
        rel = 5 # 'during'
        relS = 'd'

    elif is1 < is2 and ie1 > ie2:
        rel = 8 # 'contains'
        relS = 'c'

    elif is1 == is2 and ie1 < ie2:
        rel = 4 # 'starts'
        relS = 's'

    elif is1 == is2 and ie1 > ie2:
        rel = 9 # 'started_by'
        relS = 'si'

    elif ie1 == ie2 and is2 < is1:
        rel = 6 # 'finishes'
        relS = 'f'

    elif ie1 == ie2 and is2 > is1:
        rel = 7 # 'finished_by'
        relS = 'fi'

    if type == 'numeric':
        return rel
    elif type == 'categorical':
        return relS
