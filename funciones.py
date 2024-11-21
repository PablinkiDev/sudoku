import random
import pygame
from constantes import *

          
def validar_colisiones_menu(evento, opciones, estado):
    x, y = evento.pos
    for opcion in opciones:
        texto_rect = pygame.Rect(opcion["posicion"][0], opcion["posicion"][1], ANCHO_BOTON, ALTO_BOTON)
        if texto_rect.collidepoint(x, y):
            if opcion["texto"] == "Jugar":
                estado = "jugar"
            elif opcion["texto"] == "Puntajes":
                estado = "puntajes"
            elif opcion["texto"] == "Salir":
                pygame.quit()
                quit()
                
    return estado

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
    
