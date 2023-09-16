import random

def mostrar_arreglo(arreglo):
    for elemento in arreglo:
        print(elemento, end=" ")
    print()

def busqueda_binaria(arreglo, x):
    izquierda = 0
    derecha = len(arreglo) - 1

    while izquierda <= derecha:
        medio = izquierda + (derecha - izquierda) // 2

        if arreglo[medio] == x:
            return medio

        if arreglo[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # El elemento no se encontró en el arreglo

def main():
    random.seed()
    
    # Leer el tamaño del arreglo
    n = int(input("Ingrese el tamaño del arreglo: "))

    # Crear un arreglo de enteros de tamaño n y llenarlo con números aleatorios entre 0 y 10
    arreglo = [random.randint(0, 10) for _ in range(n)]

    # Leer el número a buscar
    x = int(input("Ingrese el número a buscar: "))

    # Mostrar el arreglo original
    print("Arreglo original:")
    mostrar_arreglo(arreglo)

    # Realizar la búsqueda binaria
    resultado = busqueda_binaria(arreglo, x)

    # Mostrar los resultados
    if resultado != -1:
        print(f"El número {x} se encontró en el arreglo en la posición {resultado} por primera vez.")
    else:
        print(f"El número {x} no se encontró en el arreglo.")

if __name__ == "__main__":
    main()
