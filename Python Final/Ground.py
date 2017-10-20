import pygame, random
from pygame.locals import *
import pygame, random 
        
def drawGround(window):
    # load all images into a list 
    images=["grass.gif","rtograss.gif","road.gif","gtoroad.gif"]
    cos=0
    xPos=0
    yPos=0
    while xPos<800:
        while yPos<600:
            if yPos==0 or yPos==50 or yPos>=550:
                cos=0
                window.blit(pygame.image.load(images[cos]),(xPos,yPos))
                yPos+=50
            elif yPos==100:
                cos=3
                window.blit(pygame.image.load(images[cos]),(xPos,yPos))
                yPos+=50
            elif yPos>=150 and yPos<=450:
                cos=2
                window.blit(pygame.image.load(images[cos]),(xPos,yPos))
                yPos+=50
            elif yPos==500:
                cos=1
                window.blit(pygame.image.load(images[cos]),(xPos,yPos))
                yPos+=50
        xPos+=50
        yPos=0
