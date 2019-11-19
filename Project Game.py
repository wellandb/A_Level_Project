# import pygame
import pygame, sys, random

restart = True
while restart:
    restart = False

    from settings import *
    from map_maker import *
    from player import *
    from enemies import *
    from projectiles import *
    from collisions import *
    print('all imported')

    # camera class
    class camera():
        def __init__(self, width, height):
            self.rect = pygame.Rect( 0, 0, width, height)
            self.width = width
            self.height = height

    # returns position relative to camera
        def apply(self, entity):
            return entity.rect.move(self.rect.topleft)

    # updates camera position so that target is in middle of camera
        def update(self, target):
            x = -target.rect.x + int(screenWidth/2)
            y =  -target.rect.y + int(screenHeight/2)
            self.rect = pygame.Rect(x, y, self.width, self.height)


    # game over variable
    gameOver = False

    # game win variable
    gameWin = False

    #intialise objects
    all_sprite_list = pygame.sprite.Group()

    Camera = camera(screenWidth, screenHeight)

    score = 1000

 #enemies
    enemies = pygame.sprite.Group()

    # choosing spawn point that is far away enough from all enemies that you don't die staright away
    print('start spawning')
    spawn = False
    enemiesSpawn = True
    while not spawn:
        # enemy spawning
        if enemiesSpawn:
            for i in range(20):
                tileSpawn = floor[random.randint(0,len(floor) - 1)]
                enemyX = tileSpawn.rect.x + tileSize/4
                enemyY = tileSpawn.rect.y + tileSize/4
                newEnemy = enemy(enemyX,enemyY, 16, 23)
                enemies.add(newEnemy)
                enemiesSpawn = False
                countDownToEnemies = 10

        # player spawning
        canSpawn = True
        playerTileSpawn = floor[random.randint(0,len(floor) - 1)]
        for Enemy in enemies:
            #check if player spawn is too close to an enemy in the x axis
            if playerTileSpawn.rect.x - (5 * tileSize) < Enemy.rect.x and playerTileSpawn.rect.x + (5 * tileSize) > Enemy.rect.x:
                #check if player spawn is too close to an enemy in the y axis
                if playerTileSpawn.rect.y - (5 * tileSize) < Enemy.rect.y and playerTileSpawn.rect.y + (5 * tileSize) > Enemy.rect.y:
                    canSpawn = False

        if canSpawn:
            #enemies spawn
            for i in enemies:
                all_sprite_list.add(i)
            #player spawn
            playerX = playerTileSpawn.rect.x + tileSize/4
            playerY = playerTileSpawn.rect.y + tileSize/4
            man = player(playerX, playerY , 16, 20)
            all_sprite_list.add(man)
            spawn = True
        else:
            countDownToEnemies -= 1
            if countDownToEnemies == 0:
                enemiesSpawn = True
                enemies = pygame.sprite.Group()

    print('finished spawning')
    #projectiles
    bullets = pygame.sprite.Group()

    # draw game function
    def redrawGameWindow():
        
        Camera.update(man)
        for tile in floor:
            tile.draw(win, Camera.apply(tile))
        for wall in walls:
            wall.draw(win, Camera.apply(wall))
        for sprite in all_sprite_list:    
            sprite.draw(win, Camera.apply(sprite))
        for Enemy in enemies:
            Enemy.move(man)

        if gameOver:
            win.blit(myfont.render('Game Over', True, white), (screenWidth/2 - 125, 50))
            win.blit(myfont.render('Space to restart',True, white), (screenWidth/2-200, 150))
        if gameWin:
            win.blit(myfont.render('Game Win', True, white), (screenWidth/2 - 125, 50))
            win.blit(myfont.render('Space to restart',True, white), (screenWidth/2-200, 150))

        if score > 0:
            win.blit(smallfont.render('score:' + str(score), True, white), (screenWidth - 100, 20))
        else:
            win.blit(smallfont.render('score:' + str(score), True, red), (screenWidth - 100, 20))

        #display update window
        pygame.display.update()
    # fill window with black background
        win.fill(black)

    #main loop
    print('game loop started')
    run = True
    while run:
        # set clock
        clock.tick(30)

        #event loop
        for event in pygame.event.get():
            # bomb out of loop if quit
            if event.type == pygame.QUIT:
                run = False
        
        # check if there are no enemies
        if enemies.__len__() == 0:
            gameWin = True
            run = False
        
        # bullets
        for bullet in bullets:
            if bullet.movingX:
                if bullet.rect.x < screenWidth/2 + man.rect.x and bullet.rect.x > man.rect.x - screenWidth/2:
                    bullet.rect.x += bullet.vel
                else:
                    bullets.remove(bullet)
                    all_sprite_list.remove(bullet)
            
            # changes bullet dimensions
            if bullet.movingY:
                if bullet.rect.y < man.rect.y + screenHeight/2 and bullet.rect.y > man.rect.y - screenHeight/2:
                    bullet.rect.y += bullet.vel
                else:
                    bullets.remove(bullet)
                    all_sprite_list.remove(bullet)
            
            bulletCollisions(bullets, bullet, enemies, all_sprite_list, walls)

        enemyCollisions(enemies, walls)

        # enemy-player collisions
        for Enemy in enemies:
            if pygame.sprite.collide_rect(Enemy, man):
                gameOver = True
                run = False
        
                    

        # key press events
        keys = pygame.key.get_pressed()

        #shooting
        if keys[pygame.K_SPACE]:
            man.shoot(bullets, projectile, all_sprite_list)
            

        # movement key presses with facing direction for shooting
        man.moving = False
        if keys[pygame.K_UP]:
            moveUp = True
            for wall in walls:
                if man.rect.x >= wall.rect.x and man.rect.x < wall.rect.x + tileSize or man.rect.x <= wall.rect.x and man.rect.x + man.rect.width > wall.rect.x:
                    if man.rect.y - man.vel < wall.rect.y + tileSize and man.rect.y >= wall.rect.y:
                        moveUp = False
            if moveUp:
                man.rect.y -= man.vel
            man.up = True
            man.left = False
            man.right = False
            man.down = False
            man.moving = True

        if keys[pygame.K_DOWN]:
            moveDown = True
            for wall in walls:
                if man.rect.x >= wall.rect.x and man.rect.x < wall.rect.x + tileSize or man.rect.x <= wall.rect.x and man.rect.x + man.rect.width > wall.rect.x:
                    if man.rect.y + man.rect.height + man.vel > wall.rect.y and man.rect.y + man.rect.height <= wall.rect.y:
                        moveDown = False
            if moveDown:
                man.rect.y += man.vel
            man.up = False
            man.left = False
            man.down = True
            man.right = False
            man.moving = True

        if keys[pygame.K_LEFT]:
            moveLeft = True
            for wall in walls:
                if man.rect.y >= wall.rect.y and man.rect.y < wall.rect.y + tileSize or man.rect.y <= wall.rect.y and man.rect.y + man.rect.height > wall.rect.y:
                    if man.rect.x - man.vel < wall.rect.x + tileSize and man.rect.x >= wall.rect.x + tileSize:
                        moveLeft = False
            if moveLeft:
                man.rect.x -= man.vel
            man.left = True
            man.down = False
            man.right = False
            man.up = False
            man.moving = True

        if keys[pygame.K_RIGHT]:
            moveRight = True
            for wall in walls:
                if man.rect.y >= wall.rect.y and man.rect.y < wall.rect.y + tileSize or man.rect.y <= wall.rect.y and man.rect.y + man.rect.height > wall.rect.y:
                    if man.rect.x + man.rect.width + man.vel > wall.rect.x and man.rect.x + man.rect.width <= wall.rect.x:
                        moveRight = False
            if moveRight:
                man.rect.x += man.vel
            man.left = False
            man.up = False
            man.down = False
            man.right = True
            man.moving = True


        if score > 0:
            score -= 1

        # display loop updates
        redrawGameWindow()

    # another loop to pause the screen once dead so player can look at the game over screen before quiting
    while not run:

        clock.tick(60)

        #event loop
        for event in pygame.event.get():
            # bomb out of loop if quit
            if event.type == pygame.QUIT:
                run = True


            keys = pygame.key.get_pressed() 
            if keys[pygame.K_SPACE]:
                restart = True
                run = True

#quit program
pygame.quit()