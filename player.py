import pygame
pygame.init()

from guns import * 


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
        self.gun = 'pistol'
        self.idle = [pygame.image.load('art\knight_m_idle_anim_f0.png'),pygame.image.load('art\knight_m_idle_anim_f1.png'),pygame.image.load('art\knight_m_idle_anim_f2.png'),pygame.image.load('art\knight_m_idle_anim_f3.png')]
        self.walkRight = [pygame.image.load('art\knight_m_run_anim_f0.png'),pygame.image.load('art\knight_m_run_anim_f1.png'),pygame.image.load('art\knight_m_run_anim_f2.png'),pygame.image.load('art\knight_m_run_anim_f3.png')]
        self.walkCount = 0
        self.moving = False

     #draw function
    def draw(self,win, coords):
        if self.walkCount >= 12:
            self.walkCount = 0
        if self.moving == False:
            self.image = self.idle[self.walkCount//3]
        else:
            self.image = self.walkRight[self.walkCount//3]
        self.walkCount += 1
        win.blit(self.image,coords)

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

        if self.gun == 'pistol':
            if self.reloadTime == 0:    
                pistol(bullets, projectile, self, facing, XorY, all_sprite_list)
                self.reloadTime = 2
            else:
                self.reloadTime -= 1
