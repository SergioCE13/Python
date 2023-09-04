''' Ejercicio 10 Crear un programa que muestre la sumatoria de todos
    los números entre el 0 - 100'''

suma = 0;

for i in range(101):
    print(f"{suma} + {i} =")
    suma = suma + i
    i +=1
    
print(suma)