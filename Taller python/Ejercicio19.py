"""
Entradas
a-->int-->Precio de la compra
b-->int-->Ganancia de la venta
c-->int-->Cantidad de docenas
"""
a=int(input())
b=int(input())
c=int(input())
#caja negra
d=a-b
e=a/c
f=(d*100)/e
print("El porcentaje de ganancia de la compra es "+str(f)+"%")