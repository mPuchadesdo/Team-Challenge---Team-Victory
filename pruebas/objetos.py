from variables import *

import numpy as np 
import random

# constantes

# contante con la parametrización del juego. clave: eslora, valor: unidades 
flota = {4: 1, 
         3: 2,
         2: 3,
         1: 4}

# función que cree las coordenadas aleatorias de todos los barcos para la flota especificada. Tendrá en cuenta que no se deben pisar entre ellos

def flota_aleatoria(flota, TABLERO_LONGITUD):
    filas = columnas = TABLERO_LONGITUD
    tablero = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)
    coordenadas = []
    for eslora, unidades in flota.items():
        for i in range(unidades):
            encaje = False
            while not encaje:
                # Escoge orientación y posición inicial aleatoriamente
                orientacion = random.choice(["N", "S", "E", "O"])
                coord_barco = [random.randint(0, filas - 1), random.randint(0, columnas - 1)]
                n_ref, k_ref = coord_barco

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
    return coordenadas             

# recupero ejercicio spr3 ud2
def posicionar_barco_aleatorio(tablero):
    tablero = tablero.copy()
    filas = tablero.shape[0]
    columnas = tablero.shape[1]
    encaje = False

    while not encaje:
        # Escoge orientación y posición inicial aleatoriamente
        orientacion = random.choice(["N", "S", "E", "O"])
        posicion_inicial = (random.randint(0, filas - 1), random.randint(0, columnas - 1))
        n_ref, k_ref = posicion_inicial

        # Define coord_barco según la orientación
        if orientacion == "N":
            coord_barco = [(n_ref - i, k_ref) for i in range(4)]
        elif orientacion == "S":
            coord_barco = [(n_ref + i, k_ref) for i in range(4)]
        elif orientacion == "E":
            coord_barco = [(n_ref, k_ref + i) for i in range(4)]
        elif orientacion == "O":
            coord_barco = [(n_ref, k_ref - i) for i in range(4)]

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
            if tablero[pieza] in ["O", "X"]:
                encaje = False  # Si está ocupado, también es False
                break

    # Colocar el barco en el tablero
    for coordenada in coord_barco:
        tablero[coordenada] = "O"

    return tablero


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

    #def disparar(self): #lo quito porque lo he metido en tablero ya 
        #if self.disparos_pendientes > 0: 
            #self.total_disparos += 1
            #self.disparos_pendientes -= 1 
        #else: 
            #("Tus barcos ya están hundidos")

    def hundido(self, disparos_pendientes): 
        if disparos_pendientes == 0: 
            print("¡Te han hundido el barco!")

class Tablero:    
    def __init__(self,usuario): 
        self.usuario = usuario
    #    self.barcos = barcos   
        self.tablero_barcos = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)  # Tablero donde se colocan los barcos
        self.tablero_disparo = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), " ")
    #    self.barcos_restantes = len(barcos)  # Número total de barcos en el tablero
        self.total_disparos = 0 

    def colocar_barcos(self):
        for barco in self.barcos:
        # cambiar código por uno que ejecute el cambio de coordenadas de agua a "O"
            colocado = False
            while not colocado:
                direccion = random.choice(['N', 'S', 'E', 'O'])
                if direccion == 'E': 
                    fila = random.randint(0, TABLERO_LONGITUD - 1)
                    columna = random.randint(0, TABLERO_LONGITUD - barco.longitud)
                    posiciones = [(fila, columna + i) for i in range(barco.longitud)]
                elif direccion == 'O':  
                    fila = random.randint(0, TABLERO_LONGITUD - 1)
                    columna = random.randint(barco.longitud - 1, TABLERO_LONGITUD - 1)
                    posiciones = [(fila, columna - i) for i in range(barco.longitud)]
                elif direccion == 'S':  
                    fila = random.randint(0, TABLERO_LONGITUD - barco.longitud)
                    columna = random.randint(0, TABLERO_LONGITUD - 1)
                    posiciones = [(fila + i, columna) for i in range(barco.longitud)]
                elif direccion == 'N':  
                    fila = random.randint(barco.longitud - 1, TABLERO_LONGITUD - 1)
                    columna = random.randint(0, TABLERO_LONGITUD - 1)
                    posiciones = [(fila - i, columna) for i in range(barco.longitud)]

                if all(self.tablero_barcos[f][c] == CARACTER_AGUA for f, c in posiciones):
                    for f, c in posiciones:
                        self.tablero_barcos[f][c] = CARACTER_BARCO
                    barco.set_posiciones(posiciones, direccion)
                    colocado = True

    def disparar(self, fila = None, columna = None):
        if fila is None or columna is None:
            while True:
                coordenadas = input("Inserta unas coordenadas (ejemplo: 3,4): ")

                try:
                    # Separar las coordenadas en fila y columna
                    fila, columna = map(int, coordenadas.split(","))

                    # Comprobar que las coordenadas estén dentro del rango del tablero
                    if fila < 0 or fila >= TABLERO_LONGITUD or columna < 0 or columna >= TABLERO_LONGITUD:
                        print(f"Coordenadas fuera del rango del tablero. El tablero es de 0 a {TABLERO_LONGITUD-1}. Intenta nuevamente.")
                    else:
                        break  # Salir del bucle si las coordenadas son válidas
                except ValueError:
                    print("Entrada no válida. Asegúrate de ingresar dos números separados por una coma.")

        if self.tablero_disparo[fila, columna] in [CARACTER_DISPARO_OK, CARACTER_DISPARO_NOK]:
            print("Ya has disparado a esta posición")

        elif self.tablero_barcos[fila, columna] == CARACTER_BARCO:
            self.tablero_disparo[fila, columna] = CARACTER_DISPARO_OK  # has dado a un barco
            self.barcos_restantes -= 1  # Reducimos el número de barcos restantes
            self.total_disparos += 1
            print(f"¡Has dado a un barco!")

        else:
            self.tablero_disparo[fila, columna] = CARACTER_DISPARO_NOK  # has dado a agua
            self.total_disparos += 1
            print(f"Mala suerte...¡Agua!")


    def mostrar_tableros(self):
        print("Tablero de Barcos")
        print(self.tablero_barcos)
        print("Tablero de Disparos")
        print(self.tablero_disparo)
