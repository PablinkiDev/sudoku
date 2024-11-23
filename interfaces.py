import pygame
from constantes import *
from imagenes import cargar_imagen, DICCIONARIO_IMAGENES
from logica_sudoku import inicializar_tablero_sudoku
from funciones import detectar_click

def dibujar_input(estado_juego):
    input_rect = pygame.Rect(520, 300, 300, 75)
    if input_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(estado_juego['pantalla'], "#5c6066", input_rect, border_radius=RADIO_BOTON)
    else:
        pygame.draw.rect(estado_juego['pantalla'], "#41454a", input_rect, border_radius=RADIO_BOTON)


def pantalla_menu(eventos, estado_juego):
    """
    Esta funcion se encarga de dibujar la pantalla del menu.
    """
    # estado_juego['pantalla'].fill(COLOR_FONDO)
    estado_juego['pantalla'].blit(cargar_imagen("img/fondo.jpeg", (1280, 720)), (0, 0))
    estado_juego['pantalla'].blit(cargar_imagen("img/logo.png", (600, 200)), (350, 40))
    fuente = pygame.font.Font(None, 40)
    dibujar_botones_menu(estado_juego['pantalla'], fuente, OPCIONES_MENU)
    
    pygame.display.flip()

def dibujar_botones_menu(pantalla, fuente, diccionario):
    """
    Esta funcion se encarga de dibujar los botones en el menu.
    Recibe: pantalla: Pantalla inicializada en Pygame a la que se dibujara.
            fuente: Fuente que tendran los textos de los botones
    No retorna nada
    """
    for opcion in diccionario:
        x, y = opcion["posicion"]
        texto = fuente.render(opcion["texto"], True, BLANCO)
        texto_rect = texto.get_rect(center=(x + ANCHO_BOTON // 2, y + ALTO_BOTON // 2))
        boton_rect = pygame.Rect(x, y, ANCHO_BOTON, ALTO_BOTON)
        if boton_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(pantalla, COLOR_BOTON_SELECCION, boton_rect, border_radius=RADIO_BOTON)
        else:
            pygame.draw.rect(pantalla, COLOR_BOTON, boton_rect, border_radius=RADIO_BOTON)
        pantalla.blit(texto, texto_rect.topleft)

def pantalla_juego(estado_juego:dict):
    """
    Esta funcion se encarga de dibujar la pantalla del juego.
    Recibe: estado_juego(dict): Diccionario con todos los elementos importantes del juego.
    No retorna nada.
    """
    estado_juego['pantalla'].blit(cargar_imagen("img\ingame.jpg"), (0, 0))
    errores = str(estado_juego['errores'])
    
    dibujar_temporizador(estado_juego)
    dibujar_tablero(estado_juego)
    
    fuente = pygame.font.SysFont(None, 50)
    errores = fuente.render(errores, True, "white")
    
    for elemento in DICCIONARIO_IMAGENES:
        estado_juego['pantalla'].blit(elemento["surface"], (elemento["posicion_x"], elemento["posicion_y"]))
    
    estado_juego['pantalla'].blit(errores, (580, 42))
    

def pantalla_puntajes(estado_juego:dict):
    """
    Esta funcion se encarga de dibujar la pantalla de puntajes.
    Recibe: estado_juego(dict): Diccionario con todos los elementos importantes del juego.
    No retorna nada
    """
    estado_juego['pantalla'].fill("lightblue")
    fuente = pygame.font.SysFont(None, 74)
    texto = fuente.render("Pantalla de Puntajes", True, "black")
    estado_juego['pantalla'].blit(texto, (400, 300))
    
    for diccionario_imagen in DICCIONARIO_IMAGENES:
        if diccionario_imagen['nombre'] == "volver":
            estado_juego['pantalla'].blit(diccionario_imagen['surface'], (diccionario_imagen['posicion_x'], diccionario_imagen['posicion_y']))

def pantalla_configuracion(estado_juego:dict):
    """
    Esta funcion se encarga de dibujar la pantalla de puntajes.
    Recibe: estado_juego(dict): Diccionario con todos los elementos importantes del juego.
    No retorna nada
    """
    estado_juego['pantalla'].blit(cargar_imagen("img/fondo.jpeg", (1280, 720)), (0, 0))
    estado_juego['pantalla'].blit(cargar_imagen("img/logo.png", (600, 200)), (350, 40))
    fuente = pygame.font.SysFont(None, 40)
    
    dibujar_input(estado_juego)
    
    for diccionario_imagen in DICCIONARIO_IMAGENES:
        if diccionario_imagen['nombre'] == "volver":
            estado_juego['pantalla'].blit(diccionario_imagen['surface'], (diccionario_imagen['posicion_x'], diccionario_imagen['posicion_y']))
            
    
    
    dibujar_botones_menu(estado_juego['pantalla'], fuente, OPCIONES_CONFIG)

def dibujar_tablero(estado_juego:dict):
    """
    Esta funcion se encarga de dibujar el tablero del sudoku durante la pantalla del juego.
    Recibe: estado_juego(dict): Diccionario con todos los datos importantes del juego.
    No tiene retorn
    """
    #lista_coordenadas = []
    fuente = pygame.font.SysFont(None, 32)
    celda_size = 60
    
    for i in range(9):
        for j in range(9):
            # Obtener el valor de la celda actual
            value = estado_juego['sudoku'][i][j]
            numero = fuente.render(str(estado_juego['sudoku'][i][j]), True, "black")
            
            if (i, j) in estado_juego['colores_celdas']:
                color = estado_juego['colores_celdas'][(i, j)]
            elif (i, j) in estado_juego['celdas_bloqueadas']:
                color = CELDA_RESUELTA
            elif estado_juego['celda_seleccionada'] == (i, j):
                color = "yellow"
            else:
                color = CELDA_VACIA

            # Dibujar el rectángulo (celda)          j * celda_size + 200                   Y                 ANCHO     ALTO
            pygame.draw.rect(estado_juego['pantalla'], color, (j * celda_size + 400, i * celda_size + 100, celda_size, celda_size))
            # lista_coordenadas.append((j * celda_size + 400, i * celda_size + 100, celda_size, celda_size))
            # Dibujar borde para cada celda
            pygame.draw.rect(estado_juego['pantalla'], LINEAS_CELDAS, (j * celda_size + 400, i * celda_size + 100, celda_size, celda_size), 1)
            
            if value != " ":
                estado_juego['pantalla'].blit(numero, (j * celda_size + 425, i * celda_size + 120))
                
    for elemento in LINEAS_TABLERO:
        x1, y1, x2, y2 = elemento
        pygame.draw.line(estado_juego['pantalla'], LINEAS_EXTERNAS, (x1, y1), (x2, y2), 3)
    pygame.draw.rect(estado_juego['pantalla'], LINEAS_EXTERNAS, (400, 100, 545, 545), 5)
    # print(lista_coordenadas)   
    
    


def dibujar_temporizador(estado_juego:dict):
    """
    Esta funcion se encarga de dibujar el cronometro durante la pantalla del juego
    Recibe: estado_juego(dict): Diccionario con todos los datos importantes del juego.
    No tiene retorno
    """
    fuente = pygame.font.SysFont(None, 50)
    texto = fuente.render(estado_juego['tiempo'], True, "white")
    estado_juego['pantalla'].blit(texto, (100, 100))