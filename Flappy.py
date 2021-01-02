import random
import sys
import pygame
from pygame.locals import *    #general python import whenever using pygame lib

FPS = 30

screenWidth = 289 #setting up global variable for our game screen width
screenHeight = 512 #setting up global variable for our game screen Height

screen = pygame.display.set_mode((screenWidth,screenHeight)) # display.set_mode - setup up a game screen for the requirements given

groundY = screenHeight*0.8

game_Sprites = {}

game_Sounds = {
}

#declared the global variables for the player/background/pipe png file

player = (
    'C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/yellowbird.png',
    'C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/bird.png',
    'C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/bluebird.png',
    
)    

 #to randomly select different types of piples
    
game_Sprites['player'] = (
    pygame.image.load(player[0]).convert_alpha(), # transform rotate is to rotate the pipes by 180 degree
    pygame.image.load(player[1]).convert_alpha(),
    pygame.image.load(player[2]).convert_alpha(),
)
backGround = (
    'C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/background.png',
    'C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/background-night.png'
)

pipes = (
    'C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/pipe_green.png',
    'C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/pipe_red.png',
)

def welcomeScreen():
    
    playerx= int(screenWidth/5)
    playery= int((screenHeight - game_Sprites['player'][playerId].get_height())/2)
    messagex = int((screenWidth - game_Sprites['message'].get_width())/2)
    messagey = int(screenHeight*0.13)
    basex=0
    while True:
        for event in pygame.event.get():      #event.get() fetches the events from the user
            if event.type == QUIT or (event.type == KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return 
                
            else:
                screen.blit(game_Sprites['background'], (0, 0))    
                screen.blit(game_Sprites['player'][playerId], (playerx, playery))    
                screen.blit(game_Sprites['message'], (messagex,messagey ))    
                screen.blit(game_Sprites['base'], (basex, groundY))    
                pygame.display.update()
                fpsClock.tick(FPS)

def mainGame():
    score = 0
    playerx = int(screenWidth/5)
    playery = int(screenWidth/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': screenWidth+200, 'y':newPipe1[0]['y']},
        {'x': screenWidth+200+(screenWidth/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': screenWidth+200, 'y':newPipe1[1]['y']},
        {'x': screenWidth+200+(screenWidth/2), 'y':newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    game_Sounds['wing'].play()


        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            return     

        #check for score
        playerMidPos = playerx + game_Sprites['player'][playerId].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + game_Sprites['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                game_Sounds['point'].play()


        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = game_Sprites['player'][playerId].get_height()
        playery = playery + min(playerVelY, groundY - playery - playerHeight)

        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] <-game_Sprites['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        # Lets blit our sprites now
        screen.blit(game_Sprites['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            screen.blit(game_Sprites['pipe'][0], (upperPipe['x'], upperPipe['y']))
            screen.blit(game_Sprites['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        screen.blit(game_Sprites['base'], (basex, groundY))
        screen.blit(game_Sprites['player'][playerId], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += game_Sprites['numbers'][digit].get_width()
        Xoffset = (screenWidth - width)/2

        for digit in myDigits:
            screen.blit(game_Sprites['numbers'][digit], (Xoffset, screenHeight*0.12))
            Xoffset += game_Sprites['numbers'][digit].get_width()
        pygame.display.update()
        fpsClock.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> groundY - 25  or playery<0:
        game_Sounds['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = game_Sprites['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < game_Sprites['pipe'][0].get_width()):
            game_Sounds['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + game_Sprites['player'][playerId].get_height() > pipe['y']) and abs(playerx - pipe['x']) < game_Sprites['pipe'][0].get_width():
            game_Sounds['hit'].play()
            return True

    return False

def getRandomPipe():
    
    #Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    
    pipeHeight = game_Sprites['pipe'][0].get_height()
    offset = screenHeight/3
    y2 = offset + random.randrange(0, int(screenHeight - game_Sprites['base'].get_height()  - 1.2 *offset))
    pipeX = screenWidth + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe

    

if __name__ == "__main__":
    
    pygame.init() #to initialize pygame modules
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird') #set caption of the game window
    game_Sprites['numbers'] = ( #created a tupple inside a dictionary to store our numbers
        # used image.load to load our image through pygame module and covert_alpha is used to optimize these images for the pygame
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/0.png').convert_alpha(), 
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/9.png').convert_alpha(),
    )

    game_Sprites['message'] = pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/message.png').convert_alpha()
    
    game_Sprites['base'] =pygame.image.load('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/sprites/base.png').convert_alpha()
    #adding background and player image to sprites
    
    game_Sounds['die'] = pygame.mixer.Sound('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/audio/die.wav')
    game_Sounds['hit'] = pygame.mixer.Sound('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/audio/hit.wav')
    game_Sounds['point'] = pygame.mixer.Sound('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/audio/point.wav')
    game_Sounds['swoosh'] = pygame.mixer.Sound('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/audio/swoosh.wav')
    game_Sounds['wing'] = pygame.mixer.Sound('C:/Users/DELL-PC/Documents/GitHub/Pygame_Tetris/gallery/audio/wing.wav')
    
    
    while True:
        playerId = random.randint(0,len(player)-1)
        backgroundId = random.randint(0,len(backGround)-1)
        game_Sprites['background'] = pygame.image.load(backGround[backgroundId]).convert() 
        pipeId = random.randint(0,len(pipes)-1) #to randomly select different types of piples
        game_Sprites['pipe'] = (
            pygame.transform.rotate(pygame.image.load(pipes[pipeId]).convert_alpha(),180), # transform rotate is to rotate the pipes by 180 degree
            pygame.image.load(pipes[pipeId]).convert_alpha() 
        )
        welcomeScreen()
        mainGame()

