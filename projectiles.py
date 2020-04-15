import pygame, math
pygame.init()

# bullet class
class projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,height, width, facing, XorY, velocityX, velocityY):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.velX = velocityX
        self.velY = velocityY
        self.XorY = XorY

        self.image = pygame.image.load('art/topdown_shooter/other/bulletb.png')

    def draw(self, win, coords):
        # working out the angle to rotate the bullet
        if self.velX == 0:
            if self.velY > 0:
                self.angle = 270
            else:
                self.angle = 90
        elif self.velY == 0:
            if self.velX > 0:
                self.angle = 0
            else:
                self.angle = 180
        else:
            self.angle = int(math.degrees(math.atan2(self.velY,self.velX)))
        
        pygame.draw.rect(win, (0,0,255), self.rect)
        win.blit(pygame.transform.rotate(self.image, self.angle), coords)
            

