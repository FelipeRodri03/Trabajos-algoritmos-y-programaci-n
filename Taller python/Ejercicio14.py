"""
Entradas
a-->int-->Consumo de energía en kilowatts
b-->int-->Precio por kilowatt
Salidas
c-->int-->Valor a pagar
"""
a=int(input())
b=int(input())
#caja negra
c=a*b
print("El valor a pagar es de "+str(c))