#Diccionarios en Python
#La estructura para declarar un diccionario en Python es la siguiente:

diccionario = { #Declaramos el diccionario con -> nombre = {}
    'IDE': 'Integrated Development Enviroment', #Añadimos el contenido en formato -> 'llave' : 'descripción',
    'OPP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
} # Cerramos bloque de código del diccionario.

#Para imprimir el contenido del diccionario:
print(diccionario)

#Para imprimir el tamaño del diccionario:
print(len(diccionario))

#Obtener un elemento específico (por medio de la llave):
print(diccionario['OPP'])

#Otra forma de obtener un elemento del diccionario:}
print(diccionario.get('DBMS'))

#Modificar un elemento del diccionario:
diccionario['IDE'] = 'InTeGrAtEd DeVeLoPmEnT EnViRoMeNt'
print(diccionario['IDE'])

#Recorrer y obtener las llaves del dicionario:
for termino in diccionario.keys():
    print(termino) #imprimimimos unicamente la llave

#Recorrer y obtener los valores del diccinario:
for valor in diccionario.values():
    print(valor)

#Recorrer y obtener las llaves y valores del diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

#Comprobar la existencia de un elemento:
print('IDE' in diccionario)
    #Nota: La busqueda difiere mayúsculas de minúsculas por
    #lo que se debe tener cuidado a la hora de escribir el elemento a buscar.

#Agregar un elemento al diccionario:
diccionario['PK'] = 'Pimary Key'
print(diccionario)

#Eliminar un elemento del diccionario (por su llave):
diccionario.pop('DBMS')
print(diccionario)

#Eliminar todos los elementos del diccionario:
diccionario.clear()
print(diccionario)

#Eliminar el diccionario:
del diccionario
# print(diccionario) <-- Causa error de compilación debido aque no está definido