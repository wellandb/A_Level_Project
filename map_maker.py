#import pygame and random generator
import pygame, random, sys
# initialise pygame
pygame.init()

tileSize = 40
rows, cols = (175, 125)
grid = [['' for i in range(rows)] for j in range(cols)]


#walker to build floor
class walker():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,tileSize,tileSize)
        self.direction = random.randint(1,5)
        self.alive = True

    #movement
    def move(self):
        #check if alive
        if self.alive:
            #chance to die
            self.death()
            #random direction
            if self.direction == 1 and self.rect.y > tileSize:
                self.rect.y -= tileSize
            elif self.direction == 2 and self.rect.x < (rows - 1) * tileSize:
                self.rect.x += tileSize
            elif self.direction == 3 and self.rect.y < (cols - 1) * tileSize:
                self.rect.y += tileSize
            elif self.direction == 4 and self.rect.x > tileSize:
                self.rect.x -= tileSize
            #create floor
            if grid[int(self.rect.y/tileSize)][int(self.rect.x/tileSize)] == '':
                floor.append(floorTile(self.rect.x, self.rect.y))
                grid[int(self.rect.y/tileSize)][int(self.rect.x/tileSize)] = 'floor'
            self.direction = random.randint(1,5)
    

    #chance death
    def death(self):
        die = random.randint(1,1001)
        if die == 69:
            self.alive = False

#floor tile
class floorTile(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,tileSize,tileSize)

    def draw(self, win , coords):
        pygame.draw.rect(win,(125,125,255), coords)
    
#wall tile
class wallTile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,tileSize,tileSize)

    def draw(self, win, coords):
        pygame.draw.rect(win, (255,162,162), coords)


#lists to store floor
floor = []
walls = []
tiles = []
walkers = []
once = True

# setting up clock
clock = pygame.time.Clock()

for i in range(1,11):
    walkers.append(walker(3600,2400))

run = True
while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for walker in walkers:
        walker.move()

    percentDone = int((len(floor)/250) * 100)
    print(percentDone, '%')

    if len(floor) > 250:
        for walker in walkers:
            walker.alive = False
        if once:
            for i in range(cols):
                for j in range(rows):
                    if grid[i][j] == 'floor':
                        if i > 0:
                            if grid[i-1][j] == '':
                                grid[i-1][j] = 'wall'
                                walls.append(wallTile(j*tileSize, (i-1)*tileSize))
                        if i > 0 and j > 0:
                            if grid[i-1][j-1] == '':
                                grid[i-1][j-1] = 'wall'
                                walls.append(wallTile((j-1)*tileSize, (i-1)*tileSize))
                        if i > 0 and j < rows:
                            if grid[i-1][j+1] == '':
                                grid[i-1][j+1] = 'wall'
                                walls.append(wallTile((j+1)*tileSize, (i-1)*tileSize))
                        if j > 0:
                            if grid[i][j-1] == '':
                                grid[i][j -1] = 'wall'
                                walls.append(wallTile((j-1)*tileSize, (i)*tileSize))
                        if j < rows:
                            if grid[i][j+1] == '':
                                grid[i][j+1] = 'wall'
                                walls.append(wallTile((j+1)*tileSize, (i)*tileSize))
                        if i < cols:
                            if grid[i+1][j] == '':
                                grid[i+1][j] = 'wall'
                                walls.append(wallTile((j)*tileSize, (i+1)*tileSize))
                        if i < cols and j > 0:
                            if grid[i+1][j-1] == '':
                                grid[i+1][j-1] = 'wall'
                                walls.append(wallTile((j-1)*tileSize, (i+1)*tileSize))
                        if i < cols and j < rows:
                            if grid[i+1][j+1] == '':
                                grid[i+1][j+1] = 'wall'
                                walls.append(wallTile((j+1)*tileSize, (i+1)*tileSize))
            once = False
                                        
            run = False


    pygame.display.update()