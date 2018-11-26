import serial
from tkinter import *
import tkinter

arduinoData = serial.Serial('COM3',9600)
#arduinoData.close()
def led_on():
    arduinoData.write(b'1')
    print("encender")
def led_off():
    arduinoData.write(b'0')
    print("apagar")

led_control_window = Tk()

btn1 = Button(led_control_window, text="ON", command=led_on)
btn2 = Button(led_control_window, text="OFF", command=led_off)
btn3 = Button(led_control_window, text="ON", command=led_on)
btn4 = Button(led_control_window, text="OFF", command=led_off)
btn5 = Button(led_control_window, text="ON", command=led_on)
btn6 = Button(led_control_window, text="OFF", command=led_off)
btn7 = Button(led_control_window, text="OnAll", command=led_on)
btn8 = Button(led_control_window, text="OffAll", command=led_off)


btn1.grid(row=0,column=1)
btn2.grid(row=1,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=2)
btn5.grid(row=0,column=3)
btn6.grid(row=1,column=3)
btn7.grid(row=0,column=4)
btn8.grid(row=1,column=4)


                            
