Proceso Inicio_ventas
	Escribir "¿Cuál es el sueldo base?"
	Leer n1
	Escribir "¿Cuantas ventas realiza al mes?"
	Leer h
	t<-h*(n1*0.1)
	Escribir "La comision por las ventas es " t
	c<-n1+t
	Escribir "El sueldo total es " c
FinProceso
