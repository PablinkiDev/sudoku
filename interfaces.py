import pygame
from constantes import *
from imagenes import cargar_imagen, DICCIONARIO_IMAGENES
from logica_sudoku import inicializar_tablero_sudoku
from funciones import mostrar_mensaje


def dibujar_ranking(estado_juego):
    FUENTE = pygame.font.Font(None, 72)
    x = 380
    y = 250
    for i in range(5):
        top = i + 1
        if top == 1:
            color = ORO
        elif top == 2:
            color = PLATA
        elif top == 3:
            color = BRONCE
        else:
            color = BLANCO
        nombre = FUENTE.render(estado_juego['ranking'][i]['user'], True, color)
        puntos = FUENTE.render(str(estado_juego['ranking'][i]['points']), True, color)
        top_texto = FUENTE.render(str(top), True, color)
        
        estado_juego['pantalla'].blit(top_texto, (x, y))
        estado_juego['pantalla'].blit(nombre, (x + 100, y))
        estado_juego['pantalla'].blit(puntos, (x + 400, y))
        y += 80


def pantalla_win(estado_juego):
    estado_juego['pantalla'].blit(cargar_imagen("img/win_background.jpg"), (0, 0))
    estado_juego['pantalla'].blit(cargar_imagen('img/win.webp', (400, 300)), (480, 10))
    
    for elemento in DICCIONARIO_IMAGENES:
        if elemento['nombre'] == "volver_white":
            estado_juego['pantalla'].blit(elemento["surface"], (elemento["posicion_x"], elemento["posicion_y"]))
    
    mostrar_mensaje(f"Felicidad {estado_juego['user']} por completar el Sudoku", estado_juego['pantalla'], (670, 315), BLANCO, 50)
    mostrar_mensaje(f"Tardaste {estado_juego['minutos']} minutos", estado_juego['pantalla'], (670, 370), BLANCO, 50)
    mostrar_mensaje(f"Hiciste {estado_juego['puntaje']} puntos", estado_juego['pantalla'], (670, 420), BLANCO, 50)
    mostrar_mensaje(f"Tuviste {estado_juego['errores']} errores", estado_juego['pantalla'], (670, 470), BLANCO, 50)
    
    
def dibujar_input(estado_juego):
    font = pygame.font.Font(None, 32)
    mostrar_mensaje("Nombre de usuario", estado_juego['pantalla'], (670, 300), "white", 30)
    
    if estado_juego['input_rect'].collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(estado_juego['pantalla'], "#5c6066", estado_juego['input_rect'])
    else:
        pygame.draw.rect(estado_juego['pantalla'], "#41454a", estado_juego['input_rect'])
        
        
    if estado_juego['activo_input'] == True:
        pygame.draw.rect(estado_juego['pantalla'], "#333333", estado_juego['input_rect'])  # Fondo gris del input
        text_surface = font.render(estado_juego['user'], True, "red")
        estado_juego['pantalla'].blit(text_surface, (estado_juego['input_rect'].x + 10, estado_juego['input_rect'].y + 10))  # Posición del texto

def pantalla_menu(eventos, estado_juego):
    """
    Esta funcion se encarga de dibujar la pantalla del menu.
    """
    # estado_juego['pantalla'].fill(COLOR_FONDO)
    estado_juego['pantalla'].blit(cargar_imagen("img/fondo.jpeg", (1280, 720)), (0, 0))
    estado_juego['pantalla'].blit(cargar_imagen("img/logo.png", (600, 200)), (350, 40))
    fuente = pygame.font.Font(None, 40)
    dibujar_botones_menu(estado_juego['pantalla'], fuente, OPCIONES_MENU)


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
    fuente = pygame.font.SysFont(None, 50)
    estado_juego['pantalla'].blit(cargar_imagen("img\ingame.jpg"), (0, 0))
    errores = str(estado_juego['errores'])
    texto_puntaje = f"Score: {str(estado_juego['puntaje'])}"
    if estado_juego['puntaje'] < 0:
        estado_juego['puntaje'] = 0
    texto_puntaje = fuente.render(texto_puntaje, True, "red")
    
    
    dibujar_temporizador(estado_juego)
    dibujar_tablero(estado_juego)
    
    fuente = pygame.font.SysFont(None, 50)
    errores = fuente.render(errores, True, "white")
    
    for elemento in DICCIONARIO_IMAGENES:
        if elemento['nombre'] == "volver_white":
            continue
        estado_juego['pantalla'].blit(elemento["surface"], (elemento["posicion_x"], elemento["posicion_y"]))
    
    estado_juego['pantalla'].blit(errores, (580, 42))
    estado_juego['pantalla'].blit(texto_puntaje, (780, 42))
    

def pantalla_puntajes(estado_juego:dict):
    """
    Esta funcion se encarga de dibujar la pantalla de puntajes.
    Recibe: estado_juego(dict): Diccionario con todos los elementos importantes del juego.
    No retorna nada
    """
    estado_juego['pantalla'].blit(cargar_imagen("img/fondo.jpeg", (1280, 720)), (0, 0))
    estado_juego['pantalla'].blit(cargar_imagen("img/logo.png", (600, 200)), (350, 40))
    fuente = pygame.font.SysFont(None, 74)
    
    dibujar_ranking(estado_juego)
    
    for elemento in DICCIONARIO_IMAGENES:
        if elemento['nombre'] == "volver_white":
            estado_juego['pantalla'].blit(elemento["surface"], (elemento["posicion_x"], elemento["posicion_y"]))

def pantalla_configuracion(estado_juego:dict):
    """
    Esta funcion se encarga de dibujar la pantalla de puntajes.
    Recibe: estado_juego(dict): Diccionario con todos los elementos importantes del juego.
    No retorna nada
    """
    
    fuente = pygame.font.SysFont(None, 40)
    estado_juego['pantalla'].blit(cargar_imagen("img/fondo.jpeg", (1280, 720)), (0, 0))
    estado_juego['pantalla'].blit(cargar_imagen("img/logo.png", (600, 200)), (350, 40))
    
    dibujar_input(estado_juego)
    dibujar_botones_menu(estado_juego['pantalla'], fuente, OPCIONES_CONFIG)
    
    for elemento in DICCIONARIO_IMAGENES:
        if elemento['nombre'] == "volver_white":
            estado_juego['pantalla'].blit(elemento["surface"], (elemento["posicion_x"], elemento["posicion_y"]))
    


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