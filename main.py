from funciones import *
from imagenes import *

matriz = inicializar_matriz(9,9, 0)
generar_sudoku(matriz)
sudoku = ocultar_celdas(matriz, 0.2)


#####################################################################################################
########################################### MAIN ####################################################

pygame.init()

estado = "inicio"
dificultad = "facil"


# Ventana
pantalla = pygame.display.set_mode(DIMENSIONES_PANTALLA)

fondo = pygame.image.load("img/fondo.jpg")

FUENTE = pygame.font.Font(None, 74)
mi_evento_segundo = pygame.USEREVENT + 1
un_segundo = 150
pygame.time.set_timer(mi_evento_segundo, un_segundo)

def pantalla_menu(eventos, dificultad):
    dibujar_botones_menu(pantalla, FUENTE)
    fuente = pygame.font.Font(None, 40)
    
    # facil = fuente.render("Facil", True, "white")
    # intermedio = fuente.render("Intermedio", True, "white")
    # dificil = fuente.render("Dificil", True, "white")
    
    # if dificultad == "facil":
    #     facil = fuente.render("Facil", True, "green")
    # elif dificultad == "intermedio":
    #     intermedio = fuente.render("Intermedio", True, "green")
    # elif dificultad == "dificil":
    #     dificil = fuente.render("Dificil", True, "green")
    
    # facil_rect = facil.get_rect()
    # intermedio_rect = intermedio.get_rect()
    # dificil_rect = dificil.get_rect()
    # facil_rect.topleft = (1000, 100)
    # intermedio_rect.topleft = (1000, 140)
    # dificil_rect.topleft = (1000, 180)
                    
    # pantalla.blit(facil, facil_rect)
    # pantalla.blit(intermedio, intermedio_rect)
    # pantalla.blit(dificil, dificil_rect)
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if facil_rect.collidepoint(evento.pos):
                dificultad = "facil"
            elif intermedio_rect.collidepoint(evento.pos):
                dificultad = "intermedio"
            elif dificil_rect.collidepoint(evento.pos):
                dificultad = "dificil"
    
    pygame.display.flip()

def dibujar_tablero():
    fuente = pygame.font.SysFont(None, 22)
    cell_size = 50
    
    for i in range(9):
        for j in range(9):
            # Obtener el valor de la celda actual
            value = sudoku[i][j]
            numero = fuente.render(str(sudoku[i][j]), True, "black")
            
            if value != " ":
                color = "#edbfb7"
            else:
                color = "#db8779"
            

            # Dibujar el rectángulo (celda)          j * cell_size + 200                   Y                 ANCHO     ALTO
            pygame.draw.rect(pantalla, color, (j * cell_size + 400, i * cell_size + 100, cell_size, cell_size))
            
            # Dibujar borde para cada celda
            pygame.draw.rect(pantalla, "#b3341e", (j * cell_size + 400, i * cell_size + 100, cell_size, cell_size), 1)
            
            
            if value != " ":
                pantalla.blit(numero, (j * cell_size + 420, i * cell_size + 120))
                
    for elemento in LINEAS_TABLERO:
        x1, y1, x2, y2 = elemento
        pygame.draw.line(pantalla, "red", (x1, y1), (x2, y2), 3)
    pygame.draw.rect(pantalla, "red", (400, 100, 450, 450), 5)
            
    
def pantalla_juego(tiempo, errores, diccionario):
    pantalla.fill("#e8cca5")
    errores = str(errores)
    
    
    
    dibujar_temporizador(tiempo)
    dibujar_tablero()
    
    fuente = pygame.font.SysFont(None, 50)
    errores = fuente.render(errores, True, "black")
    
    for elemento in diccionario:
        pantalla.blit(elemento["surface"], (elemento["posicion_x"], elemento["posicion_y"]))
    
    pantalla.blit(errores, (580, 42))
    
    pygame.display.flip()
    

def pantalla_puntajes():
    pantalla.fill("lightblue")
    fuente = pygame.font.SysFont(None, 74)
    texto = fuente.render("Pantalla de Puntajes", True, "black")
    pantalla.blit(texto, (400, 300))
    pygame.display.flip()

def cambiar_pantalla(estado, tiempo, errores, diccionario, eventos, dificultad):
        if estado == "inicio":
            pantalla_menu(eventos, dificultad)
        elif estado == "jugar":
            pantalla_juego(tiempo, errores, diccionario)
        elif estado == "puntajes":
            pantalla_puntajes()

def calcular_tiempo_jugado(segundos, minutos):
    segundos += 1
    if segundos > 60:
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
    return cadena, segundos, minutos

def dibujar_temporizador(tiempo:str):
    fuente = pygame.font.SysFont(None, 50)
    texto = fuente.render(tiempo, True, "black")
    pantalla.blit(texto, (100, 100))

tupla = ("", 0, 0)
tiempo, segundos, minutos = tupla
errores = 0




fuente = pygame.font.Font(None, 40)

facil = fuente.render("Facil", True, "white")
intermedio = fuente.render("Intermedio", True, "white")
dificil = fuente.render("Dificil", True, "white")
    
if dificultad == "facil":
    facil = fuente.render("Facil", True, "green")
elif dificultad == "intermedio":
    intermedio = fuente.render("Intermedio", True, "green")
elif dificultad == "dificil":
    dificil = fuente.render("Dificil", True, "green")
    
facil_rect = facil.get_rect()
intermedio_rect = intermedio.get_rect()
dificil_rect = dificil.get_rect()
facil_rect.topleft = (1000, 100)
intermedio_rect.topleft = (1000, 140)
dificil_rect.topleft = (1000, 180)
                    





while True:
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(facil, facil_rect)
    pantalla.blit(intermedio, intermedio_rect)
    pantalla.blit(dificil, dificil_rect)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            # print(evento.pos)
            print(dificultad)
            if estado == "inicio":
                estado = validar_colisiones_menu(evento, OPCIONES_MENU, estado)


            
            if estado == "jugar" and volver_rect.collidepoint(pygame.mouse.get_pos()):
                estado = "inicio"
            if estado == "jugar" and reset_rect.collidepoint(pygame.mouse.get_pos()):
                matriz = inicializar_matriz(9,9, 0)
                generar_sudoku(matriz)
                sudoku = ocultar_celdas(matriz, 0.2)
                tiempo, segundos, minutos = ("", 0, 0)
                
            if facil_rect.collidepoint(evento.pos):
                dificultad = "facil"
            elif intermedio_rect.collidepoint(evento.pos):
                dificultad = "intermedio"
            elif dificil_rect.collidepoint(evento.pos):
                dificultad = "dificil"
            
        if evento.type == mi_evento_segundo and estado == "jugar":
            tiempo, segundos, minutos = calcular_tiempo_jugado(segundos, minutos)

    cambiar_pantalla(estado, tiempo, errores, DICCIONARIO_IMAGENES, pygame.event.get(), dificultad)
    

    # Actualizamos la pantalla
    pygame.display.flip()
    
