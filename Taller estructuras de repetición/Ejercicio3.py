contador=97
suma=97
#caja negra
for i in range (97,1004):
    if (contador%2==0):
        contador=contador+1
        suma=suma+contador
    elif (contador%2!=0):
        contador=contador+1
        suma=suma+0
    print(suma)
    