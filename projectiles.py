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
            temp = self.rect.width
            self.rect.width = self.rect.height
            self.rect.height = temp
            
        self.image = pygame.image.load('art/topdown_shooter/other/bulletb.png')

    def draw(self, win, coords):
        if self.vel > 0 and self.movingX:
            win.blit(self.image, coords)
        elif self.vel < 0 and self.movingX:
            win.blit(pygame.transform.flip(self.image, 1,0),coords)
        elif self.vel > 0:
            win.blit(pygame.transform.rotate(self.image, 270),coords)
        else:
            win.blit(pygame.transform.rotate(self.image, 90),coords)


            

