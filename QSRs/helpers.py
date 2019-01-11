
def rec2intervals(rec1, rec2):
    # Accepts 2 rectangle coordinates in form of x y width height, and returns the pairwise set of intervals as required
    # core-9 QSRs

    is1x = rec1['x'] - rec1['width'] / 2
    ie1x = rec1['x'] + rec1['width'] / 2

    is2x = rec2['x'] - rec2['width'] / 2
    ie2x = rec2['x'] + rec2['width'] / 2

    is1y = rec1['y'] - rec1['height'] / 2
    ie1y = rec1['y'] + rec1['height'] / 2

    is2y = rec2['y'] - rec2['height'] / 2
    ie2y = rec2['y'] + rec2['height'] / 2

    return is1x, ie1x, is2x, ie2x, is1y, ie1y, is2y, ie2y