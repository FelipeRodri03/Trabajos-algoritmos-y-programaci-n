"""
Entradas
Cantidad de hombres-->int-->a
Cantidad de mujeres-->int-->b
Salidas
Porcentaje de hombres-->float-->d
Porcentaje de mujeres-->float-->e
"""
inp=(input(). split(" "))
a,b=inp
a=int(a)
b=int(b)
#caja negra
c=a+b
d=(a*100)/c
e=(b*100)/c
print("El porcentaje de hombres es "+str(d)+"%" )
print("El porcentaje de mujeres es "+str(e)+"%")