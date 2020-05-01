from dxl_control.Ax12 import Ax12 #From https://github.com/cckieu/dxl_control by Aary Kieu
import numpy as np
#Get current position of a motor
#input
    #ID = motor ID
    
    motor_object= Ax12(ID)
    pos=motor_object.get_position()
    pos=np.interp(pos,[0,1023],[0,300])
    return pos

#output
    #pos