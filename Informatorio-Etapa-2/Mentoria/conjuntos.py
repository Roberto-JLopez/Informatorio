lista = [1, 3, 5, 2, 4 , 5, 5 ,2, 3]

# una forma facil de filtrar los elementos unicos es usando el set (transforma la lista en un conjunto)
# es porque los conjuntos no permiten elementos repetidos
# y los conjuntos no tienen orden, por lo que no importa el orden en el que se agreguen los elementos
# por lo que no importa el orden en el que se agreguen los elementos

conjunto = set(lista)
conjunto2= {3, 5, 6, 1, 2, 4, 7}  
conjunto3 = {"Hola", "Mundo","desde", "Python"}
# print(conjunto)
# print(conjunto2)
# print(conjunto3)

# # conjunto.add(elemento) Agrega el elemento al conjunto, recordar que en conjunto no se hablar de indices
# conjunto.add(7) # agrega un elemento al conjunto
# print(conjunto)
# # conjunto.remove(elemento) elimina el elemento del conjunto, si no existe lanza un error
# conjunto.remove(4) # elimina un elemento del conjunto
# print(conjunto)

conjunto4 = conjunto.union(conjunto3) # une los dos conjuntos
# print(conjunto4)

# recorridos 
for i in conjunto2:
    if i == 3:
        print("El elemento es 3")


if 7 in conjunto2:
    print("El elemento 7 esta en el conjunto2")

for i in conjunto2:
    print(i)
