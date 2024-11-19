import UI as ui
import funciones as fn
import entrada_datos as ed
import tablero as tbl
import variables as var
import numpy as np


class Partida:
    # Dificultad y nombre del jugador como argumentos
    def __init__(self, dificultad, nombre_jugador):
        self.tablero_humano = tbl.Tablero(var.TABLERO_LONGITUD, nombre_jugador) # clase Tablero
        self.tablero_maquina = tbl.Tablero(var.TABLERO_LONGITUD, var.RANGOS[dificultad-1]) # clase Tablero

        self.disparos_maquina = []
        for fila in range(0,var.TABLERO_LONGITUD):
            for columna in range(0,var.TABLERO_LONGITUD):
                self.disparos_maquina.append([fila, columna])


        self.dificultad = dificultad
        self.turno = 1

        self.mensajes_turno_humano = []
        self.mensajes_turno_maquina = []
    

    def iniciar_partida(self):
        # Crea los tableros y coloca barcos
        self.tablero_humano.iniciar_tablero()
        self.tablero_maquina.iniciar_tablero()


        fin_de_partida = False
        ui.pintar_tableros(self)
        while not fin_de_partida:
            self.mensajes_turno_humano = []
            self.mensajes_turno_maquina = []

            # Tirada del humano
            jugador_acierta = True
            while jugador_acierta and not fin_de_partida:
                coordenada = ed.coordenada_disparo()
                if coordenada == True:
                    mensaje = "Has seleccionado salir de la partida"
                    self.mensajes_turno_humano.append(mensaje)
                    fin_de_partida = True
                else:
                    mensaje = f"{coordenada[0]}, {coordenada[1]} " 
                    disparo = self.tablero_maquina.disparar(coordenada[0]-1, coordenada[1]-1)
                    if disparo == 1:
                        mensaje += "¡Acierto! Puedes volver a disparar."
                    elif disparo == 2:
                        mensaje += "Posición ya disparada. Cambio de turno."
                        #TODO: Cuando se dispara a un punto ya disparado, se pone como AGUA
                    else:
                        mensaje += "Agua. Cambio de turno"
                        jugador_acierta = False
                    self.mensajes_turno_humano.append(mensaje)
                    

                    if self.tablero_maquina.comprobar_todos_hundidos():
                        self.mensajes_turno_humano.append("HAS GANADO!!!")
                        fin_de_partida = True
                    ui.pintar_tableros(self)

            # Turno de la máquina
            maquina_acierta = True
            while maquina_acierta and not fin_de_partida:
                coordenada = self.disparo_aleatorio()
                mensaje = f"{coordenada[0]}, {coordenada[1]} "
                disparo = self.tablero_humano.disparar(coordenada[0], coordenada[1])
                if disparo == 1:
                    mensaje += "¡Acierto! Puedes volver a disparar."
                else:
                    mensaje += "Agua. Cambio de turno"
                    maquina_acierta = False
                self.mensajes_turno_maquina.append(mensaje) 

                if self.tablero_humano.comprobar_todos_hundidos():
                        self.mensajes_turno_maquina.append(f"El {var.RANGOS[self.dificultad-1]} ha ganado la partida!!!")
                        fin_de_partida = True

            ui.pintar_tableros(self)
            self.turno += 1        


    # Genera una coordenada aleatoria para el disparo de la máquina sin repetir teniendo en cuenta el nivel de dificultad:
    def disparo_aleatorio(self):
        disparo_correcto = False
        d = 1
        while not disparo_correcto and d <= self.dificultad:
            d += 1
            
            posicion = np.random.randint(0, len(self.disparos_maquina))        

            fila = self.disparos_maquina[posicion][0]
            columna = self.disparos_maquina[posicion][1]
            coordenada = [fila, columna]

            self.disparos_maquina.remove(coordenada)

            if self.tablero_humano.is_disparo_ok(fila, columna):
                disparo_correcto = True
        return coordenada    