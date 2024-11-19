import random
import numpy as np
import variables as var
from variables import *

# Funcion para la introducción del nombre del usuario.

def continuar_partida():
    preguntar_salir = False
    while not preguntar_salir:

        continuar = input("¿Quieres volver a jugar (S/N)? ").lower().replace(" ","")
        preguntar_salir = continuar in ["s","n"]
        if preguntar_salir:
            return continuar == "s"
        print("No te entiendo!")
    
    return False



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
    #TODO: Verificar que no se puedan meter cualquier otra cosa que no sea una coordenada o "salir". Si es caracter en blanco, se vuelve a pedir
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
            try:
                coordenada = coordenada.split(",") # Separamos el string utilizando la coma y convirtiendo el input en una lista de 2 items
                for i in coordenada:
                    lista_coordenada_int.append(int(i))
                coordenada_array = np.array(lista_coordenada_int)                
                if coordenada_array.max() <= var.TABLERO_LONGITUD and coordenada_array.min() >= 0:
                    no_valido = False
                    return lista_coordenada_int
                else:
                    print("Lo siento, esa coordenada no es válida.")
            except:
                print("La coordenada indicada no es válida")
        

# Para elegir la dificultad vamos a hacer esta funcion:

def dificultad():
    for index, n in enumerate(RANGOS):
        print(f"Dificultad {index +1}: {n}")
    input_valido = False
    while not input_valido:
        eleccion_dificultad = input("Elija la dificultad del 1 al 5: ").replace(" ","") # Le pedimos al sujeto que seleccione la dificultad 
        if eleccion_dificultad not in ["1","2","3","4","5"]:
            input_valido = False
            print("Lo siento, no tenemos un cargo para esa dificultad.")
        else:
            dificultad_seleccionada = RANGOS[int(eleccion_dificultad)-1]    
            print(f"Perfecto, ha elegido la dificultad {eleccion_dificultad}, ¡se enfrentará a un {dificultad_seleccionada}!")
            input_valido = True
            return int(eleccion_dificultad)