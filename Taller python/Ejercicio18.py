"""
Entradas
a-->int-->Cantidad prestada
b-->int-->Cantidad pagada
Salidas
d-->int-->Tasa de interes
"""
a=int(input())
b=int(input())
c=b-a
d=(c/(a*4))*100
print("La tasa de interes es del "+str(d)+"%")