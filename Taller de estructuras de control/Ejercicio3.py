"""
Entradas
a-->int-->dato
b-->int-->dato
c-->int-->dato
d-->int-->dato
"""
inp=input().split()
a,b,c,d=inp
a=int(a)
b=int(b)
c=int(c)
d=int(d)
#Caja negra
if (d==0):
    print(((a-c)**2))
else:
    print(((a-b)**3))