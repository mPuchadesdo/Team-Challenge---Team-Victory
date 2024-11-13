from variables import TABLERO_LONGITUD, CARACTER_AGUA, CARACTER_BARCO, CARACTER_DISPARO_OK, CARACTER_DISPARO_NOK

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

    #def disparar(self): #lo quito porque lo he metido en tablero ya 
        #if self.disparos_pendientes > 0: 
            #self.total_disparos += 1
            #self.disparos_pendientes -= 1 
        #else: 
            #("Tus barcos ya están hundidos")

    def hundido(self, disparos_pendientes): 
        if disparos_pendientes == 0: 
            print("¡Te han hundido el barco!")

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

# Colocar los barcos aleatoriamente en el tablero
tablero.colocar_barcos()

# Mostrar el estado de los tableros
tablero.mostrar_tableros()

# Realizar algunos disparos
print("\nDisparando a la posición...")
tablero.disparar()

print("\nDisparando a la posición ...")
tablero.disparar()

print("\nDisparando a la posición...")
tablero.disparar()

# Mostrar el estado de los tableros después de los disparos
tablero.mostrar_tableros()
