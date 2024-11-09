#Clase tablero 
from variables import TABLERO_LONGITUD, CARACTER_AGUA, CARACTER_BARCO, CARACTER_DISPARO_OK, CARACTER_DISPARO_NOK
class Barco: 

    def __init__(self, longitud, posicion_x, posicion_y, orientacion):
        self.longitud = longitud  
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.orientacion = orientacion
        self.total_disparos = 0 
        self.disparos_pendientes = longitud

    def disparos(self): #registra cada vez que disparan y dan al barco
        self.total_disparos += 1
        self.disparos_pendientes -= 1

    def hundido(self, disparos_pendientes): 
        if disparos_pendientes == 0: 
            print("¡Te han hundido el barco!")

#######################################

class Tablero:    
    def __init__(self,usuario,barcos): 
        self.usuario = usuario
        self.barcos = barcos   
        self.tablero_barcos = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)  # Tablero donde se colocan los barcos
        self.tablero_disparo_OK = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)
        self.tablero_disparo_NOK = np.full((TABLERO_LONGITUD, TABLERO_LONGITUD), CARACTER_AGUA)  
        self.barcos_restantes = len(barcos)  # Número total de barcos en el tablero
 

   def disparar(self, fila, columna):
        if self.tablero_barcos[fila, columna] == CARACTER_BARCO:
            self.tablero_disparo_OK[fila, columna] = CARACTER_DISPARO_OK  # has dado a un barco
            self.barcos_restantes -= 1  # Reducimos el número de barcos restantes
            print(f"¡Has dado a un barco!")
        else:
            self.tablero_disparo_NOK[fila, columna] = CARACTER_DISPARO_NOK  # has dado a agua
            print(f"Mala suerte...¡Agua!")