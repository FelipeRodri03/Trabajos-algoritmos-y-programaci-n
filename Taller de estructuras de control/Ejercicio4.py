"""
Entradas
a-->int-->Monto total de la compra
"""
a=int(input())
#caja negra
if (a<5000000):
    b=(a*0.7)
    c=(a*0.3)
    d=c+(c*0.2)
    print("La cantidad que debe gastar la empresa es de "+str(b)+" ,la cantidad total del credito es de "+str(d)+" y el monto de los intereses es "+str(c*0.2))
else:
    e=a*0.55
    f=a*0.3
    g=a*0.15
    h=g+(g*0.2)
    print("La cantidad que debe gastar la empresa es de "+str(e)+" ,la cantidad total del prestamo es de "+str(h)+" el monto de los intereses es "+str(g*0.2)+" y la cantidad prestada del banco es "+str(f))