def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def calcular_mcd_lista(valores):
    if not valores:
        return 0

    mcd = valores[0]

    for i in range(1, len(valores)):
        mcd = calcular_mcd(mcd, valores[i])

    return mcd

def main():
    n = 0

    # Solicitar al usuario el número de valores
    while n <= 0:
        try:
            n = int(input("Ingrese la cantidad de valores: "))
            if n <= 0:
                print("El número de valores debe ser mayor que cero.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Crear una lista de enteros para almacenar los valores
    valores = []

    # Leer los valores desde el teclado
    print("Ingrese los valores uno por uno:")
    for i in range(n):
        try:
            valor = int(input())
            valores.append(valor)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Calcular el MCD de los valores utilizando el algoritmo de Euclides
    mcd = calcular_mcd_lista(valores)

    # Mostrar el resultado
    print("El MCD de los números ingresados es:", mcd)

if __name__ == "__main__":
    main()
