
# # Resolucion a problmeatica
votantes = set()
comidas = set()
print("Bienvenido a la votacion de las comidas, cuando ya tengamos todas las opciones a votar escriba 'salir'") 
while True:
    comida = input("Ingrese la comida: ")
    if comida == "salir":
        if len(comidas) == 0:
            print("Por lo menos una comida tiene que ser elegida")
            continue
        else:                                   
            print("\nPasamos a cargar los votantes")
            break
    else:   
        comidas.add(comida)
        print(comidas)

while True:        
    votante = input("Ingrese el nombre del votante, y 'salir' para terminar: ")
    if votante == "salir":
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


comidas = list(comidas)


    



    


