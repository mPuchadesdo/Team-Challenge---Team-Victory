import numpy as np
import os
import partida as part
import variables as var
 

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
def pintar_tableros(partida):
    
    os.system('cls')
    #Sustituir por los nombbres de las variables de los tableros de las partidas
    array_tableroJ1 = get_tablero_string(partida.tablero_humano.tablero_barcos)
    #array_tableroJ2 = get_tablero_string(partida.tablero_maquina.tablero_barcos, True)
    array_tableroJ2 = get_tablero_string(partida.tablero_maquina.tablero_barcos)
    len_linea_tablero = len(array_tableroJ1[0])
    separador_tableros = " " * var.NUM_CARACTERES_SEPARACION_TABLEROS

    #Pintar turno
    print(f"TURNO: {partida.turno}")

    #Pintar nombbre de los jugadores
    cabecera = f"J1:{partida.tablero_humano.usuario}"
    cabecera += get_relleno_cadena(len_linea_tablero, cabecera) + separador_tableros 
    cabecera += f"J2:{partida.tablero_maquina.usuario}"
    print(cabecera)

    #Pintar tableros
    for idx, linea in enumerate(array_tableroJ1):
        lineaStr = linea + separador_tableros  + array_tableroJ2[idx]
        print(lineaStr)

    #Pintamos los disparos totales y pendientes
    total_disparos_humano = partida.tablero_maquina.self.count_total_disparos()
    disparos_pendientes_humano = partida.tablero_maquina.self.count_celdas_restantes()
    total_disparos_maquina = partida.tablero_humano.self.count_total_disparos()
    disparos_pendientes_maquina = partida.tablero_humano.self.count_celdas_restantes()

    str_total_1, str_pendientes_1 = get_totales(len_linea_tablero, total_disparos_humano, disparos_pendientes_humano)
    str_total_2, str_pendientes_2 = get_totales(len_linea_tablero, total_disparos_maquina, disparos_pendientes_maquina)

    print(str_total_1 + separador_tableros + str_total_2)
    print(str_pendientes_1 + separador_tableros + str_pendientes_2)

    #Pintar mensaje resultado de los disparos de cada turno
    mensajes = [len(partida.mensajes_turno_humano), len(partida.mensajes_turno_maquina)]

    print()
    mensaje = f"--- J1 DISPAROS TURNO {partida.turno} ---"
    mensaje += get_relleno_cadena(len_linea_tablero, mensaje) + separador_tableros
    mensaje += f"--- J2 DISPAROS TURNO {partida.turno} ---"
    print(mensaje)

    for idx in range(0, max(mensajes)):
        mensaje = ""
        if idx < len(partida.mensajes_turno_humano):
            mensaje = " >" + partida.mensajes_turno_humano[idx]
        if idx < len(partida.mensajes_turno_maquina):
            mensaje += get_relleno_cadena(len_linea_tablero, mensaje) + separador_tableros + " >" + partida.mensajes_turno_maquina[idx]
        print(mensaje)
    print()
