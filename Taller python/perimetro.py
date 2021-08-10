"""""
Entradas
base--> float-->base
altura-->float-->altura
Salidas
perimetro-->float-->perimetro
area-->float-->area
"""
base=int(input("Escriba la base del rectangulo"))
altura=int(input("Escriba la altura del rectangulo"))
area=base*altura
perimetro=2*base+2*altura
print("el area del rectangulo es: "+str(area))
print("el perimetro del rectangulo es: "+str(perimetro))
