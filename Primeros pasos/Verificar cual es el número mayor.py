#Planteamiento: Realizar un programa que pida 3 números y determinar cual es el mayor

num1 = int(input("Ingrese el 1er número: "))
num2 = int(input("Ingrese el 2do número: "))
num3 = int(input("Ingrese el 3er número: "))

#Verificamos el 1er caso
if num1 >= num2 and num1 >= num3:
    print("El 1er número es mayor")

#Verificamos el 2do caso
if num2 >= num1 and num2 >= num3:
    print("El 2do número es mayor")

#Verificamos el 3er caso
if num3 >= num1 and num3 >= num2:
    print("El 3er número es mayor")

