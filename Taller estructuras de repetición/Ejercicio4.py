contador=6
suma=contador
#caja negra
for i in range(1,12):
    contador=contador+5
    suma=suma+contador
    print(contador)
    if (contador==61):
     print(suma)