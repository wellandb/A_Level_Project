import pygame
pygame.init()

# pistol
def pistol(bullets, projectile, man, facing, XorY, all_sprite_list):
    # max 5 bullets on screen at a time, makes bullet at centre of player and moves in direction facing, also adds delay between bullets
    if len(bullets) < 5:
       bullet = projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 6, 10, (0,0,255), facing, XorY, 10)
       bullets.add(bullet)
       all_sprite_list.add(bullet)