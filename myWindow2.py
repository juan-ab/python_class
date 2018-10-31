#Importar librerias para GUI
from tkinter import *
import tkinter

################################
#Crear ventana
root = tkinter.Tk()
root.geometry("320x400")#WxH - ancho x alto
root.title("mi calculadora")
root.resizable(FALSE, FALSE)
root.configure(background="#48C9B0    ")
################################

def btnClik(valor):
    global operador
    operador=operador+str(valor)
    input_text.set(operador)
def clear():
    global operador
    operador=(" ")
    input_text.set(operador)
def operacion():
    global operador
    try:
        opera=str(eval(operador))#sirve para ejecutar la operacion
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)#muestra el resultado

#####################################
input_text=StringVar()
operador=""

Display=Entry(root,font=('arial',20,'bold'),width=18,bd=10,insertwidth=2,bg="#8E44AD",justify="right",textvariable=input_text).place(x=10,y=30)
Boton1=Button(root,text="1",width=7,height=3,command=lambda:btnClik(1)).place(x=10,y=100)
Boton2=Button(root,text="2",width=7,height=3,command=lambda:btnClik(2)).place(x=75,y=100)
Boton3=Button(root,text="3",width=7,height=3,command=lambda:btnClik(3)).place(x=140,y=100)
Boton4=Button(root,text="4",width=7,height=3,command=lambda:btnClik(4)).place(x=10,y=160)
Boton5=Button(root,text="5",width=7,height=3,command=lambda:btnClik(5)).place(x=75,y=160)
Boton6=Button(root,text="6",width=7,height=3,command=lambda:btnClik(6)).place(x=140,y=160)
Boton7=Button(root,text="7",width=7,height=3,command=lambda:btnClik(7)).place(x=10,y=220)
Boton8=Button(root,text="8",width=7,height=3,command=lambda:btnClik(8)).place(x=75,y=220)
Boton9=Button(root,text="9",width=7,height=3,command=lambda:btnClik(9)).place(x=140,y=220)
Boton0=Button(root,text="0",width=7,height=3,command=lambda:btnClik(0)).place(x=75,y=285)
BotonIgual=Button(root,text="=",width=7,height=3,command=operacion).place(x=140,y=285)
BotonClear=Button(root,text="clear",width=7,height=3,command=lambda:clear()).place(x=10,y=285)
BotonMas=Button(root,text="+",width=7,height=3,command=lambda:btnClik("+")).place(x=224,y=100)
BotonMenos=Button(root,text="-",width=7,height=3,command=lambda:btnClik("-")).place(x=224,y=160)
BotonMultiplicacion=Button(root,text="*",width=7,height=3,command=lambda:btnClik("*")).place(x=224,y=220)
BotonDivicion=Button(root,text="/",width=7,height=3,command=lambda:btnClik("/")).place(x=224,y=285)

#Abrir ventana
root.mainloop()
