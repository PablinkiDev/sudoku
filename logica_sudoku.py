import random
import copy

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any)->list[list[any]]:
    """
    Esta función se encarga de inicializar una matriz con un valor inicial.
    Recibe: cant_filas(int): Cantidad de filas que va a tener la matriz
            cant_columnas(int): Cantidad de columnas que va a tener la matriz
            valor_inicial(any): Dato con el que se va a inicializar la matriz
    Retorna: matriz(list[list[any]]): Matriz con las dimensiones creada con los datos cargados como valor inicial. 
    """
    matriz = []
    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

def mostrar_sudoku(matriz:list[list])->None:
    """
    Esta funcion se encarga de imprimir en consola la cuadricula del sudoku.
    Recibe: matriz(list[list])
    No retorna nada.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 3 or j == 6:
                print(" ", end=" ")  
            print(matriz[i][j], end=" ")
        if i == 2 or i == 5:
            print(" ")
        print("")

def generar_sudoku(matriz):
    """
    Esta funcion se encarga de cargar una matriz 9x9 respetando las reglas del sudoku.
    Recibe: matriz(list[list]): Matriz inicializada a cargar
    Retorna: False si no encuentra numeros validos para cargar. 
            True si todas las celdas se llenaron.
    """
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:  # Solo intentamos llenar celdas vacías
                numeros = list(range(1, 10))  # Convertimos el rango a una lista
                random.shuffle(numeros)  # Barajamos los números del 1 al 9
                for numero in numeros:
                    if validar_numero_sudoku(matriz, numero, i, j):
                        matriz[i][j] = numero
                        if generar_sudoku(matriz):
                            return True
                        matriz[i][j] = 0  # Retrocedemos si no encontramos una solución
                return False  # Si no hay números válidos, volvemos
    return True  # Si todas las celdas se llenaron, el Sudoku está completo

def validar_numero_sudoku(matriz, numero, fila, columna):
    """
    Esta funcion se encarga de validar que el numero que se va a ingresar a una celda no se encuentre
    en la subcuadricula, ni en la misma fila, ni en la columna.
    Recibe: matriz(list[list]): Matriz a validar.
            numero(int): Numero a validar en la fila o columna.
            fila(int): Indice de la fila a validar.
            columna(int): Indice de la columna a validar
    Retorna: False si falla alguna de las validaciones.
            True si se valida correctamente.
    """
    # Validar la fila
    for i in range(9):
        if matriz[fila][i] == numero:
            return False
    
    # Validar la columna
    for j in range(9):
        if matriz[j][columna] == numero:
            return False
    
    # Validar la subcuadrícula de 3x3
    subcuadrícula_fila_inicio = (fila // 3) * 3
    subcuadrícula_columna_inicio = (columna // 3) * 3
    
    for i in range(3):
        for j in range(3):
            if matriz[subcuadrícula_fila_inicio + i][subcuadrícula_columna_inicio + j] == numero:
                return False
    
    return True

# ----------------------

def ocultar_celdas(matriz:list[list[int]], porcentaje:float = 0.2):
    """
    Esta funcion se encarga de ocultar de forma aleatoria distintos elementos de una matriz creando una copia de esta.
    Recibe: matriz[list[list[any]]]: Matriz a copiar para esconderle celdas.
            porcentaje[float]: Por defecto 0.2. Porcentaje de celdas a ocultar.
    Retorna: copia_tablero[list[list[any]]]: Copia de la matriz con celdas ocultas.
    """
    cantidad_celdas_a_ocultar = int(81 * porcentaje)
    copia_tablero = copy.deepcopy(matriz)
    
    for _ in range(cantidad_celdas_a_ocultar):
        fila = random.randint(0,8)
        columna = random.randint(0,8)
        while copia_tablero[fila][columna] == " ":
            fila = random.randint(0,8)
            columna = random.randint(0,8)
        copia_tablero[fila][columna] = " "
    return copia_tablero


def inicializar_tablero_sudoku():
    """
    Esta funcion se encarga de inicializar el tablero de una matriz.
    Trabaja con las funciones inicializar_matriz, generar_sudoku y ocultar_celdas.
    No recibe parametros.
    Retorna: ocultar_celdas(matriz) -> Matriz lista para jugar al Sudoku 
    """
    matriz = inicializar_matriz(9, 9, 0)
    generar_sudoku(matriz)
    mostrar_sudoku(matriz)
    return ocultar_celdas(matriz)

def verificar_victoria(estado_juego):
    bandera = True
    for fila in range(9):
        for columna in range(9):
            if estado_juego['sudoku'][fila][columna] != estado_juego['solucion'][fila][columna]:
                bandera = False
                break
    return bandera