import pygame
pygame.init()
#player class
class player(pygame.sprite.Sprite):
    #initialisation
    def __init__ (self, x, y, width, height):
        # gives initialisation of a pygame sprite
        super().__init__()
        # creates hit box
        self.rect = pygame.Rect(x, y, width, height)
        # creates speed of player
        self.vel = 5
        # creates way of facing for shooting
        self.left = False
        self.right = False
        self.up = False
        self.down = True
        # allows for instant shooting
        self.reloadTime = 0

     #draw function
    def draw(self,win, coords):
        # at the moment the player is just a red rectangle
        pygame.draw.rect(win, (255, 0, 0), coords)

    def shoot(self, bullets, projectile, all_sprite_list):
        # determines which way facing
        if self.left or self.up:
            facing = -1
        else:
            facing = 1
        if self.left or self.right:
            XorY = "X"
        else:
            XorY = "Y"
        # max 5 bullets on screen at a time, makes bullet at centre of player and moves in direction facing, also adds delay between bullets
        if len(bullets) < 5 and self.reloadTime == 0:
           bullet = projectile(round(self.rect.x + self.rect.width//4),  round(self.rect.y + self.rect.height//4), 6, 10, (0,0,255), facing, XorY, 10)
           bullets.add(bullet)
           all_sprite_list.add(bullet)
           self.reloadTime = 1
        else:
            self.reloadTime = 0