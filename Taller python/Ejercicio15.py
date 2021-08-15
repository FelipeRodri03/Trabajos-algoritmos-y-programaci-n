"""
Entradas
a-->int-->Valor de venta al publico
b-->int-->Valor final pagado
Salidas
d-->int-->Descuento final
"""
a=int(input())
b=int(input())
#caja negra
c=b/a
d=(1-c)*100
print("El descuento final es de "+str("{:.2f}".format(d)+"%"))