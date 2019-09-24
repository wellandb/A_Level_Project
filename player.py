import pygame
pygame.init()
#player class
class player(pygame.sprite.Sprite):
    #initialisation
    def __init__ (self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = True
        self.reloadTime = 0

     #draw function
    def draw(self,win):
        pygame.draw.rect(win, (255, 0, 0), self.rect)

    def shoot(self, bullets, projectile):
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
           bullets.add(projectile(round(self.rect.x + self.rect.width//4),  round(self.rect.y + self.rect.height//4), 6, 10, (0,0,255), facing, XorY, 10))
           self.reloadTime = 1
        else:
            self.reloadTime = 0