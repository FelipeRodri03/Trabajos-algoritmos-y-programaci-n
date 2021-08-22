"""
Entradas
a-->int-->Digito
b-->int-->Digito
c-->int-->Digito
d-->int-->Digito
"""
a=int(input("Ingrese un solo dígito: "))
b=int(input("Ingrese un solo dígito: "))
c=int(input("Ingrese un solo dígito: "))
d=int(input("Ingrese un solo dígito: "))
#caja negra
e=str(c)+str(d)
f=int(e)
if (f<=50):
    g=(str(a)+str(b)+"00")
else:
    g=(str(a)+str(b+1)+"00")
print(g)