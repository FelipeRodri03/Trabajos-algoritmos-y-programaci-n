"""
Entradas
a-->int-->edad
b-->str-->sexo
c-->str-->edad o meses
d-->int-->porcentaje de hemoglobina
Salidas
e-->int-->Resultado de la anemia
"""
c=str(input("Digite 1 si tiene años o 2 si tiene meses: "))
a=int(input("Digite su edad: "))
d=int(input("Ingrese su porcentaje de hemoglobina: "))
b=str(input("Digite 1 si es hombre o 2 si es mujer: "))
#caja negra
if (c==2):
    if (a<=1 and d>=13):
        e="No tiene anemia"
    else:
        e="Tiene anemia"
    if ((a>1 and a<=6) and (d>=10)):
        e="No tiene anemia"
    else:
        e="Tiene anemia"
    if ((a>6 and a<=12) and (d>=11)):
        e="No tiene anemia"
    else:
        e="Tiene anemia"
else:
    if ((a>=1 and a<=5) and (d>=11.5)):
        e="No tiene anemia"
    else:
        e="Tiene anemia"
    if ((a>5 and a<=10) and (d>=12.6)):
        e="No tiene anemia"
    else:
        e="Tiene anemia"
    if ((a>10 and a<=15) and (d>=13)):
        e="No tiene anemia"
    else:
        e="Tiene anemia"
    if (a>15):
        if (b==2):
            if (d>=12):
                e="No tiene anemia"
            else:
                e="Tiene anemia"
        else:
            if (d>=14):
                e="No tiene anemia"
            else:
                e="Tiene anemia"    
print("Usted "+str(e))       