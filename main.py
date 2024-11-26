from constantes import *
from funciones import *
from imagenes import *
from logica_sudoku import *
from interfaces import *

#####################################################################################################
########################################### MAIN ####################################################

pygame.init()

# Ventana
pantalla = pygame.display.set_mode(DIMENSIONES_PANTALLA)
pygame.display.set_caption("SUDOKU")

#FUENTE = pygame.font.Font(None, 74)
mi_evento_segundo = pygame.USEREVENT + 1
un_segundo = 1000
pygame.time.set_timer(mi_evento_segundo, un_segundo)

mi_evento_minuto = pygame.USEREVENT + 2
un_minuto = 60000
pygame.time.set_timer(mi_evento_minuto, un_minuto)


######## BORRAR ###################
tupla = ("", 0, 0)
tiempo, segundos, minutos = tupla
errores = 0
input_rect = pygame.Rect(520, 325, 300, 50)


# Diccionario Global
estado_juego = {
    'pantalla': pantalla,
    'tablero_armado': False,
    'solucion': None,
    'sudoku':  None,
    'estado': "inicio",
    'dificultad': "facil",
    'dificultad_calculada': False,
    'tiempo': "",
    'errores': 0,
    'segundos': 0,
    'minutos': 0,
    'celda_seleccionada': None,
    'user': "Player",
    'puntaje': PUNTAJE_BASE,
    'puntos_calculados': False,
    'activo_input': False,
    'input_rect': input_rect,
    'ranking': leer_json('datos.json'),
}

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
                resetear_juego(estado_juego)
            if estado_juego['estado'] == "jugar":
                detectar_click(estado_juego, evento) # Cambia celda seleccionada
            if estado_juego['estado'] == "win":
                if volver_rect.collidepoint(pygame.mouse.get_pos()):
                    estado_juego['estado'] = "inicio"
                    resetear_juego(estado_juego)
            if estado_juego['estado'] == 'configuracion':
                validar_colisiones_configuraciones(evento, OPCIONES_CONFIG, estado_juego)
        if evento.type == pygame.KEYDOWN:
            # Solo para la pantalla del juego
            ingresar_numero(estado_juego, evento)
        if evento.type == mi_evento_segundo and estado_juego['estado'] == "jugar":
            estado_juego['tiempo'], estado_juego['segundos'], estado_juego['minutos'] = calcular_tiempo_jugado(estado_juego['segundos'], estado_juego['minutos'])
        if evento.type == mi_evento_minuto and estado_juego['estado'] == "jugar":
            estado_juego['puntaje'] -= PENALIZACION_POR_TIEMPO

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if estado_juego['input_rect'].collidepoint(evento.pos):
                estado_juego['activo_input'] = True
                if estado_juego['user'] == "Player":
                        estado_juego['user'] = ""
        elif evento.type == pygame.KEYDOWN:
            if estado_juego['activo_input']:
                if evento.key == pygame.K_BACKSPACE:
                    estado_juego['user'] = estado_juego['user'][:-1]
                elif evento.key == pygame.K_RETURN:
                    print(estado_juego['user'])
                    estado_juego['activo_input'] = False
                else:
                    estado_juego['user'] += evento.unicode
    if estado_juego['estado'] != "configuracion":
        estado_juego['activo_input'] = False

    if estado_juego['estado'] == "inicio":
        pantalla_menu(estado_juego)  
        musica_actual = validar_musica(musica_actual, MUSICA_MENU)
    elif estado_juego['estado'] == "jugar":
        if estado_juego['tablero_armado'] == False:
            solucion = generar_sudoku()
            sudoku = ocultar_celdas(solucion, estado_juego['dificultad'])
            estado_juego['solucion'] = solucion
            estado_juego['sudoku'] = sudoku
            estado_juego['celdas_bloqueadas'] = inicializar_celdas_bloqueadas(estado_juego['sudoku'])
            estado_juego['tablero_armado'] = True
        if estado_juego['dificultad_calculada'] == False:
            estado_juego['puntaje'] = calcular_dificultad(estado_juego)
            estado_juego['dificultad_calculada'] = True
        musica_actual = validar_musica(musica_actual, MUSICA_JUEGO)
        pantalla_juego(estado_juego)
    elif estado_juego['estado'] == "configuracion":
        pantalla_configuracion(estado_juego)
    elif estado_juego['estado'] == "puntajes":
        ordenar_ranking(estado_juego['ranking'])
        pantalla_puntajes(estado_juego)
    elif estado_juego['estado'] == 'win':
        pantalla_win(estado_juego)
    
    if estado_juego['tablero_armado'] != False:
        if verificar_victoria(estado_juego) and estado_juego['estado'] == "jugar":
            estado_juego['estado'] = "win"
            if estado_juego['puntos_calculados'] == False:
                escribir_json('datos.json', estado_juego)
                estado_juego['puntos_calculados'] = True
        
    # Actualizamos la pantalla
    pygame.display.flip()