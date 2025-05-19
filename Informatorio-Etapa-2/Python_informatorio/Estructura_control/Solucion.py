
# # Resolucion a problmeatica
comidas = set()
votantes = set()
comidas_votadas = {}
indice_comida = 0
print("Bienvenido a la votacion de las comidas") 
while True:
    comida = input("Ingrese la comida que desea pedir, y 'salir' para pasar a registrar los votantes: ")
    if comida.lower() == "salir":
        if len(comidas) == 0:
            print("Por lo menos una comida tiene que ser elegida")
            continue
        else:                                   
            print("\nPasamos a cargar los votantes")
            break
    else:   
        comidas.add(comida)
        print(comidas)
        comidas_votadas[comida] = (indice_comida  + len(comidas))

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

votos_registrados = []
# comidas_votadas= {"pizza":1,"hamburguesa":2,"pasta":3,"ensalada":4,"sushi":5,"tacos":6}
comidas = list(comidas)
for i in range(len(votantes)):
    print(f"\nVotante {i + 1} elija una opcion: ")
    print("Comidas disponibles: ")
    for menu, posicion in comidas_votadas.items():
        print(f"{posicion} - {menu}")
    voto = input("Ingrese el número de la comida que desea votar: ")
    if voto.isdigit():
        voto = int(voto)
        comida_elegida = ""
        for menu, valor in comidas_votadas.items():
            if voto == valor:
                comida_elegida = menu
                
                break

        if comida_elegida:
            print("Voto registrado")                     
            votos_registrados.append(comida_elegida)    
        else:
            print("Opción no válida, por favor elija una opción de la lista")
    else:
        print("Opción no válida, por favor elija una opción de la lista")
            
print("Votos registrados: ", votos_registrados)