import math

# numero = 4


# raiz = math.sqrt(numero)
# potencia = math.pow(numero, 2)
# print(f"La potencia de {numero} al cuadrado es {potencia}")
# print(f"La raíz cuadrada de {numero} es {raiz}")

# # a fines practicos colocamos los modulos abajo pero 
# # hay que colocarlos arriba en la parte superior

# #########################################################

import random as rd # se le pone un alias al modulo en este caso rd

#simular lanzamiento de moneda

# resultado = random.randint(0, 1)
# if resultado == 0:
#     print("Cara")
# else:
#     print("Cruz")

# resultado = rd.randint(0, 1)
# if resultado == 0:
#     print("Cara")
# else:
#     print("Cruz")


# from datetime import *  # asi no, porque ocupa muchos recursos 
# from datetime import datetime, date # asi si

# # fecha_actual = date.today()
# # print(fecha_actual)

# def calcular_edad():

#     fecha_nacimiento = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")   
#     nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()

#     hoy = date.today()
#     edad = (hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)))
     
#     # print(hoy.year - nacimiento.year) # devuelve la edad sin tener en cuenta si ya cumplio años
#     # print((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)) # devuelve True o False si ya cumplio años(True=1, False=0)
   
#     return edad

#     # print(fecha_nacimiento)
#     # print(nacimiento)
#     # print(hoy)


# #como tarea completar cuantos dias falta para cumplir años
# print(f"Su edad es: {calcular_edad()} años")


# modula para importar a otro archivo

def saludar():
    print("Hola mundo desde el modulo mod.py")

# saludar()

def potenciar(n):
    potencia= math.pow(n, 2) 
    return potencia
