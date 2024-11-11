import numpy as np
import pandas as pd


# Funcion para la introducción del nombre del usuario.

def limpieza_nombre_usuario():
    texto = input("Por favor, introduzca el nombre de usuario (máximo 15 caracteres)")
    texto = texto.replace(" ", "") # Primero se limpia el texto del input quitando los espacios
    if len(texto) <= 15: # Debe tener un máximo de 15 caracteres de longitud
        return texto
    else:
        print("Lo siento, el nombre usuario excede el número de caracteres posibles.")



# Vamos a recoger las coordenadas de disparo como si fueran una lista:

def limpieza_coordenada():
    coordenada = input("Por favor, introduzca la coordenada a la que quiere disparar:")
    coordenada = coordenada.replace(" ", "") # Limpiamos todos los espacios del input
    coordenada = coordenada.split(",") # Separamos el string utilizando la coma y convirtiendo el input en una lista de 2 items
    lista_coordenada_int = [] # Creamos una lista vacia en la que meteremos ints en vez de str
    for i in coordenada:
        lista_coordenada_int.append(int(i))
    coordenada_array = np.array(lista_coordenada_int)
    if coordenada_array.max() <= TABLERO_LONGITUD and coordenada_array.min() >= 0:
        return lista_coordenada_int
    else:
        print("Lo siento, esa coordenada no es válida")

# ______________________________________________________________________________________________________

# Para elegir la dificultad vamos a hacer esta funcion:

def eleccion_dificultad():
    dificultad = np.array(["Marinero", "Timonel", "Contramaestre", "Oficial", "Capitán"]) # Le ponemos un nombre a cada dificultad (de más fácil a más difícil)
    eleccion_dificultad = int(input("Elija la dificultad del 1 al 5")) # Le pedimos al sujeto que seleccione la dificultad
    if eleccion_dificultad <= 5 and eleccion_dificultad >= 1: # Corroboramos que está entre 1 y 5
        dificultad_seleccionada = dificultad[eleccion_dificultad-1]
        print(f"Perfecto, ha elegido la dificultad {eleccion_dificultad}, usted es un {dificultad_seleccionada}!")
    else:
        print("Lo siento, no tenemos un cargo para esa dificultad.")


# _______________________________________________________________________________________________________



# _______________________________________________________________________________________________________



# _______________________________________________________________________________________________________



# _______________________________________________________________________________________________________



# _______________________________________________________________________________________________________