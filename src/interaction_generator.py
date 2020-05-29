#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Float64
from jamkit.msg import sensor_raw

#include all message types required

##About: Generates random values for the sensor values for the potentiometers and the fingertip sensors in the same order as  they would be output from the topic sensor_process.py
#and publishes to the topic \hand_sensing_output

##Author: Ahmed Sami Deiri - Queen Mary University of London

def sensor_generator():

    ##initialise publisher topics
    PubOverall = rospy.Publisher("hand_sensing_output", sensor_raw, queue_size=10)

    #initialise node
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(0.2)  #rate of 1hz ie, every second
    sensorvals = sensor_raw()  ##declare variable to contain the random generated values

    print("node up and generating")
    for i in range(0,27):
        sensorvals.message.append(i)

    while not rospy.is_shutdown():
        for i in range(0,16):
            sensorvals.message[i] = random.uniform(0,5) #generates random potentiometer voltage
        for i in range(16,18):
            sensorvals.message[i] = random.uniform(0.2,4.8) #generates random 1D sensor voltage
        for i in range(18,27):
            sensorvals.message[i] = random.uniform(-1000,1000) #generates random 3d sensor voltage

        PubOverall.publish(sensorvals) #publish random values to topic \hand_sensing_output
        #rospy.loginfo(sensorvals.message) #log random values and print to terminal
        print("Node: interaction_generator")
        print("New Interaction Values - Published to hand_sensing_output")
        for i in sensorvals.message:
            print(i)
        print('')
        rate.sleep()


if __name__ == '__main__':
    try:
        sensor_generator()
    except rospy.ROSInterruptException:
        pass