import entrada_datos as ed
import partida as p
import os

os.system('cls')

print("""
Bienvenid@

Dispara a tu contrincante para hundir sus barcos. 
En cada turno, introduce las coordenadas de tu disparo.
Gana el primero en hundir todos los barcos rivales.
      
Escribe 'salir' en cualquier momento para finalizar la partida.
""")

# Pedimos el nombre del jugador y la dificultad
nombre = ed.nombre_jugador()

fin_partida = False

while not fin_partida:
    dificultad = ed.dificultad()

    # Creación de la partida
    partida = p.Partida(dificultad, nombre)

    # Comenzamos la partida
    partida.iniciar_partida()

    fin_partida = not ed.continuar_partida()

# Fin de la partida