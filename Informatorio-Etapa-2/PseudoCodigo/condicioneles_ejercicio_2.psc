Algoritmo sin_titulo
//	2- validar una contraseña ingresada por el usuario.
	Definir contrasenia, clave Como entero
	
	contrasenia = 1234
	clave = 0
	
	Imprimir "escriba la contraseña"
	leer clave
	
	si clave == contrasenia Entonces
		Imprimir "La contraseña es correcta"
	SiNo
		Imprimir "la contraseña es incorrecta"
		Imprimir "vualva a colocar la contraseña"
		leer clave
	FinSi
	
FinAlgoritmo
