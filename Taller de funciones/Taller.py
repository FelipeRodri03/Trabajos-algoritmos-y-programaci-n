frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elemento-->str-->elemento
Salidas
lista-->list-->lista

def eliminar_un_caracter_de_toda_la_lista(lista:list, elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar
"""

#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista

def copia_lista(lista)->list:
  return lista.copy() 
"""
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista 
def numeros_enteros(lista:list):
  auxiliar=[]
  auxiliar_dos=[]
  for i in lista:
   auxiliar.append(float(i))
  for i in auxiliar:
    auxiliar_dos.append(int(i))
  return auxiliar_dos
"""
#Realizar una funcion que elimine un elemento de una lista
""""
Entradas:
lista-->list-->lista
elemento-->str-->elemento
Salidas
lista-->list-->lista 
"""
def elimina_elemento_lista(lista:list,elemento:str)->list:
  auxiliar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxiliar.append(a)
  return auxiliar



#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
""""
Entradas:
letra-->str-->letra
lista-->list-->lista
Salidas
lista-->list-->lista
"""
def letra(letra:str,lista:list)->list:
  auxiliar=[]
  for i in lista:
    if i[0]== letra:
      auxiliar.append(i)
  return auxiliar

#Realizar una funcion que retorne el tamaño de una lista   
""""
Entradas:
lista-->list-->lista
Salidas
tamaño-->int-->tamaño
"""
auxiliar=[]
def tamano_lista(lista:list)->int:
  a=len(lista)
  return a
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista-->list->lista
Salidas
tamaño-->int-->tamano
tipo-->type-->a
"""  
def informacion_lista(lista:list)->int:
  for i in lista:
   a=type(i)
   b=len(lista)
  return a, b
#Retornar una lista con los numero negativos  
"""
Entradas:

Salidas
"""
def numeros_negativos(lista:list)->list:
 auxiliar=[]
 for i in lista:
   if i[0]=="-":
     auxiliar.append(i)
 return auxiliar

#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
def posicion_elemento(elemento:str,lista:list):
  c=0
  auxiliar=[]
  for i in lista:
    auxiliar.append(i)
    a=" ".join(auxiliar)
    c=c+1 
    if(a==elemento):
      break
    auxiliar=[]   
  return c
if __name__ == "__main__":
  print(posicion_elemento("Frambuesa\n",lista_frutas))
"""
#realizar una funcion que agregue al final de archivo frutas una fruta

def frutas(elemento:str):
  with open (frutas.txt,"a") as f:
    f.write(elemento)
  return elemento


#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def repetir(elemento:str,lista:list)->int:
  for i in lista:
   return lista.count(elemento)
  
if __name__ == "__main__":
  print(repetir("21\n",lista_numeros))