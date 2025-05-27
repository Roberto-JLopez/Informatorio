votantes = set()
comidas = set()
votos_comida = {}  # Diccionario para almacenar los votos por comida




print("\nBienvenido a la votacion de las comidas, cuando ya tengamos todas las opciones a votar escriba 'salir'")
while True:
    comida = input("\nIngrese la comida: ")
    if comida == "salir":
        if len(comidas) == 0:
            print("Por lo menos una comida tiene que ser elegida")
        else:
            print("Pasamos a cargar los votantes")
            comidas = sorted(list(comidas))  # Convertir a lista ordenada para mostrar con índice consistente
            for comida in comidas:
                votos_comida[comida] = 0  # Inicializar el contador de votos para cada comida
            break
    else:
        comidas.add(comida)
        print(comidas)

while True:
    votante = input("\nIngrese el nombre del votante, y 'salir' para terminar: ")
    if votante == "salir":
        if len(votantes) == 0:
            print("\nPor lo menos uno tiene que votar")
        else:
            print("Pasamos a votar")
            break
    if votante in votantes:
        print("\nEl votante ya fue agregado, ingrese otro")
    else:
        votantes.add(votante)
        print(f"Votante agregado {votantes}")

comidas = list(comidas)

for i in range(len(votantes)):
    print(f"\nVotante {i + 1} elija una opcion: ")
    print("Comidas disponibles: ")
    for indice, comida in enumerate(comidas):
        indice += 1
        print(f"{indice} {comida}")
    while True:
        voto = input("\nIngrese el numero de la comida elegida: ")
        try:
            voto = int(voto)
            if 1 <= voto <= len(comidas):
                comida_elegida = comidas[voto - 1]  # Obtener la comida elegida
                votos_comida[comida_elegida] += 1  # Incrementar el contador de votos
                print("Gracias por votar")
                break
            else:
                print("Opcion no valida, vuelva a elegir")
        except ValueError:
            print("Ingrese un número válido.")

# Mostrar los resultados de la votación
print("\nResultados de la votación:")
for comida, votos in votos_comida.items():
    print(f"{comida}: {votos} votos")