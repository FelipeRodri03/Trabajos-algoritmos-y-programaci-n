"""
Entradas
Tipo de combustible-->int-->a
"""
alcool=0
gasolina=0
diesel=0
#caja negra
while True:
    a=int(input())
    if (a==1):
        alcool+=1
    elif (a==2):
        gasolina+=1
    elif (a==3):
        diesel+=1
    elif (a>4):
        continue
    elif (a==4):
        break
print ("MUITO OBRIGADO")
print ("Alcool:",alcool)
print ("Gasolina:",gasolina)
print ("Diesel:",diesel)