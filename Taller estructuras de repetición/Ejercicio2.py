contador=0
#caja negra
while True:
    contador+=1
    if (contador%2==0):
        continue
    elif (contador%7==0):
        continue
    elif (contador>=100):
        break
    print(contador)