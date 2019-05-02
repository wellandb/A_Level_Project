import pygame, random

pygame.init()

pygame.display.set_caption('Map generation')

clock = pygame.time.Clock()

screenWidth = 700
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill((0,0,0))


def redrawGameWindow():
    pygame.display.update()

class LevelGenerator():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.randint(1,5)
        self.alive = True

    def move():
        if self.alive:
#            self.death()
            if self.direction == 1:
                self.y -= 1
            elif self.direction == 2:
                self.x += 1
            elif self.direction == 3:
                self.y += 1
            elif self.direction == 4:
                self.x -= 1
 #           pygame.draw.rect(win,(255,0,0), (self.x, self.y, 1,1))
            self.direction = random.randint(1,5)
    
    def death():
        die = random.randint(1,101)
        if die == 69:
            self.alive = False



walker = LevelGenerator(350,250)

run = True
while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    walker.move()
    redrawGameWindow()

    

pygame.quit()