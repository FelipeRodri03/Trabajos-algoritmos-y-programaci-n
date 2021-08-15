"""
Entradas
a-->int-->Precio al contado
b-->int-->Precio adicional de cada cuenta
Salidas
c-->int-->Recargo de cuota
"""
a=int(input())
b=int(input())
c=(b*100)/a
print("El porcentaje de recargo por cuota es "+str(c)+"%")