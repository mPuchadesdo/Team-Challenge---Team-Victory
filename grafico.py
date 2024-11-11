import numpy as np
import os
import variables as var
 
#Genereación de datos para pruebbas
tablero = np.full((var.TABLERO_LONGITUD, var.TABLERO_LONGITUD), var.CARACTER_AGUA)

num_max_filas = tablero.shape[0]
num_max_columnas = tablero.shape[1]

tablero[5,4] = var.CARACTER_BARCO
tablero[5,5] = var.CARACTER_DISPARO_OK
tablero[5,6] = var.CARACTER_BARCO
tablero[5,7] = var.CARACTER_BARCO
tablero[5,8] = var.CARACTER_DISPARO_NOK

#Obtener datos de Partida
turno = 1

nombre_jugador_1 = "Jugador 1"
total_disparos_1 = 10
disparos_pendientes_1 = 8
mensaje_turno_1 = f"Coordenada (6,6) -> TOCADO!!!"

nombre_jugador_2 = "Jugador 2"
total_disparos_2 = 5
disparos_pendientes_2 = 13
mensaje_turno_2 = f"Coordenada (6,9) -> Agua"

# FIN Genereación de datos para pruebbas

#FUNCIONES


#Función que devuelve el strinng para un tablero dado. Si oponente=True, no pinta posiciones de barco sin disparar
def get_tablero_string(tablero, oponente = False):
    array_resultado = []

    longitud = var.TABLERO_LONGITUD
    colIncremento = 1
    var_char_separador_columna = "|"
    max_cars = len(str(longitud))

    #Primera celda
    strLinea = " " + (" " * max_cars)

    #Pintamos los nombres de las columnas
    for idxCol in range(0, longitud):
        strLinea += " | " + str(idxCol + colIncremento)
    strLinea += " |"
    array_resultado.append(strLinea)

    caracteres_fila = len(strLinea);
    #strTablero += "-" * (caracteres_fila) + "\n"
    array_resultado.append("-" * (caracteres_fila))
    array_resultado.insert(0, "-" * (caracteres_fila))

    for idxFila in range(0, longitud):
        strLinea = ""
        strIdxFila = str(idxFila + colIncremento)
        strLinea += " "  + (" " * (max_cars - len(strIdxFila))) + strIdxFila
        for idxCol in range(0, longitud):
            strIdxCol = str(idxCol + colIncremento)
            caracter = tablero[idxFila, idxCol]
            if oponente and caracter == var.CARACTER_BARCO:
                caracter = var.CARACTER_AGUA
            strLinea += " | " + (" " * (len(strIdxCol) - len(caracter))) + caracter
        strLinea += " |"
        array_resultado.append(strLinea)

    #strTablero += "-" * (caracteres_fila) + "\n"
    array_resultado.append("-" * (caracteres_fila))

    return array_resultado

#Devuelve tantos espacios en blanco como caracteres falten para de la longittud de la cadena al final
def get_relleno_cadena(total, cadena):
    return (" " * (total - len(cadena)))

#Devuelve una cadena los disparos totales disparos pendientes de un tablero
def get_totales(total_caracteres, total_disparos, disparos_pendientes):
    str_total_disparos = f"Total disparos:{total_disparos: 03d}"
    str_total_disparos = get_relleno_cadena(total_caracteres, str_total_disparos) +  str_total_disparos
    str_disparos_pendientes = f"Disparos pendientes:{disparos_pendientes: 03d}"
    str_disparos_pendientes = get_relleno_cadena(total_caracteres, str_disparos_pendientes) + str_disparos_pendientes

    return str_total_disparos, str_disparos_pendientes

#Función que develve pinta por pantalla la información del juego (turno, nombres), tableros y totales
def pintar_tableros():
    
    os.system('cls')
    #Sustituir por los nombbres de las variables de los tableros de las partidas
    array_tableroJ1 = get_tablero_string(tablero, True)
    array_tableroJ2 = get_tablero_string(tablero)

    len_linea_tablero = len(array_tableroJ1[0])
    separador_tableros = " " * var.NUM_CARACTERES_SEPARACION_TABLEROS

    #Pintar turno
    print(f"TURNO: {turno}")

    #Pintar nombbre de los jugadores
    cabecera = f"J1:{nombre_jugador_1}"
    cabecera += get_relleno_cadena(len_linea_tablero, cabecera) + separador_tableros 
    cabecera += f"J2:{nombre_jugador_2}"
    print(cabecera)

    #Pintar mensaje resultado de los disparos de cada turno
    mensajes_turno = " > " + mensaje_turno_1
    mensajes_turno += get_relleno_cadena(len_linea_tablero, mensajes_turno) + separador_tableros
    mensajes_turno += " > " + mensaje_turno_2
    print(mensajes_turno)

    #Pintar tableros
    for idx, linea in enumerate(array_tableroJ1):
        lineaStr = linea + separador_tableros  + array_tableroJ2[idx]
        print(lineaStr)

    #Pintamos los disparos totales y pendientes
    str_total_1, str_pendientes_1 = get_totales(len_linea_tablero, total_disparos_1, disparos_pendientes_1)
    str_total_2, str_pendientes_2 = get_totales(len_linea_tablero, total_disparos_2, disparos_pendientes_2)

    print(str_total_1 + separador_tableros + str_total_2)
    print(str_pendientes_1 + separador_tableros + str_pendientes_2)

pintar_tableros()