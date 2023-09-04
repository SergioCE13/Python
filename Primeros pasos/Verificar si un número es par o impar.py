#Ejercicio Número 5 Números paraes e impares

num1 = int(input("Ingresa el primer número a verificar: "))
num2 = int(input("Ingresa el segundo número a verificar: "))


#Verificación del primer número
if num1%2 == 0: 
    print("El primer número es par")
elif num1%2 != 0:
    print("El primer número es inpar")

#Verificación del segundo número
if num2%2 == 0:
    print("El segundo número es par")
elif num2%2 != 0:
    print("El segundo número es inpar")
