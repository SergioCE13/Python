''' Plantemiento: Crear un programa que muestre la sumatoria de todos
    los números entre el 0 - 100'''

suma = 0;

for i in range(101): #Con un for delimitamos las iteraciones.
    print(f"{suma} + {i} =") #imprimimos la operacion realizada en la iteración actual.
    suma = suma + i #Se realiza la operación
    i +=1
    
print(suma)