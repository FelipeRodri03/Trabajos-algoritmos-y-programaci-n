"""
Entradas
a--=int-->Chelines austriacos
c--=int-->Dragmas griegos
f--=int-->Pesetas
Salidas
b-->int-->Pesetas
e-->int-->francos franceses
g-->int-->dolares
h-->int-->liras italianas
"""
a=int(input())
#caja negra
b=a*122.499
c=int(input())
d=c*88.607
e=d/20.110
f=int(input())
g=f/122.49
h=f/9.289
print(str(a)+" chelines austriacos son " +str(b)+ " pesetas")
print(str(c)+" dracmas griegos son "+str("{:.2f}".format(e)+ " francos franceses"))
print(str(f)+" pesetas son "+str("{:.2f}".format(g)+ " dolares"))
print(str(f)+" pesetas son "+str("{:.2f}".format(h)+ " liras italianas"))