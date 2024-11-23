from constantes import *
from funciones import *
from imagenes import *
from logica_sudoku import *
from interfaces import *

#####################################################################################################
########################################### MAIN ####################################################

pygame.init()

matriz = inicializar_matriz(9, 9, 0)
generar_sudoku(matriz)
mostrar_sudoku(matriz)
sudoku = ocultar_celdas(matriz)

# Ventana
pantalla = pygame.display.set_mode(DIMENSIONES_PANTALLA)
pygame.display.set_caption("SUDOKU")

FUENTE = pygame.font.Font(None, 74)
mi_evento_segundo = pygame.USEREVENT + 1
un_segundo = 1000
pygame.time.set_timer(mi_evento_segundo, un_segundo)

estado_juego = {
    'pantalla': pantalla,
    'sudoku': sudoku,
    'solucion': matriz,
    'estado': "inicio",
    'dificultad': "facil",
    'tiempo': "",
    'errores': 0,
    'segundos': 0,
    'minutos': 0,
    'celda_seleccionada': None,
}

estado_juego['celdas_bloqueadas'] = inicializar_celdas_bloqueadas(estado_juego['sudoku'])
estado_juego['colores_celdas'] = {}

musica_actual = None

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if estado_juego['estado'] == "inicio":
                estado_juego['estado'] = validar_colisiones_menu(evento, OPCIONES_MENU, estado_juego['estado'])
            if (estado_juego['estado'] == "jugar" or estado_juego['estado'] == "configuracion" or estado_juego['estado'] == "puntajes") and volver_rect.collidepoint(pygame.mouse.get_pos()):
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
        musica_actual = validar_musica(musica_actual, MUSICA_MENU)
    elif estado_juego['estado'] == "jugar":
        musica_actual = validar_musica(musica_actual, MUSICA_JUEGO)
        pantalla_juego(estado_juego)
    elif estado_juego['estado'] == "configuracion":
        pantalla_configuracion(estado_juego)
    elif estado_juego['estado'] == "puntajes":
        pantalla_puntajes(estado_juego)
        
    if verificar_victoria(estado_juego):
        mostrar_mensaje("Ganaste! :D", estado_juego['pantalla'])

    # Actualizamos la pantalla
    pygame.display.flip()