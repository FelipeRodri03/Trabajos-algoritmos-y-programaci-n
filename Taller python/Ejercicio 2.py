"""
Entradas
Valor-->float-->v
Salidas
Precio total-->float-->p
"""
v=float(input("Digite el valor de la compra:"))
#Caja Negra
d=v*0.15
p=v-d
#Salidas
print("El valor total de la compra es: "+str(p))