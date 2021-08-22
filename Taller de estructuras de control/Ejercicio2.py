"""
Entradas
a-->int-->sueldo del trabajador
Salidas
b-->int-->Salario con aumento del 15%
c-->int-->Salario con aumento del 12%
"""
a=int(input())
#caja negra
if (a<900000):
    b=a+(a*0.15)
    print("Su salario es "+str(b))
else:
    c=a+(a*0.12)
    print("Su salario es "+str(c))