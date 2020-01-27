import pygame, sys
pygame.init()

from settings import *

menu = True
while menu:
    # set clock
    clock.tick(30)

    #event loop
    for event in pygame.event.get():
        # bomb out of loop if quit
        if event.type == pygame.QUIT:
            menu = False

    win.fill(black)
    win.blit(myfont.render('To Play press Space', True, white), (screenWidth/2 - 220, 200))

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE]:
        menu = False

    pygame.display.update()