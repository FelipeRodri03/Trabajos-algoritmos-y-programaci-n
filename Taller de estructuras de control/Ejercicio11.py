"""
Entradas
a-->float-->Grados fahrenheit
Salidas
d-->float-->deporte
"""
t=float(input())
#Caja negra
if (t>85):
    d="Natación"
elif (t>70 and t<=85):
    d="Tennis"
elif (t>32 and t<=70):
    d="Golf"
elif (t>10 and t<=32):
    d="Esquí"
else:
    d="Marcha"
print(d)