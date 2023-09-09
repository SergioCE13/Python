#Estructuras para bucles en Python
import math

numero = int(input("Escribe un número positivo: "))

#Bucle While
while numero < 0:
    print("Porfavor ingresa un número positivo: ")
    numero = int(input("Escribe un número positivo: "))

print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero): .0f}")

#Bucle for
for i in [6,8,9,4,7]: #Recorrer todos los elementos de un arreglo
    print(f"Objeto: {i}")

#Utilizando el nombre del arreglo
data = ["Hola", 5 , 6.3, True]

for j in data:
    print(f"Objeto: {j}")
    