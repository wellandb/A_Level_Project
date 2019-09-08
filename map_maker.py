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

grid = [["wall" * 350] * 250]


#walker to build floor
class walker():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,20,20)
        self.direction = random.randint(1,5)
        self.alive = True

    #movement
    def move(self):
        #check if alive
        if self.alive:
            #chance to die
            self.death()
            #random direction
            if self.direction == 1 and self.rect.y > 20:
                self.rect.y -= 20
            elif self.direction == 2 and self.rect.x < 6980:
                self.rect.x += 20
            elif self.direction == 3 and self.rect.y < 4980:
                self.rect.y += 20
            elif self.direction == 4 and self.rect.x > 20:
                self.rect.x -= 20
            #create floor
            if grid[int(self.rect.x/20)][int(self.rect.y/20)] == 'wall':
                floor.append(floorTile(self.rect.x, self.rect.y))
                grid[self.rect.x/20][self.rect.y/20] = 'floor'
            self.direction = random.randint(1,5)
    

    #chance death
    def death(self):
        die = random.randint(1,1001)
        if die == 69:
            self.alive = False

#floor tile
class floorTile(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,20,20)

    def draw(self):
        pygame.draw.rect(win,(255,0,0), self.rect)
    
#wall tile
class wallTile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,20,20)

             
#lists to store floor
floor = []
walls = []
tiles = []
walkers = []


for i in range(1,6):
    walkers.append(walker(3500,2500))


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