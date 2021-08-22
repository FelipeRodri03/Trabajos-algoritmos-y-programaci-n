"""
Entradas
a-->int-->Salario bruto
b-->int-->Ventas del departamento 1
c-->int-->Ventas del departamento 2
d-->int-->Ventas del departamento 3
"""
a=int(input("Ingrese salario bruto: "))
b=int(input("Ingrese ventas del departamento 1: "))
c=int(input("Ingrese ventas del departamento 2: "))
d=int(input("Ingrese ventas del departamento 3: "))
#caja negra
e=b+c+d
f=(33*e)/100
if (b>f):
    print("El salario de los trabajadores del departamento 1 es "+str(a+(a*0.2)))
else:
    print("El salario de los trabajadores del departamento 1 es "+str(a))
if (c>f):
    print("El salario de los trabajadores del departamento 2 es "+str(a+(a*0.2)))
else:
    print("El salario de los trabajadores del departamento 2 es "+str(a))
if (d>f):
    print("El salario de los trabajadores del departamento 3 es "+str(a+(a*0.2)))
else:
    print("El salario de los trabajadores del departamento 3 es "+str(a))
