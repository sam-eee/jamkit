#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Float64
from jamkit.msg import sensor_raw

#include all message types required



def sensor_generator():

    ##initialise publisher topics
    PubOverall = rospy.Publisher("hand_sensing_output", sensor_raw, queue_size=10)  ##used as I couldnt get two subscribers to synchronise in the following part

    #initialise node
    rospy.init_node('interaction_generator', anonymous=True)
    rate = rospy.Rate(1) # 0.1hz ie 10 seconds
    sensorvals = sensor_raw()

    print("node up and generating")
    for i in range(0,29):
        sensorvals.message.append(i)

    while not rospy.is_shutdown():
        for i in range(0,17):
            sensorvals.message[i] = random.uniform(0,1) #generates random potentiometer voltage
        for i in range(17,19):
            sensorvals.message[i] = random.uniform(0,1) #generates random potentiometer voltage
        for i in range(19,29):
            sensorvals.message[i] = random.uniform(0,2) #generates random 3d sensor voltage

        PubOverall.publish(sensorvals) #publish object to topic IntTopicObject
        rospy.loginfo(sensorvals.message)

        rate.sleep()


if __name__ == '__main__':
    try:
        sensor_generator()
    except rospy.ROSInterruptException:
        pass