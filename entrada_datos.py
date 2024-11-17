import random
import numpy as np
from variables import *
from clases import *

# Funcion para la introducción del nombre del usuario.

def nombre_jugador():
    no_valido = True
    nombre_jugador = ""
    while no_valido:
        nombre_jugador = input("Por favor, introduzca el nombre de usuario (máximo 15 caracteres): ")
        if len(nombre_jugador) <= 15: # Debe tener un máximo de 15 caracteres de longitud
            no_valido = False
            return nombre_jugador
        else:
            print("Lo siento, el nombre usuario excede el número de caracteres posibles.")


# Vamos a recoger las coordenadas de disparo como si fueran una lista:

def coordenada_disparo():
    no_valido = True
    finalizar_partida = False
    coordenada = ""
    while no_valido:
        coordenada = input("Por favor, introduzca la coordenada a la que quiere disparar: ")
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
            if coordenada_array.max() <= TABLERO_LONGITUD and coordenada_array.min() >= 0:
                no_valido = False
                return lista_coordenada_int
            else:
                print("Lo siento, esa coordenada no es válida.")
        

# Para elegir la dificultad vamos a hacer esta funcion:

def dificultad():
    for index, n in enumerate(RANGOS):
        print(f"Dificultad {index +1}: {n}")
    no_valido = True
    while no_valido:
        eleccion_dificultad = int(input("Elija la dificultad del 1 al 5: ")) # Le pedimos al sujeto que seleccione la dificultad
        if eleccion_dificultad <= 5 and eleccion_dificultad >= 1: # Comprobamos que está entre 1 y 5
            dificultad_seleccionada = RANGOS[eleccion_dificultad-1]
            print(f"Perfecto, ha elegido la dificultad {eleccion_dificultad}, ¡se enfrentará a un {dificultad_seleccionada}!")
            no_valido = False
            return eleccion_dificultad
        else:
            print("Lo siento, no tenemos un cargo para esa dificultad.")


# Genera una coordenada aleatoria para el disparo de la máquina sin repetir teniendo en cuenta el nivel de dificultad:

def disparo_aleatorio(dificultad, tablero):
    disparo_correcto = False
    d = 1
    while not disparo_correcto and d <= dificultad:
        coordenada_correcta = False
        d += 1
        while not coordenada_correcta:
            coordenada = np.random.randint(0, (TABLERO_LONGITUD-1), size = 2)
            if not any(np.array_equal(coordenada, v) for v in COORDENADAS_MAQUINA_LIST):
                COORDENADAS_MAQUINA_LIST.append(coordenada)
                coordenada_correcta = True 
        if tablero.es_disparo_ok(coordenada[0], coordenada[1]):
            disparo_correcto = True
    return coordenada    



