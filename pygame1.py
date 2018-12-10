import pygame,sys,random
from multiprocessing import Process
import random

white = (255,255,255)
red = (255,0,0)
yellow = (0,255,0)
pygame.init()
pygame.display.set_caption('First trial: Pygame')
size = [640,480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    x=random.randrange(10,350)
    y = 10
    l = 320
    r = 475
    
    while y<350:

        y += 10
        screen.fill(yellow)
        pygame.draw.circle(screen,red,(x,y),10)
        pygame.display.update()
        clock.tick(50)
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                l -= 10
                
            if event.key == pygame.K_RIGHT:
                r += 10
                
        pygame.draw.rect(screen,red,[l,r,50,5])
        
        pygame.display.update()
        clock.tick(10)
   
    
        
