#  Parses Matthew's data as received in the 3D format. Creates env_layout variable defining the dimensions of the scene
#  and the obj_motion dictionary defining the tracks of the objects as data frames

import numpy as np
import os
import csv
import pandas as pd
import pickle
import sys

#### Helper Functions

def parse_object_track(obj_label, obj_dim, df):
    #Function to take object label object dimension and raw data frame of its tracks and parse the dataframe
    # and return another data frame with w h d information added.
    #INPUT: df: dataframe of the object track file, obj_label (String) , obj_dim (np.array) of W H D of object
    #OUTPUT: obj_tracks_df (Pandas Data frame)
    x_col_label = [name for name in list(df) if 'pos_x' in name]
    y_col_label = [name for name in list(df) if 'pos_y' in name]
    z_col_label = [name for name in list(df) if 'pos_z' in name]
    new_col_names = {x_col_label[0]:'x', y_col_label[0]:'y', z_col_label[0]:'z'}
    df = df.rename(columns = new_col_names)
    dim_cols = np.tile(obj_dim, (len(df), 1))
    df['width'] = dim_cols[:, 0]
    df['height'] = dim_cols[:, 1]
    df['depth'] = dim_cols[:, 2]
    obj_tracks_df = df[['x', 'y', 'z', 'width', 'height', 'depth']]  # type: Data Frame
    return obj_tracks_df

####

def read_all_data(data3d_dir, person_dir, scene3d_dir, trialFile):

    data_dir = os.path.join(data3d_dir, person_dir, scene3d_dir, trialFile)

    # Get Scene Variables
    sceneDir = os.path.join(data_dir, 'scene')
    envFile = [filename for filename in os.listdir(sceneDir)
               if not filename.startswith('.') and 'scene' in filename.split('_')]

    with open(os.path.join(sceneDir, envFile[0])) as csv_data:
        df_scene = pd.read_csv(csv_data)

    print('Environment Layout parsed and set in ->df_scene<- dictionary variable')

    # Get Object Motion Variables
    objFileDim = [filename for filename in os.listdir(sceneDir)
                  if not filename.startswith('.') and 'objects' in filename.split('_')]

    motionDir = os.path.join(data_dir, 'movement')
    motionFiles = [filename for filename in os.listdir(motionDir)
                   if not filename.startswith('.') and not 'interaction' in filename.split('_')]

    obj_motion = {}  # A dictionary of data frames containing x,y,z,w,h,d of objects in the scene
    with open(os.path.join(sceneDir, objFileDim[0])) as csv_data:
        reader = csv.reader(csv_data)
        reader.next()
        for row in reader:
            obj_label = row[0]
            obj_dim = np.array(map(float, row[4:])) # w h d

            # open the corresponding tracks file for obj_label and extract the tracks in a dataframe
            objMotionFile = obj_label + '_' + 'movement' + '_' + trialFile + '.csv'
            df = pd.read_csv(os.path.join(motionDir, objMotionFile))
            obj_tracks_df = parse_object_track(obj_label, obj_dim, df)
            obj_motion.update({obj_label: obj_tracks_df})

    #### Append the hand object to the csv file since it is not natively included (Thic block could be removed in the future
    # when the hand object is added as a row in the csv file )
    hand_label = 'TrackedHandRight'
    handFile = hand_label + '_' + 'movement' + '_' + trialFile + '.csv'
    df_hand = pd.read_csv(os.path.join(motionDir,handFile))
    hand_tracks_df = parse_object_track(hand_label, np.array([0.20, 0.20, 0.20]), df_hand)
    obj_motion.update({hand_label: hand_tracks_df})
    ####

    print('Object motion tracks parsed and set ->object_motion<- dictionary variable')
    return df_scene, obj_motion
# Save computed vars in scene_obj_vars to avoid repeat computation


