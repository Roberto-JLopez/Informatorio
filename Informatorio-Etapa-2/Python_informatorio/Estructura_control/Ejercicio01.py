print("\nBienvenido a la votación de comidas")
print("El programa tiene 3 partes: \n1. Registro de comidas\n2. Registro de votantes\n3. Votación")
print("Vamos por la primera. \nRegistro de comidas (escriba 'salir' para pasar a la 2da)\n")

comidas_elegidas = {}
while True:
    comida = input("Ingrese la comida: ")
    if len(comidas_elegidas) == 0 and comida.lower() == "salir":
        print("Tiene que haber al menos una comida para salir")
        
    elif comida in comidas_elegidas:
        print("La comida ya fue elegida, ingrese otra")
    elif comida.lower() == "salir":
        print("\nPasamos a cargar los votantes\n")
        break
    else:
        comidas_elegidas[comida] = (len(comidas_elegidas) + 1)

votantes_cargados = set()
while True:
    votantes = input("Ingrese el nombre del votante ('salir' para avanzar): ")
    if len(votantes_cargados) == 0 and votantes.lower() == "salir":
        print("Tiene que haber al menos un votante para salir")
    elif votantes in votantes_cargados:
         print("El votante ya fue agregado, ingrese otro")
    elif votantes.lower() == "salir":
        print("\nPasamos a votar\n")
        break
    else:
        votantes_cargados.add(votantes)


votaciones = {}
comida_votada = ""
for votante in range (len(votantes_cargados)):
    print(f"Votante N°{votante+1} elija una opción: ")
    for comida, indice in comidas_elegidas.items():
        print(f"{indice} - {comida}")
    voto= int(input("Ingrese su voto: "))
    while True:
           if voto not in comidas_elegidas.values():
            print("Opción no válida, vuelva a elegir")
            voto= int(input("Ingrese su voto: "))
           else:
               break
    for comida, indice in comidas_elegidas.items():
        if voto == indice:
            comida_votada = comida
    if comida_votada in votaciones:
        votaciones[comida_votada] += 1
    else:
        votaciones[comida_votada] = 1

print("\nResultados de la votación")
maximo = 0
ganador = []

for clave, valor in votaciones.items():
    print(f"{clave}: {valor} votos")
    if valor > maximo:
        maximo = valor
        ganador = [clave]
    elif valor == maximo:
        ganador.append(clave)
                
if len(ganador) == 1:
    print(f"La comida ganadora es: {ganador[0]}")   
else:
    print(f"Hay un empate entre: {', '.join(ganador)}")

