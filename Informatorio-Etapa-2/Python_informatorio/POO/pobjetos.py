

class Persona:
    #CONSTRUCTOR
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"{self.nombre} dice buenos días.")

#instanciar objeto persona1
persona1 = Persona("Pedro", 33)
print(f"Hola, {persona1.nombre}")
print(f"Tu edad es: {persona1.edad} años")
persona1.saludar()

#instanciar persona2
persona2 = Persona("Juan", 22)
print(f"Hola, {persona2.nombre}")
print(f"Tu edad es: {persona2.edad} años")
persona2.saludar()

#instanciar persona3
persona3 = Persona("Roberto", 22)
print(f"Hola, {persona3.nombre}")
print(f"Tu edad es: {persona3.edad} años")
persona3.saludar()