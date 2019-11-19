#import pygame and random generator
import pygame, random, sys
# initialise pygame
pygame.init()

# intialise some colours
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0,0,0)
white = (255,255,255)

#window
screenWidth = 700
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill(black)

# text set up
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 50)
smallfont = pygame.font.SysFont('Arial', 20)

# setting a caption for game window
pygame.display.set_caption('Game Project')

# setting up clock
clock = pygame.time.Clock()