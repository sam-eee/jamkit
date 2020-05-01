from dxl_control.Ax12 import Ax12 #From https://github.com/cckieu/dxl_control by Aary Kieu

#input
    #ID = motor id
    
    my_dxl=Ax12(ID)
    my_dxl.disable_torque()