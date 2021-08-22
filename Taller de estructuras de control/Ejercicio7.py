"""
Entradas
a-->int-->kilometraje
Salidas
b-->int-->Valor a cancelar
"""
a=int(input())
#caja negra
if (a<300):
    b=("Se deben cancelar 50000")
elif (a>300 and a<1000):
    b=a-300
    c=b*30000
    b=("Se deben cancelar "+str(70000+c))
elif (a>300 and a>1000):
    d=a-1000
    e=d*90000
    b=("Se deben cancelar "+str(150000+e))
print(b)