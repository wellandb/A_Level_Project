import pygame
pygame.init()
# bullet class
class projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,height, width,colour,facing, XorY, velocity):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.colour = colour
        self.vel = velocity * facing
        if XorY == "X":
            self.movingX = True
            self.movingY = False
        else:
            self.movingY = True
            self.movingX = False

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)
