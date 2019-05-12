#import pygame and random generator
import pygame, random

pygame.init()

pygame.display.set_caption('Map generation')

clock = pygame.time.Clock()

screenWidth = 700
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill((0,0,0))

#walker to build floor
class walker():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,5,5)
        self.direction = random.randint(1,5)
        self.alive = True

    #movement
    def move(self):
        #check if alive
        if self.alive:
            #chance to die
            self.death()
            #random direction
            if self.direction == 1 and self.rect.y > 5:
                self.rect.y -= 5
            elif self.direction == 2 and self.rect.x < screenWidth - 5:
                self.rect.x += 5
            elif self.direction == 3 and self.rect.y < screenHeight - 5:
                self.rect.y += 5
            elif self.direction == 4 and self.rect.x > 5:
                self.rect.x -= 5
            #create floor
            floor.append(floorTile(self.rect.x,self.rect.y))
            self.direction = random.randint(1,5)
    
    #chance death
    def death(self):
        die = random.randint(1,1001)
        if die == 69:
            self.alive = False

#floor tile
class floorTile(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,5,5)

    def draw(self):
        pygame.draw.rect(win,(255,0,0), (self.rect.x, self.rect.y, 5, 5))
    
#wall tile
class wallTile(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,5,5)
             
#lists to store floor
floor = []
walls = []
walkers = []
for i in range(1,6):
    walkers.append(walker(350,250))

run = True
while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for walker in walkers:
        walker.move()
    for tiles in floor:
        tiles.draw()
    if len(floor) >= 1000:
        for walker in walkers:
            walker.alive = False            

    
    pygame.display.update()

    

pygame.quit()