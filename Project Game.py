# import pygame
import pygame, sys, random

from settings import *
from map_maker import *
from player import *
from enemies import *
from projectiles import *

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


# game over function
def gameOver():
    win.blit(myfont.render('Game Over', True, white), (screenWidth/2 - 125, 50))

# game win funtion
def gameWin():
    win.blit(myfont.render('Game Win', True, white), (screenWidth/2 - 125, 50))

#intialise objects
all_sprite_list = pygame.sprite.Group()

Camera = camera(screenWidth, screenHeight)

# player
man = player(3800, 2500, 20, 20)
all_sprite_list.add(man)

#enemies
enemies = pygame.sprite.Group()
for i in range(10):
    i = enemy(random.randint(3540 , 3540 + screenWidth -30),random.randint(2360, 2360 + screenHeight/2), 20, 20)
    enemies.add(i)
    all_sprite_list.add(i)

#projectiles
bullets = pygame.sprite.Group()

# draw game function
def redrawGameWindow():
    
    Camera.update(man)
    for sprite in all_sprite_list:    
        sprite.draw(win, Camera.apply(sprite))
    for enemy in enemies:
        enemy.move(man)
    for tile in floor:
        tile.draw(win, Camera.apply(tile))
    for wall in walls:
        wall.draw(win, Camera.apply(tile))
#        win.blit(sprite.image, Camera.apply(sprite))

    #display update window
    pygame.display.update()
   # fill window with black background
    win.fill(black)

#main loop
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
        gameWin()
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
       
       # bullet-enemy collisions
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemies, False)
        for enemy in enemy_hit_list:
            bullets.remove(bullet)
            all_sprite_list.remove(bullet)
            if bullet.movingX:
                if bullet.vel > 0:
                    enemy.rect.x += 3
                else:
                    enemy.rect.x -= 3
            else:         
                if bullet.vel > 0:
                    enemy.rect.y += 3
                else:
                    enemy.rect.y -= 3                
            enemy.shot(enemies, all_sprite_list, enemy_hit_list)

    # enemy-player collisions
    for enemy in enemies:
        if pygame.sprite.collide_rect(enemy, man):
            gameOver()
            run = False

    # enemy-enemy collisions
    for enemy1 in enemies:
        enemies2 = enemies.copy()
        enemies2.remove_internal(enemy1)
        for enemy2 in enemies2:
            if pygame.sprite.collide_rect(enemy1, enemy2):
                enemy1.canMove = False
                #bounce away mechanics
                #if enemy2 hits to the right of enemy1
                if enemy1.rect.x >= enemy2.rect.x - enemy1.rect.width and enemy1.rect.x < enemy2.rect.x:
                    enemy1.rect.x -= 3
                    enemy2.rect.x += 3
                #if enemy2 hits to the left of enemy1
                if enemy1.rect.x - enemy2.rect.width <= enemy2.rect.x and enemy1.rect.x > enemy2.rect.x:
                    enemy1.rect.x += 3
                    enemy2.rect.x -= 3
                #if enemy2 hits from ontop of enemy1
                if enemy1.rect.y <= enemy2.rect.y + enemy2.rect.height and enemy1.rect.y > enemy2.rect.y:
                    enemy1.rect.y += 3
                    enemy2.rect.y -= 3
                #if enemy2 hits from below enemy1
                if enemy1.rect.y >= enemy2.rect.y - enemy1.rect.height and enemy1.rect.y < enemy2.rect.y:
                    enemy1.rect.y -= 3
                    enemy2.rect.y += 3
                

    # key press events
    keys = pygame.key.get_pressed()

    #shooting
    if keys[pygame.K_SPACE]:
        man.shoot(bullets, projectile, all_sprite_list)
        

    # movement key presses with facing direction for shooting
    if keys[pygame.K_UP]:
        man.rect.y -= man.vel
        man.up = True
        man.left = False
        man.right = False
        man.down = False
    elif keys[pygame.K_DOWN]:
        man.rect.y += man.vel
        man.up = False
        man.left = False
        man.down = True
        man.right = False
    elif keys[pygame.K_LEFT]:
        man.rect.x -= man.vel
        man.left = True
        man.down = False
        man.right = False
        man.up = False
    elif keys[pygame.K_RIGHT]:
        man.rect.x += man.vel
        man.left = False
        man.up = False
        man.down = False
        man.right = True

    # display loop updates
    redrawGameWindow()

while not run:

    clock.tick(30)

    #event loop
    for event in pygame.event.get():
        # bomb out of loop if quit
        if event.type == pygame.QUIT:
            run = True

#quit program
pygame.quit()