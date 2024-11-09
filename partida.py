class Partida:
    # Dificultad y nombre del jugador como argumentos
    def __init__(self, dificultad, nombre_jugador):
        self.tablero1 = Tablero(nombre_jugador) # clase Tablero
        self.tablero2 = Tablero("Maquina") # clase Tablero
        self.turno = "Jugador"
        self.dificultad = dificultad
        self.iniciar_partida()

    def iniciar_partida(self):
        # Crea los tableros y coloca barcos
        self.tablero1.iniciar_tablero()
        self.tablero2.iniciar_tablero()

        self.tablero1.colocar_barcos()
        self.tablero2.colocar_barcos()
    
    def los_turnos(self):
        # Tenemos el turno como Jugador entonces
        if self.turno == "Jugador":
            x,y = self.obtener_disparo_jugador()
            disparo_bueno = self.tablero2(x,y)
            if disparo_bueno: # si es True que el disparo da a posciones del tablero enemigo
                print("Has acertado! Vuelves a tirar")
            else:
                print("Mala suerte. Le toca a la Maquina")
                self.turno = "Maquina"