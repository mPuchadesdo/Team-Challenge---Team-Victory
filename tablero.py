import variables as var
import numpy as np 
import random

class Tablero:    
    def __init__(self, longitud, usuario): 
        self.usuario = usuario 
        self.tablero_barcos = np.full((longitud, longitud), var.CARACTER_AGUA)  # Tablero donde se colocan los barcos
    
    def iniciar_tablero(self):
        filas = columnas = len(self.tablero_barcos)
        coordenadas = []
        for eslora, unidades in var.FLOTA.items():
            for i in range(unidades):
                encaje = False
                while not encaje:
                    # Escoge orientación y posición inicial aleatoriamente
                    orientacion = random.choice(["N", "S", "E", "O"])

                    n_ref = random.randint(0, filas - 1)
                    k_ref = random.randint(0, columnas - 1)
                    coord_barco = [(n_ref, k_ref)]

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
                for pieza in coord_barco: 
                    self.tablero_barcos[pieza[0], pieza[1]] = var.CARACTER_BARCO   
    
    def disparar(self, fila=None, columna=None): #función de disparos
        # 0 = Agua,  1 = Disparo correco, 2 = Ya disparado
        if fila is None or columna is None:  
            return 0

        if self.tablero_barcos[fila, columna] in [var.CARACTER_DISPARO_OK, var.CARACTER_DISPARO_NOK]:
            return 2 #disparo en coordenada ya disparada anteriormente

        elif self.tablero_barcos[fila, columna] == var.CARACTER_BARCO:
            self.tablero_barcos[fila, columna] = var.CARACTER_DISPARO_OK  
            return 1 #disparo en coordenada donde hay un barco

        else:
            self.tablero_barcos[fila, columna] = var.CARACTER_DISPARO_NOK 
            return 0 #disparo en coordenada donde hay agua

    def is_disparo_ok(self, fila = None, columna = None): 
        if self.tablero_barcos[fila, columna] == var.CARACTER_BARCO:  
            return True #verifica si el disparo ha dado a un barco o no
        
        else: 
            return False 
        
    def comprobar_todos_hundidos(self): 
        if var.CARACTER_BARCO not in self.tablero_barcos: 
            return True 
        else: 
            return False
    
    def count_celdas_restantes(self): 
        celdas = np.sum(self.tablero_barcos == var.CARACTER_BARCO) 
        return celdas #crea una matriz 0 si False 1 si true y luego suma los valores de la matriz
    
    def count_total_disparos(self): 
        disparos = np.sum(self.tablero_barcos == var.CARACTER_DISPARO_OK)
        return disparos
    #   mismo mecanismo, crea una matriz y si los valores son o disparo ok o disparo nok = 1 y sino = 0 y los suma 

