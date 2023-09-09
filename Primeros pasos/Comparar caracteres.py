#Planteamiento: Crea un programa que cmpare dos nombres, y verificar si hay 
#coincidencia o no, si es que ambos nombres comienzan con la misma letra ó 
#                si terminan con la misma letra.

pnombre = input("Ingresa el primer nombre: ")
snombre = input("Ingresa el segundo nombre: ")

if pnombre[0] == snombre[0]: #Verificamos si las primeras letras coinciden.
    print(f"La primera letra de ambos nombres es la: {pnombre[0]}")

    if pnombre[-1] == snombre[-1]: #Verificamos si las últimas letras coinciden.
        print(f"La última letra de ambos nombres es la: {pnombre[-1]}") #En pyton se puede obtener el último elemento utilizando la posición -1
        
else: #En caso de que no se cumplan las condiciones anteriores:
    print("No hay ninguna coincidencia")