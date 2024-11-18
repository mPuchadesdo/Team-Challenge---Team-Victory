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
    def __init__(self,usuario,barcos): 
        self.usuario = usuario
        self.barcos = barcos   
        self.tablero_barcos = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)  # Tablero donde se colocan los barcos
        self.tablero_disparo = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), " ")
        self.barcos_restantes = len(barcos)  # Número total de barcos en el tablero
        self.total_disparos = 0 
        
    def colocar_barcos(self):
        for barco in self.barcos:
            barco.colocar_en_tablero(self.tablero_barcos)

    
    def disparar(self, fila=None, columna=None):
        if fila is None or columna is None:  
            resultado = coordenada_disparo() #TODO: AQUI METO LA FUNCION DE MARIANO
            fila, columna = resultado  # coordenadas

        # TODO: tengo que quitar lo de debajo porque esta en is disparo ok? 
        if self.tablero_disparo[fila, columna] in [CARACTER_DISPARO_OK, CARACTER_DISPARO_NOK]:
            return False

        elif self.tablero_barcos[fila, columna] == CARACTER_BARCO:
            self.tablero_disparo[fila, columna] = CARACTER_DISPARO_OK  # has dado a un barco
            self.barcos_restantes -= 1  # Reducimos el número de barcos restantes
            self.total_disparos += 1
            return True 

        else:
            self.tablero_disparo[fila, columna] = CARACTER_DISPARO_NOK  # has dado a agua
            self.total_disparos += 1
            return False

    def is_disparo_ok(self, fila = None, columna = None): 
        if self.tablero_disparo[fila, columna] in [CARACTER_DISPARO_OK, CARACTER_DISPARO_NOK]:
            return False

        elif self.tablero_barcos[fila, columna] == CARACTER_BARCO:
            self.tablero_disparo[fila, columna] = CARACTER_DISPARO_OK  # has dado a un barco
            self.barcos_restantes -= 1  # Reducimos el número de barcos restantes
            self.total_disparos += 1
            return True 
        else:
            self.tablero_disparo[fila, columna] = CARACTER_DISPARO_NOK  # has dado a agua
            self.total_disparos += 1
            return False

    def comprobar_todos_hundidos(self, barcos_restantes): 
        if barcos_restantes == 0: 
            return True 
        else: 
            return False

    def iniciar_tablero(self): 
        self.tablero_barcos = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)
        self.tablero_disparo = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), " ")
        self.colocar_barcos()

############CODIGO DE PRUEBA 

from variables import TABLERO_LONGITUD, CARACTER_AGUA, CARACTER_BARCO, CARACTER_DISPARO_OK, CARACTER_DISPARO_NOK
import random
import numpy as np

#TABLERO_LONGITUD = 10  
#CARACTER_AGUA = '~'
#CARACTER_BARCO = 'X'
#CARACTER_DISPARO_OK = '*'
#CARACTER_DISPARO_NOK = '-'

# Crear algunos barcos (por ejemplo, uno de tamaño 3 y otro de tamaño 4)
barco1 = Barco(longitud=1)
barco2 = Barco(longitud=1)
barco3 = Barco(longitud=1)
barco4 = Barco(longitud=1)

barco5 = Barco(longitud=2)
barco6= Barco(longitud=2)
barco7= Barco(longitud=2)

barco8= Barco(longitud=3)
barco9 = Barco(longitud=3)

barco10 = Barco(longitud=4)

# Crear un tablero para un usuario
tablero = Tablero(usuario="Jugador 1", barcos=[barco1, barco2, barco3, barco4, barco5, barco6, barco7, barco8, barco9, barco10])

tablero.iniciar_tablero ()


# Colocar los barcos aleatoriamente en el tablero
#tablero.colocar_barcos()

# Mostrar el estado de los tableros
#tablero.mostrar_tableros()

# Realizar algunos disparos
print("\nDisparando a la posición...")
tablero.disparar()

print("\nDisparando a la posición ...")
tablero.disparar()

print("\nDisparando a la posición...")
tablero.disparar()

# Mostrar el estado de los tableros después de los disparos
tablero.mostrar_tableros()
