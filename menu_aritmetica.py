#ejercicio de menu dcalculadora
import os # importar librerias del sistema

os.system("cls")
print ("menu calculadora")
print ("1. sumar numeros")
print ("2. restar numeros")
print ("3. multiplicar numeros")
print ("4. dividir numeros")
print (".:::digite su opcion: ")

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo nummero: "))
opc = int(input("digite la operacion a realizar"))

if opc == 1 :
	suma = num1 + num2
	print ("la suma es: ",suma)
elif opc == 2 :
	resta = num1 - num2
	print ("la resta es: ",resta)
elif opc == 3 :
	multiplicion = num1 * num2
	print ("la multiplicion es: ",multiplicion)
elif opc == 1 :
	divicion = num1 / num2
	print ("la divicion es: ",divicion)