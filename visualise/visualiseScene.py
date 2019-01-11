#  visualise the motion of the scene by loading the variables from scene_obj_vars TEMPORARILY and plotting
# the scene with motion based on key presses

import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot_cuboid_surface(cube, ax, col):

    center = np.array([cube['x'], cube['y'], cube['z']])
    size = np.array([cube['width'], cube['height'], cube['depth']])
    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point
    o = [a - b / 2 for a, b in zip(center, size)]
    # get the length, width, and height
    l, w, h = size
    x = [[o[0], o[0] + l, o[0] + l, o[0], o[0]],  # x coordinate of points in bottom surface
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],  # x coordinate of points in upper surface
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],  # x coordinate of points in outside surface
         [o[0], o[0] + l, o[0] + l, o[0], o[0]]]  # x coordinate of points in inside surface
    y = [[o[1], o[1], o[1] + w, o[1] + w, o[1]],  # y coordinate of points in bottom surface
         [o[1], o[1], o[1] + w, o[1] + w, o[1]],  # y coordinate of points in upper surface
         [o[1], o[1], o[1], o[1], o[1]],  # y coordinate of points in outside surface
         [o[1] + w, o[1] + w, o[1] + w, o[1] + w, o[1] + w]]  # y coordinate of points in inside surface
    z = [[o[2], o[2], o[2], o[2], o[2]],  # z coordinate of points in bottom surface
         [o[2] + h, o[2] + h, o[2] + h, o[2] + h, o[2] + h],  # z coordinate of points in upper surface
         [o[2], o[2], o[2] + h, o[2] + h, o[2]],  # z coordinate of points in outside surface
         [o[2], o[2], o[2] + h, o[2] + h, o[2]]]  # z coordinate of points in inside surface
    ax.plot_surface(x, y, z, color=col, rstride=1, cstride=1, alpha=0.1)


def plot_cuboid(cube, ax):
    # convert from center x y z w h d    to    8 points of a cube with 1,2,3,4 mapping the bottom square
    # and 5,6,7,8 mapping the correspongin top square
    X = np.array([cube['x'] - cube['width']/2, cube['x'] + cube['width']/2,
                  cube['x'] + cube['width']/2, cube['x'] - cube['width']/2,
                  cube['x'] - cube['width'] / 2, cube['x'] + cube['width'] / 2,
                  cube['x'] + cube['width'] / 2, cube['x'] - cube['width'] / 2])

    Y = np.array([cube['y'] - cube['height'] / 2, cube['y'] - cube['height'] / 2,
                  cube['y'] - cube['height'] / 2, cube['y'] - cube['height'] / 2,
                  cube['y'] + cube['height'] / 2, cube['y'] + cube['height'] / 2,
                  cube['y'] + cube['height'] / 2, cube['y'] + cube['height'] / 2])

    Z = np.array([cube['z'] - cube['depth'] / 2, cube['z'] - cube['depth'] / 2,
                  cube['z'] + cube['depth'] / 2, cube['z'] + cube['depth'] / 2,
                  cube['z'] - cube['depth'] / 2, cube['z'] - cube['depth'] / 2,
                  cube['z'] + cube['depth'] / 2, cube['z'] + cube['depth'] / 2])

    #  Plotting Edges
    ax.scatter(X, Y, Z, c='r', marker='o')

    #  Plotting Lines
    line_idxs = [[0, 1, 2, 3, 0], [4, 5, 6, 7, 4], [4, 0], [5, 1], [6, 2], [7, 3]]
    for lines in line_idxs:
        ax.plot(X[lines], Y[lines], Z[lines], c='g')


if __name__ == '__main__':

    with open('scene_obj_vars') as f:
        [env_layout, object_motion] = pickle.load(f)

    #  print(object_motion)

    #  plot environment
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    frames = len(object_motion.itervalues().next())  # length of the first table of elements
    frame = 0

    while frame < frames:
        ax.clear()
        ax.set_xlabel('xaxis')
        ax.set_ylabel('yaxis')
        ax.set_zlabel('zaxis')
        plt.xlim((0, 5))
        plot_cuboid(env_layout, ax)  # Environment Plotting
        for lab, trackDF in object_motion.items():
            cube = trackDF.loc[frame].to_dict()
            if lab == 'Hand':
                col = "r"
            elif lab == 'Target':
                col = "g"
            else:
                col = "b"
            plot_cuboid_surface(cube, ax, col=col)  # Objects plotting
        ax.text2D(0.05, 0.95, "frame: " + str(frame), transform=ax.transAxes)
        plt.pause(0.01)
        frame += 1
