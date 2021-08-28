"""
Entradas
Numero 1-->int-->n1
Numero 2-->int-->n2
"""
n1=int(input())
n2=int(input())
#caja negra
while True:
    if (n1>=n2):
        print(n1,"-",n2,"=",n1-n2)
        n1=n1-n2
    else:
        break