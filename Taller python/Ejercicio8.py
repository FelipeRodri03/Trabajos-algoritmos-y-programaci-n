"""
Entradas
a-->int-->lado
b-->int-->lado
c-->int-->lado
Salida
d-->float-->area final
"""
inp=input().split(" ")
a,b,c=inp
a=int(a)
b=int(b)
c=int(c)
#caja negra
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("El area del triangulo es "+str(d))
