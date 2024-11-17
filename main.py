from funciones import *


matriz = inicializar_matriz(9,9, 0)
generar_sudoku(matriz)
print("---Tablero Generado---")
mostrar_sudoku(matriz)
print("")
print("---Sudoku Generado---")
sudoku = ocultar_celdas(matriz, 0.2)
mostrar_sudoku(sudoku)


########################################### MAIN ####################################################

pygame.init()

estado = "menu"

# Ventana
pantalla = pygame.display.set_mode(DIMENSIONES_PANTALLA)

fondo = pygame.image.load("img/fondo.jpg")

FUENTE = pygame.font.Font(None, 25)
tablero = pygame.image.load("img/board.png")




while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            estado = validar_colisiones_menu(evento, OPCIONES_MENU, estado)
            print(evento.pos)
    pantalla.blit(fondo, (0, 0))
    dibujar_botones_menu(pantalla, FUENTE)
    if estado == "jugar":
        pantalla.fill((0, 150, 0))
        pantalla.blit(tablero, (400, 100))
            
    elif estado == "puntajes":
        pantalla.fill((0, 0, 150))
    
    
    # Actualizamos la pantalla
    pygame.display.flip()
