from dxl_control.Ax12 import Ax12 #From https://github.com/cckieu/dxl_control by Aary Kieu


for x in range(11):  #Disables torque for the 12 motors and disconnects them.
    my_dxl=Ax12(x+1)
    my_dxl.disable_torque()
Ax12.close_port()    