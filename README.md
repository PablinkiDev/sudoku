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

------------------------------------------------------------------------------------------------------------------------------------------------------

Corregir:
- ✅ Que las celdas al borrase vuelvan a su color original
- ❗ Al finalizar la partida mostrar la cadena minutos y segundos 
- ✅ Que el evento de ingresar numeros solo este en la pantalla del juego. 
- ✅ Una vez ingresado un numero correcto no pueda cambiarse, ni exploitearse para sumarse mas puntos. 
- ✅ Que se muestre el nombre en el input 
- ✅ Si gana un jugador y su nombre ya existe en el archivo, debe quedar el puntaje más alto. 
- ✅ Player por defecto. 
- ✅ Reinciar el tablero cuando cambia de dificultad 
- Que al seleccionar una celda con un valor ingresado se pinte para avisarle al usuario que la selecciono
- ✅ Limpiar el main
- Validar lectura y escritura de archivo
- ✅ Chequear penalizacion por minuto
- ✅ Chequear ordenamiento puntajes 
- ✅ Limpiar funciones que no utilicemos
- Modificar funciones a cosas vistas en la cursada (1 return, sin doble asignacion, etc)
- ✅ La funcion de dificultad debe recibir un porcentaje como parametro
- Agregar limite de caracteres al input

Importante:
- Modularizar y Documentar.



Prueba de penalizacion por tiempo:

Sin jugar: 1200 puntos
0:54 baja a 1198 puntos
1:54 baja a 1196 puntos
2:54 baja a 1194 puntos

Empiezo a jugar la min: 3:25
3:25 sube a 1199 puntos
3:54 baja a 1197

Prueba 2:
Jugue: 00:15 sube a 1205
0:59 bajo a 1203
1:59 bajo a 1201

Prueba 3 reiniciando desde el boton del game:
0:49 bajo a 1198
1:49 bajo a 1196

Prueba 4 reiniciando desde el boton del game al min 2:30
00:19 bajo a 1198
01:19 bajo a 1196

