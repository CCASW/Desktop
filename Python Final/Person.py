import pygame
from pygame.locals import *
import pygame
from walls import *
class Person:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.up=False
        self.upCounter=0

        # Add images to the list of images
        #self.images = ["dude.gif", "dudeL.gif", "dudeR.gif", "dudeU.gif"]
        self.images=["dude.gif", "dudeU.gif", "dudeR.gif", "dudeL.gif"]
        # Use this to keep track of which image to use
        self.cos = 0
    
    #  draw your person with the correct image
    def draw(self, window):
        window.blit(pygame.image.load(self.images[self.cos]),(self.x,self.y))
    # move person left and set the costume facing left.
    def moveLeft(self):
        self.cos=3
        if self.x>0:
            self.x-=1
    # move person right and set the costume facing right
    def moveRight(self):
        self.cos=2
        if self.x<752:
            self.x+=1
    def moveRight1(self):
        self.x+=1
    def moveLeft1(self):
        self.x-=1
    # move person up and set the costume facing up
    def jump(self):
        self.upCounter=0
        self.up=True
    def moveUp(self):
        self.y-=1
    def update(self):
        if self.up==True:
            self.y=self.y-2
            self.upCounter=self.upCounter+1
            print(self.upCounter)
            if self.upCounter>=75:
                self.up=False
        elif self.y!=450 and not self.collide(obs.myList[0]):
            self.y=self.y+2
            self.upCounter=self.upCounter-1
            print(self.upCounter)
        
    # move person down and set the costume facing down
    def moveDown(self):
        if self.y<450:
            self.y+=1
    # This will return True if your person has collided with other
    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight  = otherRec[0] + otherRec[2]
        oBottom  = otherRec[1] + otherRec[3]
    
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]
        
        
        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
            return True
        return False


    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = pygame.image.load(self.images[self.cos]).get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
