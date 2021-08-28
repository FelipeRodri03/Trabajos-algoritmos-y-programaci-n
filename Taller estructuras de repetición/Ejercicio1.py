"""
Entradas
Dato n-->int-->n
Dato k-->int--k
"""
n=int(input())
k=int(input())
#caja negra
while True:
    if (k<=n):
        print(n)
        n-=1
    else:
        break  
