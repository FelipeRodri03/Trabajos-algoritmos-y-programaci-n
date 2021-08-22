"""
Entradas
a-->int-->cantidad invertida
b-->int-->tasa de interés
Salidas
d-->int-->Interes final
"""
a=int(input())
b=float(input())
#caja negra
c=a*b
if (c<100000):
    print("Los interes son menores que 100000")
else:
    print("Los intereses son mayores a 100000")