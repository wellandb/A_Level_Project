# import pygame
import pygame, sys

# initalise pygame
pygame.init() 

# intialise some colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0,0,0)

# setting a caption for game window
pygame.display.set_caption('Game Project')

# setting up clock
clock = pygame.time.Clock()

# classes
#player class
class player(pygame.sprite.Sprite):
    #initialisation
    def __init__ (self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

     #draw function
    def draw(self,win):
        pygame.draw.rect(win, red, (self.x, self.y, self.width, self.height))
   
# bullet class
class projectile(object):
    def __init__(self,x,y,radius,colour,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)

# enemy class
class enemy(object):

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.end = end
        self.path = [self.x, self.end]

    def draw(self,win):
        self.move()
        pygame.draw.rect(win, green, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.vel > 0:
            if self.x +self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel

            else:
                self.vel = self.vel * -1
        pass
     
#intialise objects
man = player(250,350, 20, 20)
evil = enemy(200, 250, 20, 20, 500)
bullets = []
screenWidth = 700
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)


# draw game function
def redrawGameWindow() :

    man.draw(win)
    evil.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
   # fill window with black background
    win.fill(black)

#main loop
run = True
while run:

    # set clock
    clock.tick(30)

    #event loop
    for event in pygame.event.get():
        # bomb out of loop if quit
        if event.type == pygame.QUIT:
            run = False
    
    # bullets
    for bullet in bullets:
        if bullet.x <screenWidth and bullet.x >0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    # key press events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
           bullets.append(projectile(round(man.x + man.width//2),  round(man.y + man.height//2), 6, blue, facing))

    if keys[pygame.K_UP]:
        man.y -= man.vel
    elif keys[pygame.K_DOWN]:
        man.y += man.vel
    elif keys[pygame.K_LEFT]:
        man.x -= man.vel
        man.left = True
    elif keys[pygame.K_RIGHT]:
        man.x += man.vel
        man.left = False

    # display loop updates
    redrawGameWindow()

#quit program
pygame.quit()