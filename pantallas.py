from interfaces import pantalla_menu, pantalla_juego, pantalla_puntajes

def cambiar_pantalla(estado, tiempo, errores, diccionario, eventos, dificultad):
        if estado == "inicio":
            pantalla_menu(eventos, dificultad)
        elif estado == "jugar":
            pantalla_juego(tiempo, errores, diccionario)
        elif estado == "puntajes":
            pantalla_puntajes()