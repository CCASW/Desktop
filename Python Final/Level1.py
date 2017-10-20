import pygame
from pygame.locals import *
def drawLevel1(window):
    images=["Lava.png","enemy.gif","road.gif","grass.gif","rtograss.gif","gtoroad.gif","sky.png","wall.gif"]
    cos=0
    xPos=0
    yPos=0
    while xPos<800:
        while yPos<600:
            if not yPos>=350:
                cos=6
                window.blit(pygame.image.load(images[cos]),(xPos,yPos)) 
                yPos+=50
            elif yPos==450:
                if xPos==100 or xPos==300 or xPos==450:
                    cos=7
                else:
                    cos=6
                window.blit(pygame.image.load(images[cos]),(xPos,yPos))
                yPos+=50
            elif yPos==400:
                if xPos==450:
                    cos=7
                else:
                    cos=6
                window.blit(pygame.image.load(images[cos]),(xPos,yPos))
                yPos+=50
            elif yPos==350:
                if xPos>=450 and xPos<=650:
                    cos=7
                else:
                    cos=6
                window.blit(pygame.image.load(images[cos]),(xPos,yPos))
                yPos+=50 
            elif yPos>=500:
                if not(xPos==400 or xPos==350):
                    cos=3
                else:
                    cos=0
                window.blit(pygame.image.load(images[cos]),(xPos,yPos)) 
                yPos+=50 
        xPos+=50
        yPos=0
