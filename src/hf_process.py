#!/usr/bin/env python
import rospy
import numpy as np
from jamkit.msg import sensor_raw
from jamkit.msg import fingertip_adjusted
pub_hf = rospy.Publisher('Fingertip_sensing_adjusted',sensor_raw, queue_size=10)


def process(sensing):
    #ADD INPUTS HERE. Fix accordingly
    #input hd_data
    #Order of variables, 1D SS495A sensors, 3D MLX90393 (x,y,z) readings per sensor

    hf_data=sensing.message
    num_1d=2   #Number of 1D analog sensors
    num_3d=3   #Number of MLX90393 I2C sensors

    #Convert 1D voltage readings to microT as per typical values from SS495A datasheet.
    #Assuming a 5V input voltage.
    #May need calibration to validate readings
    for i in range(num_1d-1):
        hf_data[i]=np.interp(hf_data[i],[0.2,4.8],[-67000,67000])

    fingertip_sensing = seperate(hf_data)

    rospy.loginfo(fingertip_sensing)
    pub_hf.publish(fingertip_sensing)

    #OUTPUT DATA
    #output hf_data array of hall effect sensor data in microT units in an array.

def seperate(hf_data):
    fingertip_sensing = fingertip_adjusted()
    fingertip_sensing.little = hf_data[0]
    fingertip_sensing.ring = hf_data[1]
    fingertip_sensing.middle = [hf_data[2],hf_data[3],hf_data[4]]
    fingertip_sensing.index = [hf_data[5],hf_data[6],hf_data[7]]
    fingertip_sensing.thumb = [hf_data[8],hf_data[9],hf_data[10]]
    return fingertip_sensing




def listener():
    rospy.init_node('hf_process', anonymous=True)
    rospy.Subscriber("force_raw", sensor_raw, process)  ##using this as I couldn't get both subscribers to synchronise without issues

    rospy.spin()


if __name__ == '__main__':
    print("Running")
    listener()
