
import pygame
from pygame.locals import *
import sys
from pygame import event

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
V = 50
N = 50
vel = 5

luke = pygame.image.load("/Users/Shockwave/Desktop/IMAGES PY3/luke.png")
zombie = pygame.image.load("/Users/Shockwave/Desktop/IMAGES PY3/zombie.gif")

# game loop (work here)
keys = pygame.key.get_pressed()
if keys [pygame.K_w]:
    N = N - 1


























#DO NOT TOUCH!!!!
screen=pygame.display.set_mode((width, height))
while 1:
    screen.fill(0)
    screen.blit(luke, (N, V))
    screen.blit(zombie, (100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 
