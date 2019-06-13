# import pygame
import pygame, sys, random

# initalise pygame
pygame.init() 

#window
screenWidth = 700
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)


# intialise some colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0,0,0)
white = (255,255,255)

# text set up
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 50)

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
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = True

     #draw function
    def draw(self,win):
        pygame.draw.rect(win, red, self.rect)
   
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

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)


# enemy class
class enemy(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.vel = 1
        self.health = 3

    #draw function
    def draw(self,win):
        self.move()
        pygame.draw.rect(win, green, self.rect)

    #movement
    def move(self):
        if self.rect.x < man.rect.x:
            self.rect.x += self.vel
        elif self.rect.x > man.rect.x:
            self.rect.x -= self.vel

        if self.rect.y < man.rect.y:
            self.rect.y += self.vel
        elif self.rect.y > man.rect.y:
            self.rect.y -= self.vel
    
    def shot(self):
        self.health -= 1
        if self.health == 0:
            enemies.remove(self)
        enemy_hit_list.remove(self)

# game over function
def gameOver():
    win.blit(myfont.render('Game Over', True, white), (screenWidth/2 - 125, 50))

# game win funtion
def gameWin():
    win.blit(myfont.render('Game Win', True, white), (screenWidth/2 - 125, 50))

#intialise objects
all_sprite_list = pygame.sprite.Group()

# player
man = player(250,350, 20, 20)
all_sprite_list.add(man)

#enemies
enemies = pygame.sprite.Group()
for i in range(10):
    i = enemy(random.randint(10,screenWidth-30),random.randint(10,screenHeight/2), 20, 20)
    enemies.add(i)
    all_sprite_list.add(i)

#projectiles
bullets = pygame.sprite.Group()
reloadTime = 0

# draw game function
def redrawGameWindow():

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
    
    # check if there are no enemies
    if enemies.__len__() == 0:
        gameWin()
        run = False
    
    # bullets
    for bullet in bullets:
        if bullet.movingX:
            if bullet.rect.x <screenWidth and bullet.rect.x >0:
                bullet.rect.x += bullet.vel
            else:
                bullets.remove(bullet)
        
        # changes bullet dimensions
        if bullet.movingY:
            temp = bullet.rect.width
            bullet.rect.width = bullet.rect.height
            bullet.rect.height = bullet.rect.width
            if bullet.rect.y < screenHeight and bullet.rect.y > 0:
                bullet.rect.y += bullet.vel
            else:
                bullets.remove(bullet)
       
       # bullet-enemy collisions
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemies, True)
        for enemy in enemy_hit_list:
            bullets.remove(bullet)
            if bullet.movingX:
                if bullet.vel > 0:
                    enemy.rect.x += 3
                else:
                    enemy.rect.x -= 3
            else:
                if bullet.vel > 0:
                    enemy.rect.y += 3
                else:
                    enemy.rect.y -= 3                
            enemy.shot()

    # enemy-player collisions
    for enemy in enemies:
        if pygame.sprite.collide_rect(enemy, man):
            gameOver()
            run = False


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
        # max 5 bullets on screen at a time, makes bullet at centre of player and moves in direction facing, also adds delay between bullets
        if len(bullets) < 5 and reloadTime == 0:
           bullets.add(projectile(round(man.rect.x + man.rect.width//4),  round(man.rect.y + man.rect.height//4), 6, 10, blue, facing, XorY, 10))
           reloadTime = 1
        else:
            reloadTime = 0


    #movement key presses with facing direction for shooting
    if keys[pygame.K_UP]:
        man.rect.y -= man.vel
        man.up = True
        man.left = False
        man.right = False
        man.down = False
    elif keys[pygame.K_DOWN]:
        man.rect.y += man.vel
        man.up = False
        man.left = False
        man.down = True
        man.right = False
    elif keys[pygame.K_LEFT]:
        man.rect.x -= man.vel
        man.left = True
        man.down = False
        man.right = False
        man.up = False
    elif keys[pygame.K_RIGHT]:
        man.rect.x += man.vel
        man.left = False
        man.up = False
        man.down = False
        man.right = True

    # display loop updates
    redrawGameWindow()

while not run:

    clock.tick(30)

    #event loop
    for event in pygame.event.get():
        # bomb out of loop if quit
        if event.type == pygame.QUIT:
            run = True

#quit program
pygame.quit()