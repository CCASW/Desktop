import pygame, random
from wall import *
class Walls:
    def __init__(self):
        self.myList=[Wall(100,450), Wall(300,450), Wall(450,450), Wall(450,400),
                     Wall(450,350),Wall(500,350),Wall(550,350),Wall(600,350),Wall(650,350)]
    def Collision(self, guy):
        for Wall in self.myList:
            if guy.collide(Wall):
                return True
