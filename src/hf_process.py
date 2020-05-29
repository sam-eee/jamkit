#!/usr/bin/env python
import rospy
import numpy as np
from jamkit.msg import sensor_raw
from jamkit.msg import fingertip_adjusted
from std_msgs.msg import Float64

pub_hf = rospy.Publisher('Fingertip_sensing_adjusted',fingertip_adjusted, queue_size=10)
##About : this program recieves the fingertip sensing values in the form of an array containing each fingertip,
#coverts the 1d sensors to microT rather than voltage, and publishes the data on topic \Fingertip_sensing_adjusted with message type fingertip_adjusted.

##The message fingertip_adjusted is a data structure comprising of 5 variables for each finger : thumb, index, middle, ring, little.
# The thumb index and middle finger variables are each float64 arrays that contain the 3 axis sensor values (x,y,z field strength)
# The ring and little finger contain a single float64 variable each due to the use of 1D magnetic sensors
#Published values within the Fingertip_sensing_adjusted topic are in microT.

##Authors: Ahmed Sami Deiri, Jamie Sengun  - Queen Mary University of London


def process(sensing):
    #rospy.loginfo(sensing.message)  #Logs fingertip sensing values and prints to terminal

    #Order of variables, 1D SS495A sensors, 3D MLX90393 (x,y,z) readings per sensor

    hf_data=sensing.message
    num_1d=2   #Number of 1D analog sensors
    num_3d=3   #Number of MLX90393 I2C sensors
    microtrange = 67000

    #Convert 1D voltage readings to microT as per typical values from SS495A datasheet.
    #Assuming a 5V input voltage.
    #May need calibration to validate readings
    tempval = list(hf_data)
    #print("initial")os
    for i in range(num_1d):
        #hf_data[i]=np.interp(hf_data[i],[0.2,4.8],[-67000,67000])
        tempval[i] = (tempval[i] * microtrange * 2 /4.6) - microtrange

    fingertip_sensing = seperate(tempval)
    print("Node: hf_process")
    print("Fingertip Sensors - published to fingertip_sensing_adjusted")
    print(fingertip_sensing)
    print('')
    #rospy.loginfo(fingertip_sensing)  #Logs fingertip sensing values and prints to terminal
    pub_hf.publish(fingertip_sensing)  #Publishes fingertip sensing values to topic \Fingertip_sensing_adjusted.


def seperate(hf_data):  # recieves array containing sensor values, seperates individual fingertips and returns type fingertip_adjusted
    fingertip_sensing = fingertip_adjusted()
    fingertip_sensing.little = hf_data[0]
    fingertip_sensing.ring = hf_data[1]
    fingertip_sensing.middle = [hf_data[2],hf_data[3],hf_data[4]]
    fingertip_sensing.index = [hf_data[5],hf_data[6],hf_data[7]]
    fingertip_sensing.thumb = [hf_data[8],hf_data[9],hf_data[10]]
    return fingertip_sensing




def listener():
    rospy.init_node('hf_process', anonymous=True)
    rospy.Subscriber("force_raw", sensor_raw, process) ##subscribes to topic force_raw which contains the fingertip sensor data without processing in a float64 array

    rospy.spin()


if __name__ == '__main__':
    print("Running")
    listener()
