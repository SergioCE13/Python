import random

def mostrar_arreglo(arreglo):
    for elemento in arreglo:
        print(elemento, end=" ")
    print()

def busqueda_secuencial(arreglo, x):
    contador = 0
    for elemento in arreglo:
        if elemento == x:
            contador += 1
    return contador

def main():
    # Leer el tamaño del arreglo
    n = int(input("Ingrese el tamaño del arreglo: "))

    # Crear un arreglo de enteros de tamaño n y llenarlo con números aleatorios entre 0 y 100
    arreglo = [random.randint(0, 10) for _ in range(n)]

    # Leer el número a buscar
    x = int(input("Ingrese el número a buscar: "))

    # Realizar la búsqueda secuencial
    contador = busqueda_secuencial(arreglo, x)

    # Mostrar los resultados
    if contador > 0:
        print(f"El número {x} se encontró en el arreglo {contador} veces.")
    else:
        print(f"El número {x} no se encontró en el arreglo.")

    # Mostrar el arreglo generado
    print("Arreglo generado:")
    mostrar_arreglo(arreglo)

if __name__ == "__main__":
    main()
