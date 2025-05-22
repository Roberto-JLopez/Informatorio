# VARIABLES Y TIPOS DE DATOS EN PYTHON
# Definición de variables
# En Python no es necesario declarar el tipo de variable, ya que es un lenguaje de tipado dinámico.
# Esto significa que no es necesario especificar el tipo de variable al momento de declararla.
# Python infiere el tipo de variable según el valor que se le asigne.
# Por ejemplo, si se le asigna un número entero a una variable, Python la considerará de tipo entero.
# Si se le asigna un número decimal, la considerará de tipo decimal.
# Si se le asigna un texto, la considerará de tipo texto.
# Si se le asigna una lista, la considerará de tipo lista.
# Si se le asigna una tupla, la considerará de tipo tupla.
# Si se le asigna un diccionario, la considerará de tipo diccionario.
# Si se le asigna un conjunto, la considerará de tipo conjunto.
# Si se le asigna un rango, la considerará de tipo rango.

# Tipos de datos en Python
# 1. String o cadena de texto: se utiliza para almacenar texto.
# 2. Entero: se utiliza para almacenar números enteros.
# 3. Decimal: se utiliza para almacenar números decimales.
# 4. Booleano: se utiliza para almacenar valores booleanos (True o False).
# 5. Lista: se utiliza para almacenar una colección de elementos.
# 6. Tupla: se utiliza para almacenar una colección de elementos inmutables.
# 7. Diccionario: se utiliza para almacenar una colección de pares clave-valor.
# 8. Conjunto: se utiliza para almacenar una colección de elementos únicos.
# 9. Rango: se utiliza para almacenar una secuencia de números enteros.
# 10. None: se utiliza para representar la ausencia de valor.

nombre = 'Juan'
numero = 10
numero_decimal = 10.5
booleano = False
lista = [1, 2, 3, 4, 5] 
tupla = (1, 2, 3, 4, 5)
diccionario = {'nombre': 'Juan', 'edad': 30}
conjunto = {1, 2, 3, 4, 5}
rango = range(1, 10)

# Imprimir variables
#print('esto es un string o cadena de texto', nombre, type(nombre))
#print('esto es un numero entero', numero, type(numero))
#print('esto es un numero decimal', numero_decimal, type(numero_decimal))  
#print('esto es un booleano', booleano, type(booleano))
#print('esto es una lista', lista, type(lista))
#print('esto es una tupla', tupla, type(tupla))
# Imprimir variables compuestas                 
#print('esto es un diccionario', diccionario, type(diccionario))
#print('esto es un conjunto', conjunto, type(conjunto))
#print('esto es un rango', rango, type(rango))

#if ('condicion'):
    # codigo a ejecutar si se cumple la condicion
#fuera de la condicion o bloque if
#else:
     # codigo a ejecutar si no se cumple la condicion
#fuera de la condicion o bloque else



#edad = 15


#Ejemplo de condicionales

#if edad >= 18 and edad < 65:
#    print('Eres mayor de edad')
#elif edad >=65 and edad < 100:
#    print('Usted se puede jubilar')
#elif edad >= 100:
#    print('Usted es un anciano a punto de partir')
#else:
#    print('Eres menor de edad')


#Ejemplo de condicionales anidados (evitar  hacerlo a los anidados)


# edad = 15

# if edad >= 18:
#    if edad > 65:
#        print('Eres mayor de edad')
#        if edad >= 100:
#            print('Usted es un anciano a punto de partir')
#            if edad >= 150:
#                print('Usted es un cadaver')
# else:
#    print('Eres menor de edad')


edad = input('ingrese su edad: ')
print("vamos a mostrar los tipos de datos")
print (type(edad))

conversion = int(edad) 
print (type(conversion))