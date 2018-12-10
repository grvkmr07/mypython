import pygame, sys, time
from pygame.locals import *
# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0,32)
pygame.display.set_caption('Animation')
# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
MOVESPEED = 4
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
blocks = [b1, b2, b3]
# run the game loop
while True:
# check for the QUIT event
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
windowSurface.fill(BLUE)
for b in blocks:
    if b['dir'] == DOWNLEFT:
        b['rect'].left -= MOVESPEED
        b['rect'].top += MOVESPEED
    if b['dir'] == DOWNRIGHT:
        b['rect'].left += MOVESPEED
        b['rect'].top += MOVESPEED
    if b['dir'] == UPLEFT:
        b['rect'].left -= MOVESPEED
        b['rect'].top -= MOVESPEED
    if b['dir'] == UPRIGHT:
        b['rect'].left += MOVESPEED
        b['rect'].top -= MOVESPEED
