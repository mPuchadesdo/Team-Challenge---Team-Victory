from clases import *
from entrada_datos import *
from pruebas.objetos import *


print("""
Bienvenid@

Dispara tu contrincante para hundir sus barcos. 
En cada turno, introduce las coordenadas de tu disparo.
Gana el primero en hundir todos los barcos rivales.
""")
      
nombre = nombre_jugador()

# input(f"{nombre}, elige tu nivel de dificultad del 1 al 5:")


# Inicializamos los 10 barcos aleatorios
barcos_jugador = flota_aleatoria(flota, TABLERO_LONGITUD)
barcos_maquina = flota_aleatoria(flota, TABLERO_LONGITUD)

# Inicializamos los tres tableros
tableros_jugador = Tablero(nombre)
tableros_maquina = Tablero("Máquina")
# tablero_batalla = Tablero("Batalla_jugador") -> este no haría falta porque el tablero de batalla es un atributo de la clase Tablero de cada jugador: tableros_jugador.campo_batalla

# colocamos a ambos jugadores sus respectivos barcos
Tablero.colocar_barcos(barcos_jugador)
Tablero.colocar_barcos(barcos_maquina)

# Comenzamos la partida

hay_barcos_a_flote = True # lo cambiará el control de hundidos
while hay_barcos_a_flote:
    # comenzamos cada turno mostrando los tableros del jugador
    tableros_jugador.mostrar_tableros()

    # Disparo del jugador
    
    nuevo_disparo = True
    while nuevo_disparo:
        disparo = coordenada_disparo() # preguntamos la coordenada y la guardamos en una variable
        if disparo == True: # porque coordenada_disparo() devuelve finalizar_partida = True en caso de que quiera salir
            print(f"Has finalizado la partida.")
            break # OJO: por qué pedirlo en la coordenada, por qué no se lo preguntamos cuando ya ha hecho el primer tiro | Ahora mismo esto está incompleto, resolver cuestión y continuar más abajo

        # ¿Hemos acertado? Evaluamos y devolvemos True para seguir pidiendo disparos si es así
        nuevo_disparo = tableros_jugador.disparar(disparo, tableros_maquina) # Devuelve True si al evaluar el disparo este ha dado a un barco. También imprimirá por pantalla lo que ha pasado
        
        # ¿Se han hundido ya todos los barcos del rival?
        hundidos = tableros_maquina.control_de_hundidos() # Devuelve True si ya no quedan piezas de barco sin disparar, False en caso contrario
        if hundidos == True:
            print(f"Enhorabuena, {nombre}. Ganaste la partida!")
            break # aunque tuviera otra oportunidad de disparo, queremos salir del bucle
    
    if hundidos == True:
        hay_barcos_a_flote = False
        break

    # Disparo de la máquina

    nuevo_disparo = True
    while nuevo_disparo:
        disparo = coordenada_aleatoria()
        # ¿Ha acertado? Evaluamos y devolvemos True para seguir generando disparos si es así
        nuevo_disparo = tableros_maquina.disparar(disparo, tableros_jugador)

        # ¿Se han hundido ya todos los barcos del rival?
        hundidos = tableros_jugador.control_de_hundidos() # Devuelve True si ya no quedan piezas de barco sin disparar, False en caso contrario
        if hundidos == True:
            print("GAME OVER")
            break # aunque tuviera otra oportunidad de disparo, queremos salir del bucle
    
    if hundidos == True:
        hay_barcos_a_flote = False

# mostraremos los tableros de barcos de los dos jugadores para ver cómo han quedado
tableros_jugador.mostrar_tableros(campo_batalla=False)
tableros_maquina.mostrar_tableros(campo_batalla=False)

# ¿Quieres terminar de jugar? opción de meter todo en un while que continúe inicializando tableros y barcos para empezar de cero o que con un "NO" lo asigne a False
print("¿Quieres volver a jugar?")