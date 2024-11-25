# Programacion I - Parcial 2: Pygame | Comision 311 T.N.

### Estudiantes

- Agustín Pablo Fernandez
- Thiago Duda
- Facundo Gasparrini

# Estado

## Punto 1)

- Pantalla de inicio o menu principal con botones "Jugar", "Puntajes" y "Salir". ✔️
- En esta pantalla se debe seleccionar la dificultad del juego. ❌
- Pantalla principal del juego: Tablero de sudoku, temporizador, contador de errores, boton de reinicio, boton volver. ❗
    - Falta funcionalidades del tablero, y contador de errores
- Pantalla de puntajes: Top 5 de los mejores puntajes con sus respectivos nombres, ordenados de mayor a menor. ❌

Punto 5) Hecho.


Cambios desde la defensa:

Se agrego:
- Funcion validar_musica() en el archivo **funciones.py** 
- Se cambio el fondo del menu
- Se soluciono el hover de los botones en el menu
- Se agrego la opcion de Configuraciones
- Se soluciono un bug ingame:
    Al resetear el juego, se generaba un tablero nuevo, pero la matriz de la solución no cambiaba nunca. 
    Por lo tanto el juego seguia teniendo la misma solucion, rompiendo las reglas del Sudoku.
- Se agrego un input para que el usuario ingrese su nombre.
- Se agregaron los puntajes:
    - Agregamos constantes para cada valor numerico fijo a manejar.
    - Mostramos el puntaje en vivo durante la partida.
    - Se escribe los datos al finalizar la partida en un json.
    - Se lee el json al inicializar el programa.
- Se agrego pantalla de finalización del juego:
    - Se muestran los datos (nombre, puntaje, errores, tiempo)
    - Boton para volver al menu
- Se agrego la funcionalidad de cambiar la dificultad en la configuracion.
- Se agrego pantalla de puntajes con el TOP 5.