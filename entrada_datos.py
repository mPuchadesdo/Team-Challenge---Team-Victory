import random
import numpy as np
import variables as var
from variables import *

# Función para continuar o no la partida:

def continuar_partida():
    preguntar_salir = False
    while not preguntar_salir:
        continuar = input("¿Quieres volver a jugar (S/N)? ").lower().replace(" ","") # Preguntamos y limpiamos la entrada
        preguntar_salir = continuar in ["s","n"] # Controlamos que la respuesta sea válida
        if preguntar_salir: 
            return continuar == "s" # Si la respuesta ha sido s, devolvemos un True para volver a jugar y si ha sido n, devolvemos un False y finaliza el programa
        print("¡No te entiendo!")
    return False


# Función para la introducción del nombre del usuario:

def nombre_jugador():
    no_valido = True
    while no_valido:
        nombre_jugador = input("Por favor, introduzca el nombre de usuario (máximo 15 caracteres): ")
        if 0 < len(nombre_jugador) <= 15: # # Debe tener un mínimo de 1 caracter de longitud y un máximo de 15
            no_valido = False
            return nombre_jugador
        else:
            print("Lo siento, el nombre usuario no es válido.")


# Vamos a recoger las coordenadas de disparo como si fueran una lista:

def coordenada_disparo():
    no_valido = True
    finalizar_partida = False
    coordenada = ""
    while no_valido:
        coordenada = input("Por favor, introduzca la coordenada a la que quiere disparar (escribe 'salir' para finalizar): ").replace(" ", "") 
        lista_coordenada_int = [] # Creamos una lista vacia en la que meteremos ints en vez de str
        if coordenada == "salir":
            no_valido = False
            finalizar_partida = True
            return finalizar_partida
        else:
            try:
                coordenada = coordenada.split(",") # Separamos el string utilizando la coma y convirtiendo el input en una lista de 2 items
                for i in coordenada:
                    lista_coordenada_int.append(int(i)) # Añadimos en una lista el input pero en forma de int
                coordenada_array = np.array(lista_coordenada_int) # Creamos un array de numpy para utilizar max() y min()             
                if coordenada_array.max() <= var.TABLERO_LONGITUD and coordenada_array.min() >= 0:
                    no_valido = False
                    return lista_coordenada_int
                else:
                    print("Lo siento, esa coordenada no existe en el tablero.")
            except:
                print("La coordenada indicada no es válida.")
        

# Para elegir la dificultad vamos a hacer esta función:

def dificultad():
    for index, n in enumerate(var.RANGOS): # Enseñamos por pantalla las diferentes dificultades y sus rangos
        print(f"Dificultad {index +1}: {n}")
    input_valido = False
    while not input_valido:
        eleccion_dificultad = input("Elija la dificultad del 1 al 5: ").replace(" ","") # Le pedimos al sujeto que seleccione la dificultad 
        try: # Con un try-except nos aseguramos de que, en caso de no introducir un número del 1 al 5, el programa no de error
            dificultad_seleccionada = var.RANGOS[int(eleccion_dificultad)-1] # Seleccionamos el nombre del rango    
            print(f"¡Perfecto, ha elegido la dificultad {eleccion_dificultad}, ¡se enfrentará a un {dificultad_seleccionada}!")
            input_valido = True
            return int(eleccion_dificultad)
        except:
            print("Lo siento, no te entiendo.")