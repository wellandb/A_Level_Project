from settings import *


tileSize = 40
rows, cols = (175, 125)
grid = [['wall' for i in range(rows)] for j in range(cols)]


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
            if grid[int(self.rect.y/tileSize)][int(self.rect.x/tileSize)] == 'wall':
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

    def draw(self):
        pygame.draw.rect(win,(255,0,0), self.rect)
    
#wall tile
class wallTile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,tileSize,tileSize)

    def draw(self):
        pygame.draw.rect(win, (0,255,0), self.rect)


#lists to store floor
floor = []
walls = []
tiles = []
walkers = []
once = True

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
    for tiles in floor:
        tiles.draw()
    for wall in walls:
        wall.draw
    if len(floor) == 500:
        for walker in walkers:
            walker.alive = False
        print('ayo')
        if once:
            for i in range(cols):
                for j in range(rows):
                    if grid[i][j] == 'wall':
                        walls.append(wallTile(j*tileSize, i*tileSize))
                        print('wall instatiated')
            once = False


    pygame.display.update()
 
pygame.quit()