# import pygame
import pygame, sys

# initalise pygame
pygame.init() 

# intialise some colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0,0,0)
white = (255,255,255)

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
        self.left = False
        self.right = False
        self.up = False
        self.down = True

     #draw function
    def draw(self,win):
        pygame.draw.rect(win, red, (self.x, self.y, self.width, self.height))
   
# bullet class
class projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,height, width,colour,facing, XorY):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.colour = colour
        self.vel = 8 * facing
        if XorY == "X":
            self.movingX = True
            self.movingY = False
        else:
            self.movingY = True
            self.movingX = False

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)


# enemy class
class enemy(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height,end):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.vel = 3
        #path
        self.end = end
        self.path = [self.rect.x, self.end]

    #draw function
    def draw(self,win):
        self.move()
        pygame.draw.rect(win, green, self.rect)

    #movement
    def move(self):
        if self.vel > 0:
            if self.rect.x +self.vel < self.path[1]:
                self.rect.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.rect.x - self.vel > self.path[0]:
                self.rect.x += self.vel

            else:
                self.vel = self.vel * -1
        pass
     
#intialise objects
all_sprite_list = pygame.sprite.Group()

# player
man = player(250,350, 20, 20)
all_sprite_list.add(man)

#enemies
enemies = pygame.sprite.Group()
evil = enemy(200, 250, 20, 20, 500)
enemies.add(evil)
all_sprite_list.add(evil)

#projectiles
bullets = pygame.sprite.Group()

#window
screenWidth = 700
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)


# draw game function
def redrawGameWindow() :

    man.draw(win)
    for enemy in enemies:
        enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    #display update window
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
        if bullet.movingX:
            if bullet.rect.x <screenWidth and bullet.rect.x >0:
                bullet.rect.x += bullet.vel
            else:
                bullets.remove(bullet)
        if bullet.movingY:
            if bullet.rect.y < screenHeight and bullet.rect.y > 0:
                bullet.rect.y += bullet.vel
            else:
                bullets.remove(bullet)
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemies, True)
        for enemy in enemy_hit_list:
            bullets.remove(bullet)
            enemies.remove(enemy)

    # key press events
    keys = pygame.key.get_pressed()
    #shooting
    if keys[pygame.K_SPACE]:
        # determines which way facing
        if man.left or man.up:
            facing = -1
        else:
            facing = 1
        if man.left or man.right:
            XorY = "X"
        else:
            XorY = "Y"
        # max 5 bullets on screen at a time, makes bullet at centre of player and moves in direction facing
        if len(bullets) < 5:
           bullets.add(projectile(round(man.x + man.width//4),  round(man.y + man.height//4), 10, 10, blue, facing, XorY))


    #movement key presses with facing direction for shooting
    if keys[pygame.K_UP]:
        man.y -= man.vel
        man.up = True
        man.left = False
        man.right = False
        man.down = False
    elif keys[pygame.K_DOWN]:
        man.y += man.vel
        man.up = False
        man.left = False
        man.down = True
        man.right = False
    elif keys[pygame.K_LEFT]:
        man.x -= man.vel
        man.left = True
        man.down = False
        man.right = False
        man.up = False
    elif keys[pygame.K_RIGHT]:
        man.x += man.vel
        man.left = False
        man.up = False
        man.down = False
        man.right = True

    # display loop updates
    redrawGameWindow()

#quit program
pygame.quit()