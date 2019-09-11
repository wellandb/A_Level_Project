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

rows, cols = (175, 125)
grid = [['wall' for i in range(rows)] for j in range(cols)]


#walker to build floor
class walker():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,40,40)
        self.direction = random.randint(1,5)
        self.alive = True

    #movement
    def move(self):
        #check if alive
        if self.alive:
            #chance to die
            self.death()
            #random direction
            if self.direction == 1 and self.rect.y > 40:
                self.rect.y -= 40
            elif self.direction == 2 and self.rect.x < 6960:
                self.rect.x += 40
            elif self.direction == 3 and self.rect.y < 4960:
                self.rect.y += 40
            elif self.direction == 4 and self.rect.x > 40:
                self.rect.x -= 40
            #create floor
            if grid[int(self.rect.x/40)][int(self.rect.y/40)] == 'wall':
                floor.append(floorTile(self.rect.x, self.rect.y))
                grid[int(self.rect.x/40)][int(self.rect.y/40)] = 'floor'
                print('wassup')
            self.direction = random.randint(1,5)
    

    #chance death
    def death(self):
        die = random.randint(1,1001)
        if die == 69:
            self.alive = False

#floor tile
class floorTile(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,40)

    def draw(self):
        pygame.draw.rect(win,(255,0,0), self.rect)
    
#wall tile
class wallTile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,40)

    def draw(self):
        pygame.draw.rect(win, (0,255,0), self.rect)


#lists to store floor
floor = []
walls = []
tiles = []
walkers = []


for i in range(1,11):
    walkers.append(walker(360,200))

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
    if len(floor) == 500:
        for walker in walkers:
            walker.alive = False
        print('ayo')


    pygame.display.update()
 
pygame.quit()