from constantes import *
from funciones import *
from imagenes import *
from logica_sudoku import *
from interfaces import *

#####################################################################################################
########################################### MAIN ####################################################

pygame.init()
pygame.mixer.init()

matriz = inicializar_matriz(9, 9, 0)
generar_sudoku(matriz)
mostrar_sudoku(matriz)
sudoku = ocultar_celdas(matriz)

estado = "inicio"
dificultad = "facil"

# Ventana
pantalla = pygame.display.set_mode(DIMENSIONES_PANTALLA)

FUENTE = pygame.font.Font(None, 74)
mi_evento_segundo = pygame.USEREVENT + 1
un_segundo = 1000
pygame.time.set_timer(mi_evento_segundo, un_segundo)

tupla = ("", 0, 0)
tiempo, segundos, minutos = tupla
errores = 0

# Diccionario Global
estado_juego = {
    'pantalla': pantalla,
    'sudoku': sudoku,
    'solucion': matriz,
    'estado': estado,
    'dificultad': dificultad,
    'tiempo': tiempo,
    'errores': errores,
    'segundos': segundos,
    'minutos': minutos,
    'celda_seleccionada': None,
}

estado_juego['celdas_bloqueadas'] = inicializar_celdas_bloqueadas(estado_juego['sudoku'])
estado_juego['colores_celdas'] = {}

# poner_musica("music/intro.mp3", 0.4, 1000)

musica_menu = pygame.mixer.Sound("music/intro.mp3")
musica_juego = pygame.mixer.Sound("music/juego.mp3")
musica_actual = None

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if estado_juego['estado'] == "inicio":
                estado_juego['estado'] = validar_colisiones_menu(evento, OPCIONES_MENU, estado)
            if estado_juego['estado'] == "jugar" and volver_rect.collidepoint(pygame.mouse.get_pos()):
                estado_juego['estado'] = "inicio"
            if estado_juego['estado'] == "jugar" and reset_rect.collidepoint(pygame.mouse.get_pos()):
                estado_juego['sudoku'] = inicializar_tablero_sudoku()
                estado_juego['celdas_bloqueadas'] = inicializar_celdas_bloqueadas(estado_juego['sudoku'])
                estado_juego['colores_celdas'] = {}
                estado_juego['errores'] = 0
                estado_juego['tiempo'], estado_juego['segundos'], estado_juego['minutos'] = "", 0, 0
            if estado_juego['estado'] == "jugar":
                detectar_click(estado_juego, evento)
        if evento.type == pygame.KEYDOWN:
            ingresar_numero(estado_juego, evento)
        if evento.type == mi_evento_segundo and estado_juego['estado'] == "jugar":
            estado_juego['tiempo'], estado_juego['segundos'], estado_juego['minutos'] = calcular_tiempo_jugado(estado_juego['segundos'], estado_juego['minutos'])

    if estado_juego['estado'] == "inicio":
        pantalla_menu(evento, estado_juego)  
        if musica_actual != musica_menu:
            if musica_actual:
                musica_actual.stop()
            musica_menu.play(-1)
            musica_actual = musica_menu
    elif estado_juego['estado'] == "jugar":
        if musica_actual != musica_juego:
            if musica_actual:
                musica_actual.stop()
            musica_juego.play(-1)
            musica_actual = musica_juego

            
        pantalla_juego(estado_juego)
        # poner_musica("music/juego.mp3", 0.4, 1000)
    elif estado_juego['estado'] == "puntajes":
        pantalla_puntajes(estado_juego)

    # Actualizamos la pantalla
    pygame.display.flip()

