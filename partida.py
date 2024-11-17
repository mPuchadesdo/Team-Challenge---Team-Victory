from clases import *
from pruebas.objetos import *
from main import *
import funciones as fn
import entrada_datos as ed



class Partida:
    # Dificultad y nombre del jugador como argumentos
    def __init__(self, dificultad, nombre_jugador):
        self.tablero1 = Tablero(nombre_jugador) # clase Tablero
        self.tablero2 = Tablero("Maquina") # clase Tablero
        self.turno = "Jugador"
        self.dificultad = dificultad
        # self.iniciar_partida()

    def iniciar_partida(self):
        # Crea los tableros y coloca barcos
        self.tablero1.iniciar_tablero()
        self.tablero2.iniciar_tablero()

        self.tablero1.colocar_barcos()
        self.tablero2.colocar_barcos()
    
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

    def gestion_turnos():
        turno = 1
        while True:
            print(f"TURNO {turno}")

            # Turno del jugador 1
            jugador_acierta = True
            while jugador_acierta:
                x,y = ed.coordenada_disparo()
                if tableros_maquina.disparar(x, y):
                    print("¡Acierto! Puedes volver a disparar.")
                if tableros_maquina.comprobar_todos_hundidos():
                    print("HAS GANADO!!!")
                    return
                else:
                    print(f"Agua. Turno de la máquina")
                    jugador_acierta = False

            # Turno de la máquina
            maquina_acierta = True
            while maquina_acierta:
                mx, my = fn.coordenadas_aleatorias() # mx my maquinas coordenadas
                if tableros_jugador.disparar(mx, my):
                    print("La máquina acertó. Vuelve a disparar.")
                if tableros_jugador.comprobar_todos_hundidos():
                    print("Has perdido. Fin del juego.")
                    return
                else:
                    print("La máquina falló. Tu turno.")
                    maquina_acierta = False
## salir del bucle, o el usuario pone salir o hubo un ganador

            # Mostrar el estado actual de los tableros
            print("\nEstado actual del juego:")
            print("Tablero del jugador:")
            tableros_jugador.mostrar_tableros()
            print("\nTablero de la máquina (sin mostrar barcos):")
            tableros_maquina.mostrar_tableros()
        
            turno += 1        