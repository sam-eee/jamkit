#!/usr/bin/env python
import rospy
import numpy as np
from jamkit.msg import jamkit_joint_position
from jamkit.msg import sensor_raw
from std_msgs.msg import Float64
pub = rospy.Publisher('pot_joint_angle',jamkit_joint_position, queue_size=10)

##About: Initiates node rot_process which recieves an array containing float64 values for all the potentiometer I/O voltage values,
#calculates the angle from the input voltage value
#splits the potentiometers into the individual fingers using the data structure declared in jamkit_joint_position.msg
#and publishes the joint angles to the topic \pot_joint_angle on datatype jamkit_joint_position

##jamkit_joint_position data type is formed of 5 float64 arrays representing each finger : thumb,index,middle,ring,little
#The array for each finger contains the joint angles, where finger[i] contains the joint i angle for finger "finger".
# eg: index[1] contains the angle for joint 1 on the index finger

##Authors: Ahmed Sami Deiri, Jamie Sengun - Queen Mary University of London

def callback(rot_data):
    #print("Message Recieved")
    angles = rotationcalculator(rot_data.message)
    hand = jointsplit(angles)
    #rospy.loginfo(hand)
    print("Node: rot_process")
    print("Joint Angles - published to topic pot_joint_angle")
    print(hand)
    print('')
    pub.publish(hand)

def jointsplit(angles):  #creates hand with each finger of message type jamkit_joint_position, with an array containing L1-3 for each finger
    hand = jamkit_joint_position()
    i = 0
    for x in range(3):
        hand.little.append(angles[i])
        i += 1

    for x in range(3):
        hand.ring.append(angles[i])
        i += 1

    for x in range(3):
        hand.middle.append(angles[i])
        i += 1

    for x in range(3):
        hand.index.append(angles[i])
        i += 1

    for x in range(4):
        hand.thumb.append(angles[i])
        i += 1
    return hand

def rotationcalculator(inputdata):
    # rot_data=rot_data
    rot_data = list(inputdata)
    num_rot=16
    # Data is in order of ports on KA-12 shield from port 1.
    #Defined KA-12 ports for rotational potentiometers, L1 is the base joint and
        #L2 is the middle joint and L3 is the fingertip joint:
            #Little finger link joints: L1=1, L2=2, L3=3
            #Ring finger link joints: L1=4, L2=5, L3=6
            #Middle finger link joints: L1=7, L2=8, L3=9
            #Index finger link joints: L1=10, L2=11, L3=12
            #Thumb link joints: L1=13, L2=14
            #Thumb AA joint = 15
            #Thumb oppsable joint = 16

    #Guranteed linearity is between +/- 160 degrees
    #All link sensors for ROT 1 to 14 are orientated as defined when looking at the
    #palmar side from fully extended (0 degree) to fully flexed (90 degree etc):
        #left side potentiometers output for L2 on all fingers; not including thumb
            #= -90 degree to 0 degree
        #right side potentiometers output for L1 and L3 on all fingers and 2 thumb
            #links = 90 degree to 0 degree

        #All 14 link rotational potentiometers are converted as they all start at
        #-90 degree or 90 degree as shown above, so the absolute values are
        #the same as they approach 0 degree
        #The other 2 thumb potentiometers are dealt seperately.

        #Joints have been designed to have a max displacement range of 90 degrees.
        #The displacement range will be controlled by testing and programming the AX-12 motors
        #Potentiometers do not travel greater than 90 degree from their
        #starting position while staying within the range of +/- 166.65 degrees.

    for i in range(num_rot-3):
        rot_data[i]=90-abs(np.interp(rot_data[i],[0,5],[-166.65,166.65]))

        #ROT 15 has a range of 60 degrees, from potentiometer readings of 30 degree to
        #-30 degree, mapped between 0 degree to 60 degree respectively.
    rot_data[num_rot-2]=30-np.interp(rot_data[num_rot-2],[0,5],[-166.65,166.65])

        #ROT 16 has a range of 90 degrees, from potentiometer readings of
    rot_data[num_rot-1]=abs(np.interp(rot_data[num_rot-1],[0,5],[-166.65,166.65]))

    #It has been configured such that all potentiomers; except the Thumb AA joint
    #will output either all positive or negative angles that are then converted to their
    #absolute values. A displacement range greater than 90 degrees is not required for
    #the desired functionality, so a more complicated solution involving both positive and minus
    #values from a potentiometer was not required.
    #print(rot_data)
    return rot_data
    #OUTPUT rot_data array of potentiometer angles in an array.
def listener():
            rospy.init_node('rot_process', anonymous=True)
            rospy.Subscriber("rotation_raw", sensor_raw, callback)  ##subscribes to topic rotation_raw which provides voltage output values for the potentiometers in an array

            rospy.spin()

if __name__ == '__main__':
    print("Running Rot_process")
    print("Awaiting Messages")
    listener()
