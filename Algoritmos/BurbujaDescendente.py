def ordenar_burbuja_descendente(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arreglo[j] < arreglo[j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto (descendente)
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

def mostrar_arreglo(arreglo):
    for elemento in arreglo:
        print(elemento, end=" ")
    print()

def main():
    # Leer el tamaño del arreglo
    n = int(input("Ingrese el tamaño del arreglo: "))

    # Crear un arreglo de enteros de tamaño n
    arreglo = []

    # Solicitar al usuario que llene el arreglo
    print("Ingrese los elementos del arreglo:")
    for i in range(n):
        elemento = int(input())
        arreglo.append(elemento)

    # Mostrar el arreglo original
    print("Arreglo original:")
    mostrar_arreglo(arreglo)

    # Llamar al método para ordenar los elementos del arreglo en orden descendente.
    ordenar_burbuja_descendente(arreglo)

    # Mostrar el arreglo ordenado en orden descendente
    print("Arreglo ordenado descendentemente:")
    mostrar_arreglo(arreglo)

if __name__ == "__main__":
    main()
