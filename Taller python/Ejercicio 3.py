"""
Entradas
Sueldo-->int-->a
Veces vendidas-->int-->b
Salidas
Sueldo total-->int-->d
"""
a=int(input())
b=int(input())
#caja negra
c=b*(a*0.1)
d=a+c
print(d)