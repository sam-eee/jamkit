from tkinter import *
import time
import ax12_code as ax  #From https://github.com/cckieu/dxl_control by Aary Kieu

#This code is designed to allow to user to move sliders to control the motors.
#It is recommended that either this method or direct function motor control is used
#as they cannot be used simultaneously by design.


#Functions for changing servo angles, needed unique functions for the sliders

#Author: Jamie Sengun

def F1(angle1):
    ax.move_ax(1,angle1) 
    
def F2(angle2):
    ax.move_ax(2,angle2)  
    
def F3(angle3):
    ax.move_ax(3,angle3) 
    
def F4(angle4):
    ax.move_ax(4,angle4) 
    
def F5(angle5):
    ax.move_ax(5,angle5)  
    
def F6(angle6):
    ax.move_ax(6,angle6)  

def F7(angle7):
    ax.move_ax(7,angle7)
    
def F8(angle8):
    ax.move_ax(8,angle8)

def F9(angle9):
    ax.move_ax(9,angle9)
    
def F10(angle10):
    ax.move_ax(10,angle10)
    
def F11(angle11):
    ax.move_ax(11,angle11)
    
def F12(angle12):
    ax.move_ax(12,angle12)
    
#GUI creation with sliders that control servos between 0-300 in steps 0-1023.
#Updates the sliders on initialisation to get current motor positions.
root =Tk()
time.sleep(1) #Pause for loading of GUI

w1=Scale(root,orient='vertical', command=F1, from_ =0, to=1023)
w1.set(ax.get_ax(1))
w2=Scale(root,orient='vertical', command=F2, from_ =0, to=1023)
w2.set(ax.get_ax(2))
w3=Scale(root,orient='vertical', command=F3, from_ =0, to=1023)
w3.set(ax.get_ax(3))
w4=Scale(root,orient='vertical', command=F4, from_ =0, to=1023)
w4.set(ax.get_ax(4))
w5=Scale(root,orient='vertical', command=F5, from_ =0, to=1023)
w5.set(ax.get_ax(5))
w6=Scale(root,orient='vertical', command=F6, from_ =0, to=1023)
w6.set(ax.get_ax(6))
w7=Scale(root,orient='vertical', command=F7, from_ =0, to=1023)
w7.set(ax.get_ax(7))
w8=Scale(root,orient='vertical', command=F8, from_ =0, to=1023)
w8.set(ax.get_ax(8))
w9=Scale(root,orient='vertical', command=F9, from_ =0, to=1023)
w9.set(ax.get_ax(9))
w10=Scale(root,orient='vertical', command=F10, from_ =0, to=1023)
w10.set(ax.get_ax(10))
w11=Scale(root,orient='vertical', command=F11, from_ =0, to=1023)
w11.set(ax.get_ax(11))
w12=Scale(root,orient='vertical', command=F12, from_ =0, to=1023)
w12.set(ax.get_ax(12))


Label(root, text="F1").grid(column=0,row=1)
Label(root, text="F2").grid(column=1,row=1)
Label(root, text="F3").grid(column=2,row=1)
Label(root, text="F4").grid(column=3,row=1)
Label(root, text="F5").grid(column=4,row=1)
Label(root, text="F6").grid(column=5,row=1)
Label(root, text="F7").grid(column=6,row=1)
Label(root, text="F8").grid(column=7,row=1)
Label(root, text="F9").grid(column=8,row=1)
Label(root, text="F10").grid(column=9,row=1)
Label(root, text="F11").grid(column=10,row=1)
Label(root, text="F12").grid(column=11,row=1)

w1.grid(column=0,row=0)
w2.grid(column=1,row=0)
w3.grid(column=2,row=0)
w4.grid(column=3,row=0)
w5.grid(column=4,row=0)
w6.grid(column=5,row=0)
w7.grid(column=6,row=0)
w8.grid(column=7,row=0)
w9.grid(column=8,row=0)
w10.grid(column=9,row=0)
w11.grid(column=10,row=0)
w12.grid(column=11,row=0)


root.mainloop()