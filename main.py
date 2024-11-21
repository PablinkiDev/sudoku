from constantes import *
from funciones import *
from imagenes import *
from logica_sudoku import *
from interfaces import *

#####################################################################################################
########################################### MAIN ####################################################

pygame.init()

sudoku = inicializar_tablero_sudoku()
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
    'estado': estado,
    'dificultad': dificultad,
    'tiempo': tiempo,
    'errores': errores,
    'segundos': segundos,
    'minutos': minutos
}

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            print(evento.pos)
            if estado_juego['estado'] == "inicio":
                estado_juego['estado'] = validar_colisiones_menu(evento, OPCIONES_MENU, estado)
            if estado_juego['estado'] == "jugar" and volver_rect.collidepoint(pygame.mouse.get_pos()):
                estado_juego['estado'] = "inicio"
            if estado_juego['estado'] == "jugar" and reset_rect.collidepoint(pygame.mouse.get_pos()):
                estado_juego['sudoku'] = inicializar_tablero_sudoku()
                estado_juego['tiempo'], estado_juego['segundos'], estado_juego['minutos'] = "", 0, 0

        if evento.type == mi_evento_segundo and estado_juego['estado'] == "jugar":
            estado_juego['tiempo'], estado_juego['segundos'], estado_juego['minutos'] = calcular_tiempo_jugado(estado_juego['segundos'], estado_juego['minutos'])

    if estado_juego['estado'] == "inicio":
        pantalla_menu(evento, estado_juego)
    elif estado_juego['estado'] == "jugar":
        pantalla_juego(estado_juego)
    elif estado_juego['estado'] == "puntajes":
        pantalla_puntajes(estado_juego)

    # Actualizamos la pantalla
    pygame.display.flip()

