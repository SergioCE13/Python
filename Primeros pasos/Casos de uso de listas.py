arreglo1 = ["futbol", "Pc", 18.6, 18, [6,7,10,4], True, False]
arreglo2 = ["Adios", "Pc", "Mañana"]


#Obtener la longitud de un arreglo:
print(len(arreglo1))

#Añadir un nuevo elemento al arreglo:
arreglo1.append("Hola")
print(arreglo1)

#Añadir un nuevo elemento en una posición en específico
arreglo1.insert(1, "Xbox") # (posición a insertar, elemento a insertar)
print(arreglo1)

#Añadir varios elementos al final del arreglo::
arreglo1.extend([True, False, "No"]) # ([Elementos a insertar])
print(arreglo1)

#Concatenar arreglos (el segundo al final del primero):
arreglo3 = arreglo1+arreglo2
print(arreglo3)

#Buscar un elemento dentro del arreglo:
print("Adios" in arreglo3)

#Obtener el indice en el que esta un elemento:
print(arreglo3.index("No"))

#Obtener el número de veces que se repite un elemento:
print(arreglo1.count("Pc"))
print(arreglo2.count("Pc"))
print(arreglo3.count("Pc"))

#Quitar el primer elemento del arreglo que concuerde:
arreglo3.remove("Pc")
print(arreglo3)

#Limpiar todos los elements del arreglo: 
arreglo1.clear()
print(arreglo1)

#Invertir el orden de los elementos del arreglo:
arreglo2.reverse()
print(arreglo2)
 
 #Ordenar los elementos de un arreglo (Ascendente):
arreglo4 = [8,5,9,7,6,3,2,1,4,]
arreglo4.sort()
print(arreglo4)

#Ordenar los elementos de un arreglo (Descendente):
arreglo4.sort(reverse=True)
print(arreglo4)
