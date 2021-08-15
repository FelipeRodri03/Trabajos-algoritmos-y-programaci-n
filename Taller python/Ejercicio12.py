"""
Entradas
a-->int-->Tarea de matematicas
b-->int-->Tarea de matematicas
c-->int-->Tarea de matematicas
d-->int-->Examen final de matematicas
e-->int-->Tarea de fisica
f-->int-->Tarea de fisica
g-->int-->Examen final de fisica
h-->int-->Tarea de quimica
i-->int-->Tarea de quimica 
j-->int-->Tarea de quimica
k-->int-->Examen final de quimica
Salidas
l -->int-->Nota final de matematicas
m-->int-->Nota final de fisica
n-->int-->Nota final de quimica
"""
inp=input().split(" ")
a,b,c,d,e,f,g,h,i,j,k=inp
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
g=int(g)
h=int(h)
i=int(i)
j=int(j)
k=int(k)
#caja negra
l=(d*0.9)+(((a+b+c)/3)*0.1)
m=(g*0.8)+(((e+f)/2)*0.2)
n=(k*0.85)+(((h+i+j)/3)*0.15)
print("La nota final de matematicas es "+str(l))
print("La nota final de fisica es "+str(m))
print("La nota final de quimica es "+str(n))