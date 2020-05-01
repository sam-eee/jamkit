#!/usr/bin/env python
import rospy
import numpy as np
from jamkit.msg import sensor_raw
from std_msgs.msg import Float64
pub_hf = rospy.Publisher('force_raw',sensor_raw, queue_size=10)
pub_rot = rospy.Publisher('rotation_raw',sensor_raw, queue_size=10)


def split(sensingdata):

    #Order of variables, Rotational potentiometers, 1D SS495A sensors, 3D MLX90393
    sensor_raw= sensingdata.message
    num_rot=16 #Number of rotational potentiometers
    num_1d=2   #Number of 1D analog sensors
    num_3d=3   #Number of MLX90393 I2C sensors



    rot_data=sensor_raw[0:num_rot-1]    #rotational potentiometer data
    rospy.loginfo(rot_data)
    pub_rot.publish(rot_data)

    hf_data=sensor_raw[num_rot:len(sensor_raw)-1] #1D then 3D hall effect sensors
    rospy.loginfo(hf_data)
    pub_hf.publish(hf_data)

    return()
    #OUTPUT DATA
    #rot_data to rot_process.py
    #hf_data to hf_process.py


def listener():
    rospy.init_node('sensor_split', anonymous=True)
    rospy.Subscriber("hand_sensing_output", sensor_raw, split)  ##using this as I couldn't get both subscribers to synchronise without issues

    rospy.spin()


if __name__ == '__main__':
    print("Running")
    listener()
