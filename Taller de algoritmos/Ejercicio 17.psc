Proceso Inicio_Velocidad
	Escribir "Digite la velocidad de cada vehículo"
	Leer v1 v2
	Escribir "Digite la distancia entre los vehículos"
	Leer d
	t<-60*(d/(v1-v2))
	q<-abs(t)
	Escribir "El tiempo en el que se encuentran los dos vehículos es " q "minutos"	
FinProceso
