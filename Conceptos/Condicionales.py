#Condicionles en Python

numero = int(input("Ingrese un número para analizarlo: "))

if numero > 0: #Veridiamos SI la condicion se cumple
    print("El número es positivo")
elif numero < 0: #En caso de que la condición anterior no se cumpla verificamos SI
    print("El número es negativo")
else: #En caso de que ninguna condición se cumpla realizamos:
    print("El número es 0")