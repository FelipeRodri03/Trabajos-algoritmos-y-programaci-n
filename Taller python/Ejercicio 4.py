"""
Entradas
Valor-->float-->v
Salidas
Precio total-->float-->p
"""
v=float(input("Digite el valor de la compra:"))
#Caja Negra
d=v*0.15100
p=v-d
print("El valor total de la compra es: ",p)