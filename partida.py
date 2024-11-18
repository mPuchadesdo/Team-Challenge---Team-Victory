from main import *
from grafico import *
import funciones as fn
import entrada_datos as ed
import clases as cl


class Partida:
    # Dificultad y nombre del jugador como argumentos
    def __init__(self, dificultad, nombre_jugador):
        self.tablero_humano = Tablero(nombre_jugador) # clase Tablero
        self.tablero_maquina = Tablero(RANGOS[dificultad-1]) # clase Tablero
        self.dificultad = dificultad
        self.mensajes_turno_humano = []
        self.mensajes_turno_maquina = []
        # self.iniciar_partida()

    def iniciar_partida(self):
        # Crea los tableros y coloca barcos
        self.tablero_humano.cl.iniciar_tablero()
        self.tablero_maquina.cl.iniciar_tablero()
        self.gestion_turnos()

        # self.tablero_humano.colocar_barcos()
        # self.tablero_maquina.colocar_barcos()
    
    # def los_turnos(self):
    #     # Tenemos el turno como Jugador entonces
    #     if self.turno == "Jugador":
    #         x,y = self.obtener_disparo_jugador()
    #         disparo_bueno = self.tablero2(x,y)
    #         if disparo_bueno: # si es True que el disparo da a posciones del tablero enemigo
    #             print("Has acertado! Vuelves a tirar")
    #         else:
    #             print("Mala suerte. Le toca a la Maquina")
    #             self.turno = "Maquina"

    def gestion_turnos(self):
        fin_de_partida = False
        turno = 1
        pintar_tableros()
        while not fin_de_partida:
            self.mensajes_turno_humano = []
            self.mensajes_turno_maquina = []
            print(f"TURNO {turno}")

            # Turno del jugador 1
            jugador_acierta = True
            while jugador_acierta and not fin_de_partida:
                coordenada = ed.coordenada_disparo()
                if coordenada == True:
                    mensaje = "Has seleccionado salir de la partida"
                    self.mensajes_turno_humano.append(mensaje)
                    fin_de_partida = True
                else:
                    mensaje = f"{coordenada[0]}, {coordenada[1]}"
                    if self.tablero_maquina.disparar(coordenada[0], coordenada[1]):
                        mensaje += "¡Acierto! Puedes volver a disparar."
                    else:
                        mensaje += "Agua. Turno de la máquina."
                    self.mensajes_turno_humano.append(mensaje)

                    if self.tablero_maquina.comprobar_todos_hundidos():
                        self.mensajes_turno_humano.append("HAS GANADO!!!")
                        fin_de_partida = True

            # Turno de la máquina
            maquina_acierta = True
            while maquina_acierta and not fin_de_partida:
                coordenada = ed.disparo_aleatorio(self.dificultad, self.tablero_humano)
                mensaje = f"{coordenada[0]}, {coordenada[1]}"
                if self.tablero_humano.disparar(coordenada[0], coordenada[1]):
                    mensaje += "¡Acierto! Puedes volver a disparar."
                else:
                    mensaje += "Agua. Turno de la máquina."
                self.mensajes_turno_maquina.append(mensaje) 

                if self.tablero_humano.comprobar_todos_hundidos():
                        self.mensajes_turno_maquina.append(f"El {RANGOS[self.dificultad-1]} ha ganado la partida!!!")
                        fin_de_partida = True
## salir del bucle, o el usuario pone salir o hubo un ganador

            # # Mostrar el estado actual de los tableros
            # print("\nEstado actual del juego:")
            # print("Tablero del jugador:")
            # tableros_jugador.mostrar_tableros()
            # print("\nTablero de la máquina (sin mostrar barcos):")
            # tableros_maquina.mostrar_tableros()
            pintar_tableros()
        
            turno += 1        