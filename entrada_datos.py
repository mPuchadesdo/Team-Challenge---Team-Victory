import numpy as np
import pandas as pd
import variables as var

# Funcion para la introducción del nombre del usuario.

def limpieza_nombre_usuario():
    no_valido = True
    texto = ""
    while no_valido:
        texto = input("Por favor, introduzca el nombre de usuario (máximo 15 caracteres)")
        if len(texto) <= 15: # Debe tener un máximo de 15 caracteres de longitud
            no_valido = False
            return texto
        else:
            print("Lo siento, el nombre usuario excede el número de caracteres posibles.")



# Vamos a recoger las coordenadas de disparo como si fueran una lista:

def limpieza_coordenada():
    no_valido = True
    finalizar_partida = False
    coordenada = ""
    while no_valido:
        coordenada = input("Por favor, introduzca la coordenada a la que quiere disparar:")
        coordenada = coordenada.replace(" ", "") # Limpiamos todos los espacios del input
        lista_coordenada_int = [] # Creamos una lista vacia en la que meteremos ints en vez de str
        if coordenada == "salir":
            no_valido = False
            finalizar_partida = True
            return finalizar_partida
        else:
            coordenada = coordenada.split(",") # Separamos el string utilizando la coma y convirtiendo el input en una lista de 2 items
            for i in coordenada:
                lista_coordenada_int.append(int(i))
            coordenada_array = np.array(lista_coordenada_int)
            if coordenada_array.max() <= var.TABLERO_LONGITUD and coordenada_array.min() >= 0:
                no_valido = False
                return lista_coordenada_int
            else:
                print("Lo siento, esa coordenada no es válida")
        

# ______________________________________________________________________________________________________

# Para elegir la dificultad vamos a hacer esta funcion:

def eleccion_dificultad():
    dificultad = np.array(["Marinero", "Timonel", "Contramaestre", "Oficial", "Capitán"]) # Le ponemos un nombre a cada dificultad (de más fácil a más difícil)
    print("Dificultad 1: Marinero \nDificultad 2: Timonel \nDificultad 3: Contramaestre \nDificultad 4: Oficial \nDificultad 5: Capitán")
    no_valido = True
    while no_valido:
        eleccion_dificultad = int(input("Elija la dificultad del 1 al 5")) # Le pedimos al sujeto que seleccione la dificultad
        if eleccion_dificultad <= 5 and eleccion_dificultad >= 1: # Corroboramos que está entre 1 y 5
            dificultad_seleccionada = dificultad[eleccion_dificultad-1]
            print(f"Perfecto, ha elegido la dificultad {eleccion_dificultad}, se enfrentará a un {dificultad_seleccionada}!")
            no_valido = False
        else:
            print("Lo siento, no tenemos un cargo para esa dificultad.")


# _______________________________________________________________________________________________________

