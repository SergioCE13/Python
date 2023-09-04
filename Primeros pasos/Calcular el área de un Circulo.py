#Ejercicio Número 3 Obtener radio y logitud de un circulo en python
import math

radio = float(input("Ingresa el radio del circulo: "))

area = math.pi*radio**2
perimetro = 2*math.pi*radio

print("El area del circulo es: ",area)
print("El perímetro del circulo es: ",perimetro)
