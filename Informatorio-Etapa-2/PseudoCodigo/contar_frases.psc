Algoritmo contar_frases
	Definir frases Como Caracter
	Definir contador Como Entero
	contador = 0
	frases <- ""
	
	Escribir Mayusculas("Contador de frases")
	Escribir "Escriba tantas frases como desee: "
	Escribir "Para finalizar escriba " "Fin"  
	Leer frases
		Mientras frases <> "fin" Hacer
		contador =+ 1 // es lo mismo que contador <- contador +1
		Escribir "Ingrese una nueva frase :"
		leer frases
	FinMientras
	si contador ==0 Entonces
		
		Escribir  "Usted no escribio ninguna frase"
		
	SiNo si contador == 1 Entonces
			
			Escribir "Ud escribio " contador " frase."
		SiNo
			Escribir "Ud escribio " contador " frases."
		FinSi
		
	FinSi
	 
FinAlgoritmo
 