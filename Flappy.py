import random
import sys
import pygame
from pygame.locals import *    #general python import whenever using pygame lib

FPS = 30

screenWidth = 300 #setting up global variable for our game screen width
screenHeight = 520 #setting up global variable for our game screen Height

screen = pygame.display.set_mode((screenWidth,screenHeight)) # display.set_mode - setup up a game screen for the requirements given

groundY = screenHeight*0.8

game_Sprites = {}

game_Sounds = {
    
}

#declared the global variables for the player/background/pipe png file

player = '/gallery/sprites/bird.png'     
backGround = '/gallery/sprites/background.png'
pipe = '/gallery/sprites/pipe.png'

if __name__ == "__main__":
    
    pygame.init() #to initialize pygame modules
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird') #set caption of the game window
    game_Sprites['numbers'] = ( #created a tupple inside a dictionary to store our numbers
        # used image.load to load our image through pygame module and covert_alpha is used to optimize these images for the pygame
        pygame.image.load('gallery/sprites/0.png').convert_alpha(), 
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )




