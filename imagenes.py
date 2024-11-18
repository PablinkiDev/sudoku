import pygame

reset = pygame.image.load("img/reset.webp")
reset = pygame.transform.scale(reset, (80, 80))
reset_rect = reset.get_rect()
reset_rect.topleft = (1100, 100) 

volver = pygame.image.load("img/volver.png")
volver = pygame.transform.scale(volver, (80, 80))
volver_rect = volver.get_rect()
volver_rect.topleft = (1100, 550)
    
error = pygame.image.load("img/error.png")
error = pygame.transform.scale(error, (70, 70))



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