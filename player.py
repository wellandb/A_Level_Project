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
        self.gun = 'shotgun'
        self.idle = pygame.image.load('art/topdown_shooter/characters/idle.png')
        self.walkRight = [pygame.image.load('art/topdown_shooter/characters/right0.png'), pygame.image.load('art/topdown_shooter/characters/right1.png'), pygame.image.load('art/topdown_shooter/characters/right2.png'), pygame.image.load('art/topdown_shooter/characters/right3.png')]
        self.walkLeft = [pygame.image.load('art/topdown_shooter/characters/left0.png'), pygame.image.load('art/topdown_shooter/characters/left1.png'), pygame.image.load('art/topdown_shooter/characters/left2.png'), pygame.image.load('art/topdown_shooter/characters/left3.png')]
        self.walkDown = [pygame.image.load('art/topdown_shooter/characters/down0.png'),pygame.image.load('art/topdown_shooter/characters/down1.png'),pygame.image.load('art/topdown_shooter/characters/down2.png'),pygame.image.load('art/topdown_shooter/characters/down3.png')]
        self.walkUp = [pygame.image.load('art/topdown_shooter/characters/up0.png'),pygame.image.load('art/topdown_shooter/characters/up1.png'),pygame.image.load('art/topdown_shooter/characters/up2.png'),pygame.image.load('art/topdown_shooter/characters/up3.png')]
        self.walkCount = 0
        self.moving = False

     #draw function
    def draw(self,win, coords):
        if self.walkCount >= 12:
            self.walkCount = 0
        if self.moving == False:
            if self.right:
                self.image = self.walkRight[2]
            if self.left:
                self.image = self.walkLeft[2]
            if self.down:
                self.image = self.idle
            if self.up:
                self.image = self.walkUp[2]
        else:
            if self.right:
                self.image = self.walkRight[self.walkCount//3]
            if self.left:
                self.image = self.walkLeft[self.walkCount//3]
            if self.down:
                self.image = self.walkDown[self.walkCount//3]
            if self.up:
                self.image = self.walkUp[self.walkCount//3]
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
        
        if self.gun == 'shotgun':
            if self.reloadTime == 0:
                shotgun(bullets, projectile, self, facing, XorY, all_sprite_list)
                self.reloadTime = 6
            else:
                self.reloadTime -= 1
