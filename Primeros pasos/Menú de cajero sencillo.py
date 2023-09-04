#Ejercicio 8 Cajero automático

print("Menú principal: ")
print("1. Ingresar dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")

opcion = int(input("Ingrese la opción deseada: "))

saldo = 2000

if opcion == 1:
    saldo += int(input("Cantidad de dinero a ingresar: "))
    print(f"El saldo en su cuenta es de: {saldo}")

if opcion == 2:
    saldo -= int(input("Cantidad de dinero a retirar: "))
    print(f"El saldo en su cuenta es de: {saldo}")

if opcion == 3:
    print(f"El saldo en su cuenta es de: {saldo}")

if opcion == 4:
    print("Hasta luego")

