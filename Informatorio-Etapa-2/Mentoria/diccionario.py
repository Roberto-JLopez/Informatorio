estudiante = {
    "nombre": "roberto",
    "apellido": "gonzalez",
    "direccion": "calle falsa 123",
    "dni": 12345678,
    "telefono": 123456789,
}

# #para buscar un valor se coloca la variable y entre corchetes la clave y nos devuelve el valor
# print(estudiante["nombre"])

# # agregar un nuevo par clave valor al diccionario  puede ser con el metodo update o directamente
estudiante.update({"fecha_nacimiento": "01/01/2000"})
estudiante["curso"] = "Introduccion a Python"

print(estudiante)


print(estudiante.items())        # devuelve una lista de tuplas con los pares clave valor])
# print(estudiante.keys())         # devuelve una lista con las claves
# print(estudiante.values())       # devuelve una lista con los valores