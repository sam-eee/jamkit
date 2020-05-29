#!/usr/bin/env python
import rospy
from jamkit.msg import sensor_raw
from std_msgs.msg import Float64
pub_hf = rospy.Publisher('force_raw',sensor_raw, queue_size=10)
pub_rot = rospy.Publisher('rotation_raw',sensor_raw, queue_size=10)

##About: node \sensor_split subscribes to topic \hand_sensing_output where it recieves an array containing float values for the jamkit robot hand
#sensor values including the 16 potentiometers, 2x 1D fingertip sensors, and 3x 3D Fingertip sensors with 3 values each for x y z.
#outputs two arrays, one containing the potentiometer values, the other containing the fingertip sensor values. These arrays are
#published onto topics rotation_raw and force_raw respectively.

##Authors: Ahmed Sami Deiri, Jamie Sengun - Queen Mary University of London


def split(sensingdata):
    print("Node: sensor_split")
    #Order of variables, Rotational potentiometers, 1D SS495A sensors, 3D MLX90393
    sensor_raw= sensingdata.message
    num_rot=16 #Number of rotational potentiometers
    num_1d=2   #Number of 1D analog sensors
    num_3d=3   #Number of MLX90393 I2C sensors

    #rot_data = sensor_raw()
    #for i in range(0,num_rot-1):
       # rot_data.message.append(i)

    rot_data = sensingdata.message[0:num_rot]    #rotational potentiometer data
    #rospy.loginfo(rot_data)  ##logs potentiometer array and prints to terminal
    pub_rot.publish(rot_data)  ##publish potentiometer values to topic \rotation_raw
    #print(rot_data)
    print("Potentiometer Raw Values - published to rotation_raw")
    for i in rot_data:
        print(i)
    print('')
    #hf_data = sensor_raw()
    #for i in range(0,10):
    #    hf_data.message.append(i)


    hf_data=sensor_raw[num_rot:len(sensor_raw)] #1D then 3D hall effect sensors
    #srospy.loginfo(hf_data)  ##logs fingertip sensor array and prints to terminal

    #hfpub = sensor_raw()
    #hfpub.message = hf_data
    pub_hf.publish(hf_data)  ##publish fingertip sensor values to topic \force_raw
    #print(hf_data)
    print("Fingertip Sensor Raw Values - published to force_raw")
    for i in hf_data:
        print(i)
    print('')
    return()

def listener():  #subscribes to topic, calls function split() when a message is published on topic.
    rospy.init_node('sensor_split', anonymous=True)
    rospy.Subscriber("hand_sensing_output", sensor_raw, split)  ##subscribes to topic hand_sensing_output. Expects a float array with 27 values.

    rospy.spin()


if __name__ == '__main__':
    print("Running")
    listener()
