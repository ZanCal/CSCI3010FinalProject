import pygame, sys
import matplotlib.pyplot as plt
import numpy as np
import util


#na is the number of active moshers 
nact = 5

#np is the number of passive moshers
npass = 10

class Mosher():
    def __init__(self, mosherType):
        self.mosherType = mosherType
        self.width = 5
        self.height = 5
        if mosherType == "active":
            self.color = util.RED
        elif mosherType == "passive":
            self.color = util.BLACK

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.width, self.height], flags=pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        cx = self.rect.centerx
        cy = self.rect.centery
        pygame.draw.circle(self.image, self.color, (int(self.width/2), int(self.height/2)), cx, cy)

    def calcForce(self, other):

        force = np.zeros(4, dtype = 'float32')

        return force


class Simulation:
    def __init__(self, title, nact, npass):
        self.paused = True
        self.title = title
        self.curTime = 0
        self.dt = 0.033
        self.actState = np.zeros([nact, 4], dtype = 'float32')
        # x y vx vy for active moshers
        self.pasState = np.zeros([npass, 4], dtype = 'float32')
        # x y vx vy for passive moshers

def main():
    title = 'Mosh Sim'

    pygame.init()
    clock = pygame.time.Clock()
    text = util.BLACK

    activeMoshers = []
    passiveMoshers = []
    for i in range(nact):
        activeMoshers.append(Mosher("active"))
    for i in range(npass):
        passiveMoshers.append(Mosher("passive"))

    win_width = 640
    win_height = 480
    screen = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption(title)
    
    sim = Simulation(title, nact, npass)



main()