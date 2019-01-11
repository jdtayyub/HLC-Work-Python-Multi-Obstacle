

import readData as rD
import pickle
from objects import cuboid
from scene import scenes as sc
from QSRs import QSRS
if __name__ == '__main__':

    data3d_dir = "../../3D HLC 4 Obstacle Data/basic_mod"
    person_dir = 'Pilot01'
    scene3d_dir = 'S001'
    trialFile = 'T001'

    #Read data for one trial and parse into meaningful variables, if not already read and saved before
    df_scene, obj_motion = rD.read_all_data(data3d_dir, person_dir, scene3d_dir, trialFile)

    #Instantiate the scene
    scene_obj = sc.Scene3D(0, 0, 0, 1, 1, 1) # X Y Z of the left corner and then Width, Height, Depth default set as 1 meter on each side

    #scene_obj.visualise()

    #Read and instantiate objects as cuboids (with first value of motion files as first frame), could use other shapes depending on need
    object_obj = []
    for obj_label,obj_info in obj_motion.iteritems():
        # Remove hand as an object since enviornment is being modelled as a set of obstacles provided a trajectory label class.
        #  The hand tracks are used to learn the trajectory label discriminative classes.
        if obj_label == 'TrackedHandRight' or obj_label == 'Target': # CHECK: and obj == 'Target' ? , add walls as objects
            continue
        else:
            physical_object = cuboid.Cuboid(obj_label, obj_info['x'][0], obj_info['y'][0], obj_info['z'][0]
                                            , obj_info['width'][0], obj_info['height'][0], obj_info['depth'][0]) # Name X Y Z of the center then Width, Height, Depth

            # Add track of motion to the object
            physical_object.add_track(obj_info)

            # Add object to the scene
            scene_obj.add_object(physical_object)

    # ADD right and left walls as objects as well to compute the relations against


    ## Compute QSRs (INDU & ALLEN) among obstacles and walls.

    # Read object dimensions at this frame
    for obj in scene_obj.get_objects():
        obj_info = obj_motion[obj.get_name()].iloc[0, :];
        obj.set_coords(obj_info['x'],obj_info['y'],obj_info['z'])

    # Compute QSRS in 2D projection of scene
    qsr_obj = QSRS.QSRs(scene_obj,['Allen','Indu']) # Scene Object with objects first then allen and indu
    qsrs = qsr_obj.compute_qsrs()

    #Generate QSRs feature vector , # CHECK: confirm the feature vector corresponds correctly to object labels
    qsr_feature_vector = []
    for qsr in qsrs:
        qsr_feature_vector.append(sum(qsrs[qsr].values(),[]))

    qsr_feature_vector = sum(qsr_feature_vector,[])

    print('Feature Vector:' +  str(qsr_feature_vector))

    # Feature generation from qsrs
    #feature = feature_generation()

    # Get class path based on movement of hand
    #       ---------------Target--------------
    #       -----------------------------------
    #       ------6--------BLOCK-------7-------
    #       -3---BLOCK------4--------BLOCK--5--
    #L-WALL ------1--------BLOCK-------2-------  R-WALL
    #       -----------------------------------
    #       -----------------------------------
    #       ---------------hand----------------
    #Given the above example outlook of the scene, the class labels are tuples of 3, defining the direction chosen by
    #the hand at each row of the block. An example class label is (2,4,7) indicating that the hand moved through
    #spaces 2 then 4 then 7 to reach the target.

    #loop through hand track and find the class
    hand_label = 'TrackedHandRight'
    print(obj_motion[hand_label])
    number_frames = len(obj_motion.itervalues().next())
    asd
    for frame in range(number_frames):
        print(frame)

    with open('scene_obj_vars', 'w') as f:
        pickle.dump([df_scene, obj_motion], f)
    print('END')