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

player = 'gallery/sprites/bird.png'     
backGround = 'gallery/sprites/background.png'
pipes = (
    'gallery/sprites/pipe_green.png',
    'gallery/sprites/pipe_red.png',
)

def welcomeScreen():
    
    playerx= int(screenWidth/5)
    playery= int((screenHeight - game_Sprites['player'].get_height())/2)
    messagex = int((screenWidth - game_Sprites['message'].get_width())/2)
    messagey = int(screenHeight*0.13)
    basex=0
    while True:
        for event in pygame.event.get():      #event.get() fetches the events from the user
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN and (event.type==K_SPACE or event.type == K_UP):
                return 
                
            else:
                screen.blit(game_Sprites['background'], (0, 0))    
                screen.blit(game_Sprites['player'], (playerx, playery))    
                screen.blit(game_Sprites['message'], (messagex,messagey ))    
                screen.blit(game_Sprites['base'], (basex, groundY))    
                pygame.display.update()
                fpsClock.tick(FPS)


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

    game_Sprites['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    
    pipeId = random.randint(0,len(pipes)-1) #to randomly select different types of piples
    
    game_Sprites['pipe'] = (
        pygame.transform.rotate(pygame.image.load(pipes[pipeId]).convert_alpha(),180), # transform rotate is to rotate the pipes by 180 degree
        pygame.image.load(pipes[pipeId]).convert_alpha() 
    )
    
    #adding background and player image to sprites
    
    game_Sprites['background'] = pygame.image.load(backGround).convert() 
    game_Sprites['player'] = pygame.image.load(player).convert_alpha()
    
    
    game_Sounds['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    game_Sounds['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    game_Sounds['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    game_Sounds['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    game_Sounds['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    
    
    while True:
        welcomeScreen()
        mainGame()

