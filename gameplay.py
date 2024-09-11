import pygame

ANCHO=1000
ALTO=600
VENTANA= pygame.display.set_mode([ANCHO, ALTO])

Jugando=True

while Jugando:
    eventos=pygame.event.get()
    for event in eventos:
        if event.type==pygame.QUIT:
            Jugando=False
    pygame.display.update()
quit()

