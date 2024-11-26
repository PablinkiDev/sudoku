import random
import pygame
import json
from constantes import *
from logica_sudoku import *

def validar_colisiones_menu(evento, opciones, estado):
    """
    Esta funcion se encarga de validar las colisiones de los botonees del menu. Cuando se pulse un boton cambia el estado del juego.
    Recibe: evento(dict): Diccionario de eventos del juego.
            opciones(list[dict]): Opciones para cada boton.
            estado(str): Estado del juego
    Retorna: estado(str): Estado del juego
    """
    x, y = evento.pos
    for opcion in opciones:
        texto_rect = pygame.Rect(opcion["posicion"][0], opcion["posicion"][1], ANCHO_BOTON, ALTO_BOTON)
        if texto_rect.collidepoint(x, y):
            if opcion["texto"] == "Jugar":
                estado = "jugar"
            elif opcion["texto"] == "Puntajes":
                estado = "puntajes"
            elif opcion["texto"] == "Configuracion":
                estado = "configuracion"
            elif opcion["texto"] == "Salir":
                pygame.quit()
                quit()
    return estado

def validar_colisiones_configuraciones(evento, opciones, estado_juego):
    x, y = evento.pos
    for opcion in opciones:
        texto_rect = pygame.Rect(opcion["posicion"][0], opcion["posicion"][1], ANCHO_BOTON, ALTO_BOTON)
        if texto_rect.collidepoint(x, y):
            if opcion['btn'] == 1: 
                if estado_juego['dificultad'] == 'facil':
                    estado_juego['dificultad'] = "intermedio"
                    opcion["texto"] = f"Dificultad {DIFICULTADES[1]}"
                elif estado_juego['dificultad'] == 'intermedio':
                    estado_juego['dificultad'] = 'dificil'
                    opcion["texto"] = f"Dificultad {DIFICULTADES[2]}"
                elif estado_juego['dificultad'] == 'dificil':
                    opcion["texto"] = f"Dificultad {DIFICULTADES[0]}"
                    estado_juego['dificultad'] = 'facil'

def calcular_tiempo_jugado(segundos, minutos):
    """
    Esta funcion se encarga de calcular el tiempo que lleva transcurrido el juego.
    Recibe segundos y minutos inicializados en 0.
    Retorna: Una tupla.
    La tupla contiene: cadena(str): Cadena formateada en minutos y segundos.
                       segundos(int): Segundos actual
                       minutos(int): Minutos actual
    """
    segundos += 1
    if segundos >= 60:
        minutos += 1
        segundos = 0
    if minutos < 10:
        cadena_minutos = "0" + str(minutos)
    else:
        cadena_minutos = str(minutos)
    if segundos < 10:
        cadena_segundos = "0" + str(segundos)
    else:
        cadena_segundos = str(segundos)
    cadena = cadena_minutos + ":" + cadena_segundos
    return [cadena, segundos, minutos]
    
def detectar_click(estado_juego, evento):
    """
    Detecta el clic del usuario y actualiza la celda seleccionada en el estado del juego.
    """
    cell_size = 60
    tablero_x = 400
    tablero_y = 100

    if evento.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = evento.pos

        # Verificar si el clic está dentro del tablero
        if tablero_x <= mouse_x <= tablero_x + 9 * cell_size and tablero_y <= mouse_y <= tablero_y + 9 * cell_size:
            # Calcular las coordenadas de la celda
            columna = (mouse_x - tablero_x) // cell_size
            fila = (mouse_y - tablero_y) // cell_size
            estado_juego['celda_seleccionada'] = (fila, columna)
        else:
            # Si el clic está fuera del tablero, deseleccionar
            estado_juego['celda_seleccionada'] = None
            
def ingresar_numero(estado_juego, evento):
    """
    Permite al usuario ingresar un número en la celda seleccionada.
    """
    if estado_juego['celda_seleccionada'] is not None:
        fila, columna = estado_juego['celda_seleccionada']
        
        # Verificar si el evento corresponde a un número del 1 al 9
        if (fila, columna) not in estado_juego['celdas_bloqueadas']:
            if evento.unicode.isdigit() and 1 <= int(evento.unicode) <= 9:
                numero_ingresado = int(evento.unicode)
                
                # Validar el número ingresado
                if numero_ingresado == estado_juego['solucion'][fila][columna]:
                    estado_juego['sudoku'][fila][columna] = numero_ingresado
                    estado_juego['colores_celdas'][(fila, columna)] = COLOR_CORRECTO
                    estado_juego['puntaje'] += BONIFICACION_POR_ACIERTO
                    estado_juego['celdas_bloqueadas'].append((fila, columna))
                else:
                    estado_juego['sudoku'][fila][columna] = numero_ingresado
                    estado_juego['colores_celdas'][(fila, columna)] = COLOR_ERROR
                    estado_juego['errores'] += 1
                    estado_juego['puntaje'] -= PENALIZACION_POR_ERRORES
            elif evento.key == pygame.K_BACKSPACE:
                estado_juego['sudoku'][fila][columna] = " "  # Borrar el contenido de la celda

def inicializar_celdas_bloqueadas(tablero):
    """
    Detecta las celdas que tienen valores prellenados (no vacías) y las marca como bloqueadas.
    """
    celdas_bloqueadas = []
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] != " ":  # Si la celda tiene un valor, está bloqueada
                celdas_bloqueadas.append((fila, columna))
    return celdas_bloqueadas

def mostrar_mensaje(mensaje, pantalla, coordenadas, color, fuente_size):
    """
    Muestra un mensaje en pantalla.
    """
    fuente = pygame.font.Font(None, fuente_size)
    texto = fuente.render(mensaje, True, color) 
    texto_rect = texto.get_rect(center=coordenadas)
    pantalla.blit(texto, texto_rect)

def poner_musica(ruta, volumen, loops):
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(loops)
    
def validar_musica(musica_actual, musica_a_validar):
    if musica_actual != musica_a_validar:
            if musica_actual:
                musica_actual.stop()
            musica_a_validar.play(-1)
            musica_actual = musica_a_validar
    return musica_actual

def calcular_dificultad(estado_juego):
    if estado_juego['dificultad'] == "facil":
        dificultad = BONIFICACION_DIFICULTAD_FACIL
    elif estado_juego['dificultad'] == "intermedio":
        dificultad = BONIFICACION_DIFICULTAD_MEDIA
    elif estado_juego['dificultad'] == "dificil":
        dificultad = BONIFICACION_DIFICULTAD_DIFICIL
        
    return estado_juego['puntaje'] * dificultad




def ordenar_ranking(lista_ranking):
    for i in range(len(lista_ranking) - 1):
        for j in range(i + 1, len(lista_ranking)):
            if lista_ranking[i]['points'] < lista_ranking[j]['points']:
                aux = lista_ranking[j]['points']
                lista_ranking[j]['points'] = lista_ranking[i]['points']
                lista_ranking[i]['points'] = aux

def leer_json(ruta):
    with open(ruta, "r") as archivo:
        data = json.load(archivo)
    return data



def escribir_json(ruta, estado_juego):
    data = {
        "user": estado_juego['user'],
        "points": estado_juego['puntaje'],
        "minutos": estado_juego['minutos'],
        "errores": estado_juego['errores']
    }
    
    estado_juego['ranking'].append(data)
    
    with open(ruta, "w") as archivo:
        json.dump(estado_juego['ranking'], archivo, indent=4)
        
        
def resetear_juego(estado_juego):
    estado_juego['tablero_armado'] = False
    estado_juego['puntaje'] = PUNTAJE_BASE
    estado_juego['dificultad_calculada'] = False
    estado_juego['puntos_calculados'] = False
    estado_juego['colores_celdas'] = {}
    estado_juego['errores'] = 0
    estado_juego['tiempo'], estado_juego['segundos'], estado_juego['minutos'] = "", 0, 0
    estado_juego['celdas_bloqueadas'] = inicializar_celdas_bloqueadas(estado_juego['sudoku'])