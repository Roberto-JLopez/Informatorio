Algoritmo sin_titulo
//	2- validar una contraseņa ingresada por el usuario.
	Definir contrasenia, clave Como entero
	
	contrasenia = 1234
	clave = 0
	
	Imprimir "escriba la contraseņa"
	leer clave
	
	si clave == contrasenia Entonces
		Imprimir "La contraseņa es correcta"
	SiNo
		Imprimir "la contraseņa es incorrecta"
		Imprimir "vualva a colocar la contraseņa"
		leer clave
	FinSi
	
FinAlgoritmo
