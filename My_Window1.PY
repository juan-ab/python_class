import serial

from tkinter import *
import tkinter
#################################################
# crear ventana
root = tkinter.Tk ()
root.geometry("267x400") #WxH
root.title("Mi Calculadora")
root.resizable(FALSE,FALSE)
root.configure (background= "#110F0F")
arduinoData = serial.Serial('COM3',9600)
#################################################

#funciones
def btnClik(valor):
    global operador
    operador=operador+str(valor)
    input_text.set(operador)
def clear ():
    global operador
    operador=(" ")
    input_text.set(operador)
def operacion ():
    global operador
    try:
    
        opera=str(eval(operador))#sirve para ejecutar la operacion
        arduinoData.write(b'opera')
    except:
        clear()
        opera=("ERRROR")
    input_text.set(opera)#muestra el resultado    
###############################################
input_text=StringVar ()
operador=" "


display=Entry(root,font=('arial',20,'bold'),width=14,bd=15,insertwidth=2,bg="#DF0101",justify="right",textvariable=input_text).place(x=10,y=30)
Boton1=Button(root,text="1",width=7,height=3,command=lambda:btnClik(1)).place(x=10,y=100)
Boton2=Button(root,text="2",width=7,height=3,command=lambda:btnClik(2)).place(x=70,y=100)
Boton3=Button(root,text="3",width=7,height=3,command=lambda:btnClik(3)).place(x=130,y=100)
Boton4=Button(root,text="4",width=7,height=3,command=lambda:btnClik(4)).place(x=10,y=160)
Boton5=Button(root,text="5",width=7,height=3,command=lambda:btnClik(5)).place(x=70,y=160)
Boton6=Button(root,text="6",width=7,height=3,command=lambda:btnClik(6)).place(x=130,y=160)
Boton7=Button(root,text="7",width=7,height=3,command=lambda:btnClik(7)).place(x=10,y=220)
Boton8=Button(root,text="8",width=7,height=3,command=lambda:btnClik(8)).place(x=70,y=220)
Boton9=Button(root,text="9",width=7,height=3,command=lambda:btnClik(9)).place(x=130,y=220)
Boton0=Button(root,text="0",width=7,height=3,command=lambda:btnClik(0)).place(x=70,y=280)
BotonIgual=Button(root,text="=",width=7,height=3,command=operacion).place(x=130,y=280)
BotonClear=Button(root,text="clear",width=7,height=3,command=lambda:clear()).place(x=10,y=280)
BotonMas=Button(root,text="+",width=7,height=3,command=lambda:btnClik("+")).place(x=195,y=100)
BotonMenos=Button(root,text="-",width=7,height=3,command=lambda:btnClik("-")).place(x=195,y=160)
BotonDividir=Button(root,text="/",width=7,height=3,command=lambda:btnClik("/")).place(x=195,y=220)
BotonMultiplicar=Button(root,text="*",width=7,height=3,command=lambda:btnClik("*")).place(x=195,y=280)
#Abrir ventana
root.mainloop()


led_control_window = Tk()
