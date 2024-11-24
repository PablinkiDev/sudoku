import pygame

# CONFIGURACIONES
DIMENSIONES_PANTALLA = (1280, 720)
OPCIONES_MENU = [
    {"texto": "Jugar", "posicion": (520, 300)},
    {"texto": "Puntajes", "posicion": (520, 400)},
    {"texto": "Configuracion", "posicion": (520, 500)},
    {"texto": "Salir", "posicion": (520, 600)},
]

OPCIONES_CONFIG = [
    {"texto": "Dificultad:", "posicion": (520, 400)},
    {"texto": "Resolucion: 1280x720", "posicion": (520, 500)},
    {"texto": "Modo claro: NO", "posicion": (520, 600)},
    
]

LINEAS_TABLERO = [
    (580, 102, 580, 640),
    (760, 103, 760, 640),
    (403, 280, 940, 280),
    (403, 460, 940, 460),
]
    #(400, 100, 450, 450)
 
# BOTONES MENU
ANCHO_BOTON = 300
ALTO_BOTON = 75
RADIO_BOTON = 15

# COLORES
COLOR_FONDO = "#183b4a"
BLANCO = (255, 255, 255)
COLOR_SELECCION = (255, 0, 0)
COLOR_BOTON = "#3b65a3"
COLOR_BOTON_SELECCION = "#5382c9"

COLOR_CORRECTO = "#b7f0b6"
COLOR_ERROR = "#f0b6b7"

LINEAS_EXTERNAS = "#1c3742"
LINEAS_CELDAS = "#71828a"
CELDA_RESUELTA = "#abb6ba"
CELDA_VACIA = "#c8d5db"


# MUSICA
pygame.mixer.init()
MUSICA_MENU = pygame.mixer.Sound("music/intro.mp3")
MUSICA_JUEGO = pygame.mixer.Sound("music/juego.mp3")