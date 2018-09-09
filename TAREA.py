import os
os.system("cls")

nper = 0
edad = 0
j = 1
k = 1
i = 1
ch = 0
cm = 0
prom1 = 0
prom2 = 0
sumaedad = 0
sumaedad1 = 0

nper = int(input("Ingrese cantidad de personas"))
if nper > 0 :
    while j <= nper :
        genero = input("Ingrese el genero masculino (M) o femenino (F) de la persona" + str(j) + "")
        if genero.upper() == 'M' :
            ch = ch + 1
        elif genero.upper() == 'F' :
            cm = cm + 1
        else :
            print ("Genero equivocado")
        j = j + 1
    while k <= ch :
        print("Ingrese la edad del hombre", k, "")
        edad = int(input())
        if edad >= 1 and edad <= 110 :
            k = k + 1
        else :
                print("Ingreso una edad incorrecta")
        sumaedad = sumaedad + edad
        prom1 = sumaedad / ch
    while i <= cm :
        print("Ingrese la edad de la mujer", i, "")
        edad = int(input())
        if edad >= 1 and edad <= 110 :
            i = i + 1
        else :
                print("Ingreso una edad incorrecta")
        sumaedad1 = sumaedad1 + edad
        prom2 = sumaedad1 / cm
    print ("La cantidad de hombres es: ", ch , "")
    print ("La cantidad de mujeres es: ", cm , "")
    print ("La suma de las edades de los hombres es: " +str (sumaedad) + "")
    print ("El promedio de las edades de los hombres es: " +str (prom1) + "")
    print ("La suma de las edades de las mujeres es: " +str (sumaedad1) + "")
    print ("El promedio de las edades de las mujeres es: " +str (prom2) + "")
    print ("El total de personas es: " +str (nper) + ":")
else :
    print("Ingreso un dato incorrecto")
