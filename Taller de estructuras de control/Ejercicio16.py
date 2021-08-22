"""
Entradas
a-->int-->a
b-->int-->b
c-->int-->c
Salidas
e-->int-->e
"""
a=int(input("digite valor a: "))
b=int(input("digite valor b: "))
c=int(input("digite valor c: "))
#caja negra
d=b**2-4*a*c
if (d==0):
    e=-b/(2*a)
elif (d>0):
    e="X1= "+str((-b+(b**2-4*a*c)**(1/2))/(2*a))+" y X2= "+str((-b-(b**2-4*a*c)**(1/2))/(2*a))
elif (d<0):
    e="No tiene solución en los reales"
print(e)