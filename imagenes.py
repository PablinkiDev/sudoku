import pygame

def cargar_imagen(ruta:str, dimensiones:int|None = None):
    """
    Esta funcion se encarga de cargar una imagen.
    Recibe: ruta(str): Directorio de la imagen.
            dimensiones(int|None): Dimensiones a la que se va escalar la imagen.
            Por defecto es None.
    Retorna: La imagen cargada con pygame.
    """
    imagen = pygame.image.load(ruta)
    if dimensiones != None:
        imagen = pygame.transform.scale(imagen, dimensiones)
    return imagen
    

reset = cargar_imagen("img/reset.webp", (80, 80))
volver = cargar_imagen("img/volver.png", (80, 80))
error = cargar_imagen("img/error.png", (70, 70))

reset_rect = reset.get_rect()
reset_rect.topleft = (1100, 100) 


volver_rect = volver.get_rect()
volver_rect.topleft = (1100, 550)


DICCIONARIO_IMAGENES = [
    {
        "nombre": "reset",
        "surface": reset,
        "surface_rect": reset_rect,
        "url": "img/reset.webp",
        "posicion_x": 1100,
        "posicion_y": 100,
    },
    {
        "nombre": "volver",
        "surface": volver,
        "surface_rect": volver_rect,
        "url": "img/volver.png",
        "posicion_x": 1100,
        "posicion_y": 550,
    },
    {
        "nombre": "error",
        "surface": error,
        "surface_rect": None,
        "url": "img/error.png",
        "posicion_x": 500,
        "posicion_y": 20,
    }, 
]