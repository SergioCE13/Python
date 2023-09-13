import math

def cuadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    return area, perimetro

def triangulo(base, altura):
    area = 0.5 * base * altura
    lado1 = math.sqrt((base / 2) ** 2 + altura ** 2)
    perimetro = base + 2 * lado1
    return area, perimetro

def rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def rombo(diagonal_mayor, diagonal_menor):
    area = 0.5 * diagonal_mayor * diagonal_menor
    perimetro = 4 * math.sqrt((0.5 * diagonal_mayor) ** 2 + (0.5 * diagonal_menor) ** 2)
    return area, perimetro

opcion = 0
while opcion !=5:
    print("Seleccione la figura con la que desea trabajar:")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Rectángulo")
    print("4. Rombo")
    print("5. Salir")

    opcion = int(input("Ingrese el número de la figura: "))

    if opcion == 1:
        lado = float(input("Ingrese la longitud del lado del cuadrado: "))
        area, perimetro = cuadrado(lado)
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area, perimetro = triangulo(base, altura)
    elif opcion == 3:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area, perimetro = rectangulo(base, altura)
    elif opcion == 4:
        diagonal_mayor = float(input("Ingrese la longitud de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la longitud de la diagonal menor del rombo: "))
        area, perimetro = rombo(diagonal_mayor, diagonal_menor)
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")
