from variables import *
from entrada_datos import * 
import numpy as np 
import random

class Barco: 

    def __init__(self, longitud, posicion_x= None, posicion_y = None, orientacion= None):
        self.longitud = longitud  
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.orientacion = orientacion
        self.total_disparos = 0 
        self.disparos_pendientes = longitud
        self.posiciones = []

    def set_posiciones(self, posiciones, orientacion):
        self.posiciones = posiciones
        self.orientacion = orientacion

    def colocar_en_tablero(self, tablero_barcos): #tablero_barcos porque estamos accediendo a la clase tablero
        TABLERO_LONGITUD = len(tablero_barcos)  # Asumimos que el tablero es cuadrado

        colocado = False
        while not colocado:
            direccion = random.choice(['N', 'S', 'E', 'O'])
            if direccion == 'E': 
                fila = random.randint(0, TABLERO_LONGITUD - 1)
                columna = random.randint(0, TABLERO_LONGITUD - self.longitud)
                posiciones = [(fila, columna + i) for i in range(self.longitud)]
            elif direccion == 'O':  
                fila = random.randint(0, TABLERO_LONGITUD - 1)
                columna = random.randint(self.longitud - 1, TABLERO_LONGITUD - 1)
                posiciones = [(fila, columna - i) for i in range(self.longitud)]
            elif direccion == 'S':  
                fila = random.randint(0, TABLERO_LONGITUD - self.longitud)
                columna = random.randint(0, TABLERO_LONGITUD - 1)
                posiciones = [(fila + i, columna) for i in range(self.longitud)]
            elif direccion == 'N':  
                fila = random.randint(self.longitud - 1, TABLERO_LONGITUD - 1)
                columna = random.randint(0, TABLERO_LONGITUD - 1)
                posiciones = [(fila - i, columna) for i in range(self.longitud)]

            # Verificar si las posiciones están libres
            if all(tablero_barcos[f][c] == CARACTER_AGUA for f, c in posiciones):
                for f, c in posiciones:
                    tablero_barcos[f][c] = CARACTER_BARCO
                self.set_posiciones(posiciones, direccion)
                colocado = True

#######################################

class Tablero:    
    def __init__(self,usuario): 
        self.usuario = usuario 
        self.tablero_barcos = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)  # Tablero donde se colocan los barcos
    
    def flota_aleatoria(self, flota, TABLERO_LONGITUD):
        filas = columnas = TABLERO_LONGITUD
        coordenadas = []
        for eslora, unidades in flota.items():
            for i in range(unidades):
                encaje = False
                while not encaje:
                    # Escoge orientación y posición inicial aleatoriamente
                    orientacion = random.choice(["N", "S", "E", "O"])
                    coord_barco = [random.randint(0, filas - 1), random.randint(0, columnas - 1)]
                    n_ref, k_ref = coord_barco
                    print(coord_barco)

                    # Define coord_barco según la orientación
                    if eslora > 1:
                        if orientacion == "N":
                            coord_barco = [(n_ref - i, k_ref) for i in range(eslora)]
                        elif orientacion == "S":
                            coord_barco = [(n_ref + i, k_ref) for i in range(eslora)]
                        elif orientacion == "E":
                            coord_barco = [(n_ref, k_ref + i) for i in range(eslora)]
                        elif orientacion == "O":
                            coord_barco = [(n_ref, k_ref - i) for i in range(eslora)]
                    print(coord_barco)
                    # Verifica si todas las posiciones de coord_barco están dentro del tablero y libres
                    encaje = True  # Asumimos que encajará, pero verificamos
                    for pieza in coord_barco:
                        # Condiciones de borde
                        condicion_n = 0 <= pieza[0] < filas
                        condicion_k = 0 <= pieza[1] < columnas
                        if not (condicion_n and condicion_k):
                            encaje = False  # Si está fuera del tablero, encaje es False
                            break  # Salimos del bucle for, reintentamos otra posición
                        
                        # Solo si estamos seguros de que está dentro, revisamos si está ocupado
                        for lista_barco in coordenadas:
                            for pieza_otro_barco in lista_barco:
                                if pieza_otro_barco == pieza:
                                    encaje = False
                                    break
                coordenadas.append(coord_barco)
                for pieza in coord_barco: 
                    self.tablero_barcos[pieza[0], pieza[1]] = CARACTER_BARCO   
    
    def disparar(self, fila=None, columna=None):
        if fila is None or columna is None:  
            return False

        if self.tablero_barcos[fila, columna] in [CARACTER_DISPARO_OK, CARACTER_DISPARO_NOK]:
            return False

        elif self.tablero_barcos[fila, columna] == CARACTER_BARCO:
            self.tablero_barcos[fila, columna] = CARACTER_DISPARO_OK  # has dado a un barco
            return True 

        else:
            self.tablero_barcos[fila, columna] = CARACTER_DISPARO_NOK  # has dado a agua
            return False

    def is_disparo_ok(self, fila = None, columna = None): 
        if self.tablero_barcos[fila, columna] == CARACTER_BARCO:  # has dado a un barco
            return True 
        
        else: 
            return False 
        
    def comprobar_todos_hundidos(self): 
        if CARACTER_BARCO not in self.tablero_barcos: 
            return True 
        else: 
            return False
    
    def count_celdas_restantes(self): 
        celdas = np.sum(self.tablero_barcos == CARACTER_BARCO) #crea una matriz 0 si False 1 si true y luego suma los valores de la matriz
        return celdas
    
    def count_total_disparos(self): 
        disparos = np.sum((self.tablero_barcos == CARACTER_DISPARO_OK) | (self.tablero_barcos == CARACTER_DISPARO_NOK))
        return disparos
    #mismo mecanismo, crea una matriz y si los valores son o disparo ok o disparo nok = 1 y sino = 0 y los suma 

    def iniciar_tablero(self): 
        self.flota_aleatoria(FLOTA,TABLERO_LONGITUD)
    

