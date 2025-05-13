## ----------------------------------------------------------------------------
# # 1. Definir una lista con 10 elementos.
# lista = ['uno', 1 ,3, 4, 5, 6, 0, 'dos', 'hola mundo', 8]
# print(len(lista))

# # a. Agregar 1 elemento al final
# lista.append('probando append')
# print(lista)

# # b. Agregar 1 elemento al inicio
# lista.insert(0, 'principio')
# print(lista)

# # c. Eliminar el ultimo elemento
# lista.pop(-1)
# print(lista)

# # d. Eliminar el primer elemento
# lista.pop(0)
# print(lista)

# # c. Modificar el índice 3
# lista[3] = 'modificando'
# print(lista)

# # e. Agregar 1 elemento en el índice 7
# lista.insert(7, 'agregando en indice 7')
# print(lista)

# # f. Ordenar la lista de manera ascendente y luego descendente
# lista2= [5, 3, 6, 10, 2, 4, 1, 0, 8, 1]
# lista2.sort()
# print(lista2)

# lista2.sort(reverse = True)
# print(lista2)

## -------------------------------------------------------------------------

# # 2. Definir una tupla con 10 elementos.
# tupla = ('uno', 1 ,3, 4, 5, 6, 0, 'dos', 'hola mundo', 8)
# print(len(tupla))
# print(type(tupla))
# print(tupla)

# # a. Modificar, eliminar, agregar 1 elemento
# print('No se puede modificar, eliminar o agregar elementos a una tupla')

# # 3. Definir un conjunto con 10 elementos.
conjunto = {'dos', 'uno', 1, 3, 4, 6, 2, 0, 9, 'diez'}
# print(type(conjunto))
# print(len(conjunto))
# print(conjunto)

# a. Agregar 5 elementos iguales
conjunto.update( {1 , 1, 1, 1 ,1, 1})
print(conjunto)
print('No se pueden agregar elementos iguales a un conjunto')

# b. Filtrar los elementos únicos de [1, 2, 2, 3, 3, 3]


# 4. Definir un diccionario para una persona y completar con sus datos personales:
# nombre, apellido, dirección, dni, teléfono, fecha de nacimiento, edad, país.
# a. Acceder solo al teléfono
# b. Modificar el numero de teléfono
# c. Modificar el pais