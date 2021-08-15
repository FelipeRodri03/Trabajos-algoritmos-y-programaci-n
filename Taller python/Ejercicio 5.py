"""
Entradas
3 calificaciones parciales-->int-->a,b,c
Examen final-->int-->d
Trabajo final-->int-->e
Salidas
Nota final-->float-->nf
"""
input1=input().split(" ")
a,b,c=input1
a=int(a)
b=int(b)
c=int(c)
d=int(input())
e=int(input())
#caja negra
cc=(a+b+c)/3
nf=cc*0.55+d*0.3+e*0.15
print("{:.3f}".format(nf))