import pygame, math, random
pygame.init()

# pistol
def pistol(bullets, projectile, man, facing, XorY, all_sprite_list):
    # max 5 bullets on screen at a time, makes bullet at centre of player and moves in direction facing, also adds delay between bullets
    if len(bullets) < 5:
        if XorY == 'X':
            if man.right:
                bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 6, 10, facing, XorY, 10, 0)
            else:
                bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 6, 10, facing, XorY, -10, 0)
        else:
            if man.down:
                bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 10, 6, facing, XorY, 0, 10)
            else:
                bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 10, 6, facing, XorY, 0, -10)
                
      
        bullets.add(bullet)
        all_sprite_list.add(bullet)

def shotgun(bullets, projectile, man, facing, XorY, all_sprite_list):
    if len(bullets) < 15:
        for i in range(5):
            if XorY == 'X':
                if man.right:
                    bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 6, 10, facing, XorY, 10, random.randint(-5, 5))
                else:
                    bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 6, 10, facing, XorY, -10, random.randint(-5, 5))
            else:
                if man.down:
                    bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 10, 6, facing, XorY, random.randint(-5, 5), 10)
                else:
                    bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 10, 6, facing, XorY, random.randint(-5, 5), -10)
   
            bullets.add(bullet)
            all_sprite_list.add(bullet)