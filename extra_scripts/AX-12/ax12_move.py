from dxl_control.Ax12 import Ax12 #From https://github.com/cckieu/dxl_control by Aary Kieu
import numpy as np

#input
    #ID = motor ID
    #angle = motor angle in degrees
    
    #Motor angle function is between 0-1023 for the 300 degrees.
    #Requested motor angle in degrees is mapped between 0-1023
    angle=np.interp(angle,[0,300],[0,1023])
    
    motor_object= Ax12(ID)
    motor_object.set_position(angle)