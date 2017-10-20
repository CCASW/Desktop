import pygame, sys
from pygame.locals import *
from Ground import *
from Person import *
from Level1 import *
from wall import *
from walls import*
# Initialize the screen
pygame.init()
screen = pygame.display.set_mode((800,600))


# draw the ground
background = pygame.Surface((800,600))

drawLevel1(background)
screen.blit(background, (0,0))

# Check if a key is still pressed down every 100 milliseconds
# allows user to hold down the key to move
pygame.key.set_repeat(1,1)

obs=Walls()
# create a person at position (400, 50)
guy = Person(400, 50)
# A list that keeps track of the areas of screen that have changed
changedRecs = []

#draw the starting screen
pygame.display.update()
while True:
    # draw the scene
    screen.blit(background, (0,0))
    #hit=obs.Collision(guy)
    guy.draw(screen)
    guy.update()
    # adds the current position of guy to the areas that have been changed
    changedRecs.append(guy.getRec())
    y=0
    for Wall in obs.myList:
        if guy.collide(obs.myList[y]) and guy.y<=450:
            guy.moveUp()
            print(guy.y,"Intentional Lag")
        y+=1
    #update only the changed areas of the screen
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==KEYDOWN:
            if event.key==K_UP: 
                guy.jump()
            elif event.key==K_LEFT:
                y=0
                guy.moveLeft()
                for Wall in obs.myList:
                    if guy.collide(obs.myList[y]):
                        guy.moveRight1()
                    y+=1
            elif event.key==K_RIGHT:
                y=0
                guy.moveRight()
                for Wall in obs.myList:
                    if guy.collide(obs.myList[y]):
                        guy.moveLeft1()
                    y+=1

                        
