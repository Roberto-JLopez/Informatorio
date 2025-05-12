# lista vacia
# lista_vacia = []
# print(lista_vacia)
# print(type(lista_vacia))

# lista_vacia = list()
# print(lista_vacia)
# print(type(lista_vacia))

lista = [1, "Hola mundo", 1.5, "1", ["otra", "lista"], True, {}]

# # print(lista)
# print(lista[2])   # imprime el elemento en la posición 2

# # lista en trozos
# # imprime los elementos desde la posición 1 hasta la 3 (sin incluir la 3)
# print(lista[1:3])  
# print(lista[0:2]) # imprime los elementos desde la posición 0 hasta la 2 (sin incluir la 2)

# # imprime el último elemento
# print(lista[-1]) 

# # agrega un elemento al final
# lista.append("nuevo")
# print(lista)

# # agregar un numero en el indice número 3 y desplazar el resto de los elementos a la derecha
# lista.insert(3, "Adios")
# print(lista)

# # eleminar el ultimo elemento por defecto sino ingresar el índice
# lista.pop(3)
# print(lista)

# # modificar un elemento
# lista[1] = "Hola informatorio"
# print(lista)

# # forma de reccorer una lista (para iterar una lista)
# for i in lista:
#     print(i)

# #imprimir un elemento dentro de otra lista     
# print(lista[2][1]) # imprime el segundo elemento de la lista que está en la posición 2

# # imprime la longitud de la lista
# print(len(lista)) 


# # ---------- Tuplas    -------------------# # 

# # Tuplas son inmutables, no se pueden modificar, son indexadas, se pueden acceder a sus 
# elementos por su índice
# # Tuplas pueden contener elementos de diferentes tipos
# # Tuplas pueden contener listas, diccionarios, conjuntos, etc, pueden contener otras tuplas

# # tupla vacia 
# tupla = ()
# print(tupla)
# print(type(tupla))
# tupla = tuple()
# print(tupla)
# print(type(tupla))

tupla = (1, "Hola mundo", 1.5, "1", ["otra", "lista"], True, {})


# print(tupla)

# # indices de la tupla es igual que en la lista
# print(tupla[1])   # imprime el elemento en la posición 2


# print(tupla[1:3])  # imprime los elementos desde la posición 1 hasta la 3 (sin incluir la 3)    

# # contar los elementos de la tupla "lenght" 
# print(len(tupla)) # imprime la longitud de la tupla

# # para odenar una tupla se convierte a lista  y se hace con sorted
# tupla2 = (5, 4, 3, 2, 1)
# print(tupla2)

# tupla2 = sorted(tupla2) # ordena la tupla y la convierte a lista
# print(tupla2)

# # convertir la lista a tupla
# tupla2 = tuple(tupla2) # convierte la lista a tupla
# print(tupla2)


# # ---------- Conjuntos -------------------# #

# # conjunto vacio
# conjunto = set()  #cuando es vacio se usa set()
# conjunto1 = {} # esto no es un conjunto, es un diccionario
# print(type(conjunto))
# print(type(conjunto1))

# # los conjuntos no pueden tener elementos repetidos
# conjunto = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
# print(conjunto) # imprime el conjunto sin elementos repetidos}

# # union = todos los elemnetos del conjunto 1 y 2  sin elementos repetidos 
# conjA = {1, 2, 3}
# conjB = {1,4, 5, 6}
# print(conjA.union(conjB)) # imprime el conjunto

# # interseccion = todos los elemnetos que tienen en comun los conjuntos 1 y 2
# conjA = {1, 2, 3}
# conjB = {1, 4, 5, 6}
# print(conjA.intersection(conjB)) 

# # diferencia = todos los elemnetos que tiene el conjunto 1 y no el 2
# conjA = {1, 2, 3}
# conjB = {1, 4, 5, 6}  
# print(conjA.difference(conjB)) 

# # diferencia simetrica = todos los elemnetos que tienen en comun los conjuntos 1 y 2  
# conjA = {1, 2, 3}
# conjB = {1, 4, 5, 6}
# print(conjA.symmetric_difference(conjB)) 

# # agregar un elemento al conjunto
# conjunto = {1, 2, 3}
# conjunto.add(4)
# print(conjunto) # imprime el conjunto con el nuevo elemento

# # eliminar un elemento del conjunto
# conjunto = {1, 2, 3}  
# conjunto.remove(2) # elimina el elemento 2
# print(conjunto) # imprime el conjunto sin el elemento 2

# # eliminar un elemento del conjunto sin error si no existe
# conjunto = {1, 2, 3}  
# conjunto.discard(2) # elimina el elemento 2
# print(conjunto) # imprime el conjunto sin el elemento 2

# # longitud es igual que los anteriores
# conjunto = {1, 2, 3}
# print(len(conjunto)) # imprime la longitud del conjunto


# # ---------- Diccionarios -------------------# #

# # diccionario vacio
# diccionario = {}
# print(diccionario)
# print(type(diccionario))
# diccionario = dict()
# print(diccionario)
# print(type(diccionario))

# diccionario con elementos
diccionario_autos = { 
    "marca": "Ford",
    "modelo": "Fiesta",
    "año": 2020,
    "color": "rojo"
}
# print(diccionario_autos)

# print(diccionario_autos.keys()) # imprime las claves del diccionario
# print(diccionario_autos.values()) # imprime los valores del diccionario
# print(diccionario_autos.items()) # imprime las claves y valores del diccionario

# elimina el elemento con la clave marca
# diccionario_autos.pop("marca") # elimina el elemento con la clave marca
# print(diccionario_autos) # elimina el elemento con la clave año

# # agregar una clave y valor al diccionario
# diccionario_autos.update({"km": 10000}) # agrega la clave km y el valor 10000
# print(diccionario_autos) # imprime el diccionario con la nueva clave y valor

# for clave, valor in diccionario_autos.items():
#     print(clave, valor) # imprime las claves y valores del diccionario

# # longitud es igual que los anteriores
# print (len(diccionario_autos)) 

# # modifica el valor de la clave marca
# diccionario_autos["marca"] = "Chevrolet" 
# print(diccionario_autos) 