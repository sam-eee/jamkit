#!/usr/bin/env python
import rospy
import serial
import time
import csv
import sys
import numpy as np

from jamkit.msg import sensor_raw


#Function that pulls serial data and converts it to float array for processing.
#Function is called below.
def ser_loop(ser,num_rot,num_1d,num_3d):
        ser.flushInput()
        cc=ser.readline()
        cc=cc.decode('utf-8')
        sensor_data_list=cc.split(',',-1)
        #Error checking for number of expected number of sensor readings
        if len(sensor_data)!=num_rot+num_1d+num_3d*3:
            return

        #Convert imported split string values to float values.
        for k in range(0,len(sensor_data),1):
            try:
                sensor_data[k]=float(sensor_data[k])
            except ValueError:
                break

        #Convert list to array
        sensor_data_arr=np.array(sensor_data)
        return sensor_data_arr #Return one array of sensor data





    #Set serial port variable for connected Arduino.

    #Close any open connections and open a new serial connections to the Arduino
    serial.Serial.close(serial.Serial("COM4"))
    ser=serial.Serial("COM4", 9600,timeout=0.01)#Port, Baud rate, timeout

    #Starts requesting serial data from the Arduino continuously
    csv_record='no' #set as 'yes' or 'no' for CSV recording in an Excel file.

    #Clear Serial cache on Arduino and idle time for completion.
    ser.flushInput()
    time.sleep(3)

    num_rot=16
    num_1d=2
    num_3d=3

    #Rotational sensors should output first, followed by 1D hall effect sensors.(1 output each)
    #3D hall effect sensors should output be last in the array. (3 outputs - X,Y,Z)
    #This can be function expanded on depending on how the user wants the outputs done.
    if csv_record=='yes':
        while True:
            sensor_data_arr=ser_loop(ser,num_rot,num_1d,num_3d)
            with open("test_data.csv","a",newline='') as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow(sensor_data)
            time.sleep(0.01) #Time can be used to limit serial request rate to match Arduino.
    elif csv_record=='no':
        while True:
            sensor_data_arr=ser_loop(ser,num_rot,num_1d,num_3d)
            time.sleep(0.01) #Time can be used to limit serial request rate to match Arduino.
    else :
        sys.exit('Wrong input for CSV_record') #if wrong then exit the program.




#OUTPUT sensor_data_arr to sensor_split.py

if __name__ == '__main__':
    try:
        ser_loop()
    except rospy.ROSInterruptException:
        pass