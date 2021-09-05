#importing modules
import time
import random
import pygame,sys
from pygame.locals import *

#word list
wordList=['jump','game','python','pygame',
          'play','coding','time','random','words',
          'word','score','player','lost','won','develop',
          'jumpGame','project','code','jumble','answer',
          'difficult','annoy','scare','scary','bean','dummy',
          'boil','plot','honey','koala','monkey']

#initializing pygame
pygame.init()

#creating game window of size 1000x800 
window = pygame.display.set_mode((1000,800))

#loading background image
bg = pygame.image.load('bg.jpg')
#adjusting image size as per window size
bg = pygame.transform.scale(bg,(1000,800))

#setting font style
myFont=pygame.font.SysFont('Segoe UI',30)

#global variables
speed = 0.6
score=0
gamenotover=True
gamestarted=False

#-------------------------to get a random word---------------------------
def generateWord():
    global currWord, playerWord,x,y,speed

    # choosing a random x coordinate for current word
    x=random.randint(150,550)
    # y coordinate
    y=150

    #incresing speed to increase the difficulty of game with time
    speed = speed + 0.05
    #initializing player's word
    playerWord= ''

    #choosing a random word from word list
    currWord = random.choice(wordList)

#calling generateWord function
generateWord()


#-----------------------to place text on pygame window--------------------------------
def putText(x,y,text,sz):
    #setting font size
    myFont=pygame.font.SysFont('Segoe UI',sz)

    #rendering the text
    mytext = myFont.render(text,True,(0,0,0))

    #blitting the text on window
    window.blit(mytext,(x,y))


#----------------------to display initial and final screen--------------------------------
def displayScreen():
    #blitting background image on window
    window.blit(bg,(0,0))

    #if game is over
    if gamenotover is False: 
        #display game over on the window, here 100 is size of the text
        putText(200,200,"Game Over!!!",100)
        #displaying final score
        putText(200,300,"Score: "+str(score),50)

    #if game is not over
    else:
        putText(200,200,"Press a Key to start playing!",50)
    
    #for better effects we will flip the window
    pygame.display.flip()

    #remains true until a key is pressed
    wait=True
    while wait:
        #checking all events sequentially
        for e in pygame.event.get():
            #if user wants to quit window
            if e.type == pygame.QUIT:
                #quitting pygame
                pygame.quit()
            
            #if any other key is pressed
            if e.type== pygame.KEYDOWN:
                # so as to begin the game setting wait = False
                wait = False


#infinite loop until game is over
while True:
    if gamenotover:
        if not gamestarted:
            #initializing the game window
            displayScreen()

        #setting gamestarted to True
        gamestarted=True
    gamenotover=False

    #loading playing character
    character = pygame.image.load('character.png')
    #transforming it to size 50x50 
    character = pygame.transform.scale(character,(50,50))

    #setting bg image 
    window.blit(bg,(0,0))

    y+=speed
    #displaying character
    window.blit(character,(x-100,y))

    #displaying current Word
    putText(x,y,str(currWord),35)

    #displaying score
    putText(300,5,'Score: '+str(score),35)

    #events------
    for e in pygame.event.get():
         #if user wants to quit window
        if e.type == pygame.QUIT:
            #quitting pygame
            pygame.quit()
            quit()

        # if user pressed another button
        elif e.type == pygame.KEYDOWN:
            #adding pressed letter in playerWord
            print(pygame.key.name(e.key))
            playerWord+= pygame.key.name(e.key)

            #if the playerWord is correct till now
            if currWord.startswith(playerWord):
                #if both the words are matching
                if currWord == playerWord:
                    #increase score
                    score += 10
                    #generate new word
                    generateWord()

            #if user mis-spelled the word
            else:
                displayScreen()
                time.sleep(2)
                pygame.quit()

    #if the word has not reached bottom continue updating the window 
    if y< 590:
        pygame.display.update()
    #word reached end therefore end the game
    else:
        displayScreen()
                
