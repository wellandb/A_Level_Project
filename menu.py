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
    win.blit(pygame.image.load('art/robot_background.jpg'), (screenWidth/2 - 225, 100))
    win.blit(myfont.render('To Play press Space', True, white), (screenWidth/2 - 220, 100))
    win.blit(smallfont.render('Shooting: Hold down Space', True, white), (screenWidth* 3/4, 200))
    win.blit(smallfont.render('Movement: Arrow keys', True, white), (screenWidth* 3/4, 250))
    win.blit(smallfont.render('Guns: 1 for pistol, 2 for shotgun', True, white), (screenWidth* 3/4, 300))

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE]:
        menu = False

    
    #event loop
    for event in pygame.event.get():
        # bomb out of loop if quit
        if event.type == pygame.QUIT:
            run = False
            menu = False

    pygame.display.update()