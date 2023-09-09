#Operadores Lógicos en Python

a=10
b=20
c=30

#Operador AND: 
print((a<b) and (b<c))
    # AND: Devuelve True si ambos operandos son True, de lo contrario, devuelve False.

#Operador NOT:
print(not((a<b) and (b<c)))
    # NOT: Devuelve la negación lógica del operando. Si el operando es True, not lo convierte en False, y viceversa.

#Operador OR:
print(a>b) or (b<c)
    # OR: Devuelve True si al menos uno de los operandos es True, de lo contrario, devuelve False.

#Operador sintético XOR:
print(not((a>b) and (b<c)))
    # XOR: Devuelve True si exactamente uno de los operandos es True, de lo contrario, devuelve False.

