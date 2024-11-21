from interfaces import pantalla_menu, pantalla_juego, pantalla_puntajes

def cambiar_pantalla(estado, tiempo, errores, diccionario, eventos, dificultad):
    """
    Esta funcion se encarga de cambiar las pantallas del juego segun el estado del mismo.
    """
        if estado == "inicio":
            pantalla_menu(eventos, dificultad)
        elif estado == "jugar":
            pantalla_juego(tiempo, errores, diccionario)
        elif estado == "puntajes":
            pantalla_puntajes()