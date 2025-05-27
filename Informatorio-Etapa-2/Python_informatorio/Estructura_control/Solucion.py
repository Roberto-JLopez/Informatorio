
# # Resolucion a problmeatica

votantes = set()
menu = {}
indice_comida = 0
print("Bienvenido a la votacion de las comidas") 
while True:
    comida = input("Ingrese la comida que desea pedir, y 'salir' para pasar a registrar los votantes: ")
    if comida.lower() == "salir":
        if len(menu) == 0:
            print("Por lo menos una comida tiene que ser elegida")
            continue
        else:                                   
            print("\nPasamos a cargar los votantes")
            break
    else:
          
        menu[comida] = (len(menu) + 1)
        
      

while True:        
    votante = input("Ingrese el nombre del votante ('salir' para terminar): ")
    if votante.lower() == "salir":
        if len(votantes) == 0:
            print("Por lo menos uno tiene que votar")
            continue
        else:
            print("\nPasamos a votar")
            break
    if votante in votantes:
        print("El votante ya fue agregado, ingrese otro")
    else:
        votantes.add(votante)
        print(f"Votante agregado {votantes}")



resultado = []

for votante in votantes:
    for clave, valor in menu.items():
        print(f"{valor} - {clave}")
    voto = int(input(f"{votante} ingrese su voto: "))
    while voto not in range(1, len(menu)+1):
        print("Voto no valido")
        voto = int(input(f"{votante} ingrese su voto: "))
    comida_elegida = ""
    for clave, valor in menu.items():
        if voto == valor:
            comida_elegida = clave
    if voto in range(1, len(menu)+1):
      print("Voto registrado")
      resultado.append(comida_elegida)

conteo_votos = {}  
for comida in resultado:
  if comida in conteo_votos:
    conteo_votos[comida] += 1
  else:
    conteo_votos[comida] = 1

# Mostrar el conteo de votos
for comida, votos in conteo_votos.items():
    print(f"{comida}: {votos} votos")

# Obtener el máximo de votos
max_votos = max(conteo_votos.values()) if conteo_votos else 0

# Obtener todas las comidas con el máximo de votos
ganadores = [comida for comida, votos in conteo_votos.items() if votos == max_votos]

# Mostrar el resultado
if len(ganadores) == 1:
    print(f"El ganador es: {ganadores[0]} con {max_votos} votos")
elif len(ganadores) > 1:
    print(f"Empate entre: {', '.join(ganadores)} con {max_votos} votos cada uno")

print("Gracias por participar")
