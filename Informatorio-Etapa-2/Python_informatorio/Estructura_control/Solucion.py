
# # # Resolucion a problmeatica
votantes = set()
comidas = set()
cantidad_votantes = 0


print("\nBienvenido a la votacion de las comidas, cuando ya tengamos todas las opciones a votar escriba 'salir'") 
while True:
    comida = input("\nIngrese la comida: ")
    if comida == "salir":
        if len(comidas) == 0:
            print("Por lo menos una comida tiene que ser elegida")
            
        else:                                   
            print("Pasamos a cargar los votantes")
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


# votantes = ["Juan", "Pedro"]
# comidas= ["pancho", "hamburguesa", "pizza", "milanesa"]
comidas = list(comidas)


for i in range(len(votantes)):
        print(f"\nVotante {i+1} elija una opcion: ")
        print("Comidas disponibles: ")
        for indice , comida in enumerate(comidas):
            indice += 1
            print(f"{indice} {comida}")
        while True:
                voto = input("\nIngrese el numero de la comida elegida: ")
                voto = int(voto)
                if voto < 1 or voto > len(comidas):
                    print("Opcion no valida, vuelva a elegir")
                    
                else:
                    print("Gracias por votar")
                    cantidad_votantes += 1
                    break



    
        








    



    


