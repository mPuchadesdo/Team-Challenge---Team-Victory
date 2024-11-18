import UI as ui
import funciones as fn
import entrada_datos as ed
import clases as cl
import variables as var


class Partida:
    # Dificultad y nombre del jugador como argumentos
    def __init__(self, dificultad, nombre_jugador):
        self.tablero_humano = cl.Tablero(nombre_jugador) # clase Tablero
        self.tablero_maquina = cl.Tablero(var.RANGOS[dificultad-1]) # clase Tablero
        self.dificultad = dificultad
        self.mensajes_turno_humano = []
        self.mensajes_turno_maquina = []
        self.turno = 1
    

    def iniciar_partida(self):
        # Crea los tableros y coloca barcos
        self.tablero_humano.iniciar_tablero()
        self.tablero_maquina.iniciar_tablero()
        self.gestion_turnos()

    def gestion_turnos(self):
        fin_de_partida = False
        ui.pintar_tableros(self)
        while not fin_de_partida:
            self.mensajes_turno_humano = []
            self.mensajes_turno_maquina = []
            print(f"TURNO {self.turno}")

            # Turno del jugador 1
            jugador_acierta = True
            while jugador_acierta and not fin_de_partida:
                coordenada = ed.coordenada_disparo()
                print(coordenada)
                if coordenada == True:
                    mensaje = "Has seleccionado salir de la partida"
                    self.mensajes_turno_humano.append(mensaje)
                    fin_de_partida = True
                else:
                    mensaje = f"{coordenada[0]}, {coordenada[1]} " 
                    if self.tablero_maquina.disparar(coordenada[0]-1, coordenada[1]-1):
                        mensaje += "¡Acierto! Puedes volver a disparar."
                    else:
                        mensaje += "Agua.Cambio de turno"
                        jugador_acierta = False
                    self.mensajes_turno_humano.append(mensaje)
                    

                    if self.tablero_maquina.comprobar_todos_hundidos():
                        self.mensajes_turno_humano.append("HAS GANADO!!!")
                        fin_de_partida = True
                    ui.pintar_tableros(self)
            # Turno de la máquina
            maquina_acierta = True
            while maquina_acierta and not fin_de_partida:
                coordenada = ed.disparo_aleatorio(self.dificultad, self.tablero_humano)
                print(coordenada)
                mensaje = f"{coordenada[0]}, {coordenada[1]} "
                if self.tablero_humano.disparar(coordenada[0], coordenada[1]):
                    mensaje += "¡Acierto! Puedes volver a disparar."
                else:
                    mensaje += "Agua.Cambio de turno"
                    maquina_acierta = False
                self.mensajes_turno_maquina.append(mensaje) 

                if self.tablero_humano.comprobar_todos_hundidos():
                        self.mensajes_turno_maquina.append(f"El {var.RANGOS[self.dificultad-1]} ha ganado la partida!!!")
                        fin_de_partida = True
               
## salir del bucle, o el usuario pone salir o hubo un ganador

            ui.pintar_tableros(self)
        
            self.turno += 1        