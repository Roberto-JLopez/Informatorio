Algoritmo sin_titulo
//	2- validar una contrase�a ingresada por el usuario.
	Definir contrasenia, clave Como entero
	
	contrasenia = 1234
	clave = 0
	
	Imprimir "escriba la contrase�a"
	leer clave
	
	si clave == contrasenia Entonces
		Imprimir "La contrase�a es correcta"
	SiNo
		Imprimir "la contrase�a es incorrecta"
		Imprimir "vualva a colocar la contrase�a"
		leer clave
	FinSi
	
FinAlgoritmo
