def esPerfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

def nPerfectos(n):
    numeros_perfectos = []
    numero = 2  # Empezamos con el primer número perfecto conocido (6)
    while len(numeros_perfectos) < n:
        if esPerfecto(numero):
            numeros_perfectos.append(numero)
        numero += 1
    return numeros_perfectos

n = int(input("Ingrese la cantidad de números perfectos que desea calcular: "))
numeros_perfectos = nPerfectos(n)

print(f"\nLos primeros {n} números perfectos son:")
for numero_perfecto in numeros_perfectos:
    print(numero_perfecto)
