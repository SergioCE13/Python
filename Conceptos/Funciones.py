#1. Declarar funciones en Python:
def nombreFuncion1():
    print('saludos desde mi función')

nombreFuncion1() #Mandamos llamar a la función

#2. Declarar una función con parámetros
def nombreFuncion2(nombre,edad): #Parámetros
    print(nombre,edad)

nombreFuncion2("Juan",25) #Argumentos

#Nota: Parámetro: es el valor que va a recibir una función para trabajarlo.
#      Argumento: es el valor que se le manda a una función.


#3. Declarar una función que retorna un valor:
def Suma(a,b):
    return a+b

suma = Suma(5,4)
print(f'Resultado de la suma: {suma}')

#4. Declarar una función que reciba parametros ó aplique valores por default
def Resta(a = 5, b = 0): #En caso de que no se le mande un argumento valido utilizará a = 5 y b = 0
    return a-b
resta = Resta()
print(f'La resta es: {resta}')
resta = Resta(10,3)
print(f'La resta es: {resta}')

#5. Declarar una función que reciba n cantidad de parametros:

def Nombres(*nombres): #El simbolo * nos ayuda a indicar que se le va a mandar N cantidad de argumentos
    for nombre in nombres:
        print(nombre)
    #Nota: Internamente Python transforma *nombres en una tupla por lo cual se puede trabajar
    # con los argumentos de la misma manera que con una tupla.
Nombres('Sergio','Cynthia','Angel','Yayas','María')
Nombres('Sergio','Cynthia')
Nombres('María')
