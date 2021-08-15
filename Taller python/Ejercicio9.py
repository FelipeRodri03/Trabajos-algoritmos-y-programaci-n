"""
Entradas
a-->int-->horas trabajadas
b-->int-->salario por hora
Salidas
e-->int-->salario neto
"""
a=int(input())
b=int(input())
#caja negra
c=a*b
d=c*0.2
e=c-d
print("El salario neto es "+str(e))