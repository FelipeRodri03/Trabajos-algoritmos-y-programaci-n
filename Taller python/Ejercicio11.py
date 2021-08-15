"""
Entradas
a-->str-->Nombre del trabajador
b-->int-->Hora normal en pesos
c-->int-->Horas normales trabajadas
d-->int-->Horas extras trabajadas
e-->int-->Cantidad de hijos
Salidas
i-->int-->Salario final
"""
a=str(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
#caja negra
f=b*c
g=d*(b+(b*0.25))
h=f-(f*.014)
i=h+250000+(173000*e)+180000+g
print("El sueldo total del trabajador es de "+str(i))