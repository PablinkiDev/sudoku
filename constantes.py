import pygame

# CONFIGURACIONES
DIMENSIONES_PANTALLA = (1280, 720)
OPCIONES_MENU = [
    {"texto": "Jugar", "posicion": (520, 300)},
    {"texto": "Puntajes", "posicion": (520, 400)},
    {"texto": "Configuracion", "posicion": (520, 500)},
    {"texto": "Salir", "posicion": (520, 600)},
]

DIFICULTADES = ["Facil", "Intermedio", "Dificil"]
DARK_MODE = ["SI", "NO"]

OPCIONES_CONFIG = [
    {"btn": 1, "texto": f"Dificultad {DIFICULTADES[0]}", "posicion": (520, 400)},
    {"btn": 2, "texto": "Resolucion: -", "posicion": (520, 500)},
    {"btn": 3, "texto": f"Modo oscuro: {DARK_MODE[0]}", "posicion": (520, 600)}
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
NEGRO = (0, 0, 0)
COLOR_SELECCION = (255, 0, 0)
COLOR_BOTON = "#3b65a3"
COLOR_BOTON_SELECCION = "#5382c9"

COLOR_CORRECTO = "#b7f0b6"
COLOR_ERROR = "#f0b6b7"


LINEAS_EXTERNAS = "#1c3742"
LINEAS_CELDAS = "#71828a"
CELDA_RESUELTA = "#abb6ba"
CELDA_VACIA = "#c8d5db"
CELDA_SELECCIONADA = "#BBDEFB"

# MUSICA
pygame.mixer.init()
MUSICA_MENU = pygame.mixer.Sound("music/intro.mp3")
MUSICA_JUEGO = pygame.mixer.Sound("music/juego.mp3")

# PUNTAJE
PUNTAJE_BASE = 1000
PENALIZACION_POR_ERRORES = 7
PENALIZACION_POR_TIEMPO = 10
BONIFICACION_POR_ACIERTO = 5
BONIFICACION_DIFICULTAD_FACIL = 1.0
BONIFICACION_DIFICULTAD_MEDIA = 1.4
BONIFICACION_DIFICULTAD_DIFICIL = 2.0

# RANKING
ORO = "#e3ba24"
PLATA = "#969695"
BRONCE = "#6e5401"

