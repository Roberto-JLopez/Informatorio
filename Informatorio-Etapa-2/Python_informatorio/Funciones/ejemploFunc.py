# # sin parametros y no retorna valores
# def saludar ():
#     print("Hola mundo")

# # llamar o invocar la funcion    
# saludar()

# con retorno y sin parametros

# def saludar():
#     return "Hola mundo"

# saludo = saludar()
# print(saludo)

# def multiplicar(numero):
#     m = numero * 2
#     return m

# resultado = multiplicar(4)
# print(resultado)

# print(multiplicar(5))

# ARGS basicamente es un argumento que se le pasa a la funcion y se convierte en una tupla
# sin importar la cantidad de argumentos que se le pase, osea va a recibir una cantidad indefinida de argumentos

def sumar(*args):
    #variable local
    total = 0
    for numero in args:
        total += numero
    return total


resultado1 = sumar(1,22,3,44,5)
print(f"el resultado de la suma es {resultado1}")

# KWARGS basicamente es un argumento que se le pasa a la funcion y se convierte en un diccionario
#va a recibir clave y valor.

def db(**kwags):
    config = {
        "host": "localhost",

    }
