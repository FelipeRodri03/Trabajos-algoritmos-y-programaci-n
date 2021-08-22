"""
Entradas
p-->int-->dato
q-->int-->dato
Salidas
b-->int-->Condicion de la expresion
"""
p=int(input())
q=int(input())
a=p**3+q**4-(2*p**2)
if (a>680):
    b=("P y Q satisfacen la expresión")
else:
    b=("P y Q no satisfacen la expresión")
print(b)
