from dxl_control.Ax12 import Ax12 #From https://github.com/cckieu/dxl_control by Aary Kieu

    Ax12.open_port() #Connects to the Robotis U2D2 using the default port in Ax12.py
    Ax12.set_baudrate() #Uses the motor default 1000000 baud rate.