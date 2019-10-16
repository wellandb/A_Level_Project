import pygame
pygame.init()

# bullet collisions:
def bulletCollisions(bullets, bullet, enemies, all_sprite_list, walls):
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

    #bullet-wall collisions
    for wall in walls:
        if pygame.sprite.collide_rect(bullet, wall):
            bullets.remove(bullet)
            all_sprite_list.remove(bullet)

# enemy collisions
def enemyCollisions(enemies, man, gameOver, run, walls):

    # enemy-player collisions
    for enemy in enemies:
        if pygame.sprite.collide_rect(enemy, man):
            gameOver = True
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
                    enemy1.rect.x -= 2
                    enemy2.rect.x += 2
                #if enemy2 hits to the left of enemy1
                if enemy1.rect.x - enemy2.rect.width <= enemy2.rect.x and enemy1.rect.x > enemy2.rect.x:
                    enemy1.rect.x += 2
                    enemy2.rect.x -= 2
                #if enemy2 hits from ontop of enemy1
                if enemy1.rect.y <= enemy2.rect.y + enemy2.rect.height and enemy1.rect.y > enemy2.rect.y:
                    enemy1.rect.y += 2
                    enemy2.rect.y -= 2
                #if enemy2 hits from below enemy1
                if enemy1.rect.y >= enemy2.rect.y - enemy1.rect.height and enemy1.rect.y < enemy2.rect.y:
                    enemy1.rect.y -= 2
                    enemy2.rect.y += 2
                


    #enemy-wall collisions
    for enemy in enemies:
        for wall in walls:
            if pygame.sprite.collide_rect(enemy, wall):               
                enemy.canMove = False
                #bounce away mechanics
                #if enemy hits to the right of wall
                if wall.rect.x >= enemy.rect.x - wall.rect.width and wall.rect.x < enemy.rect.x:
                    enemy.rect.x += 3
                #if enemy hits to the left of wall
                if wall.rect.x - enemy.rect.width <= enemy.rect.x and wall.rect.x > enemy.rect.x:
                    enemy.rect.x -= 3
                #if enemy hits from ontop of wall
                if wall.rect.y <= enemy.rect.y + enemy.rect.height and wall.rect.y > enemy.rect.y:
                    enemy.rect.y -= 3
                #if enemy hits from below wall
                if wall.rect.y >= enemy.rect.y - wall.rect.height and wall.rect.y < enemy.rect.y:
                    enemy.rect.y += 3


#player-wall collisions
#    for wall in walls:
#        if pygame.sprite.collide_rect(man,wall):
            #if player is to the right
 #           if wall.rect.x >= man.rect.x - wall.rect.width and wall.rect.x < man.rect.x:
  #              man.rect.x += (man.vel + 1)
                # if the player is to the left
   #         if wall.rect.x <= man.rect.x + man.rect.width and wall.rect.x > man.rect.x:
    #            man.rect.x -= (man.vel + 1)
            #if the player is below the wall
     #       if wall.rect.y >= man.rect.y - wall.rect.height and wall.rect.y < man.rect.y:
      #          man.rect.y += (man.vel + 1)
            # if the player is above the wall
       #     if wall.rect.y <= man.rect.y + man.rect.height and wall.rect.y > man.rect.y:
        #        man.rect.y += (man.vel + 1)
       