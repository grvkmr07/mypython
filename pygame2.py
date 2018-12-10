import pygame, sys,random
from multiprocessing import Process
#import sys

 
white = (255, 255, 255)
red = (255, 0, 0)
BLUE =(0,0,255)
GREEN=(0,255,0)
yellow = (255,255,0)

pygame.init()
pygame.display.set_caption('Keyboard Example')
size = [640, 480]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
 
x = 100
y = 550
 
# using this to set the size of the rectange
# using this to also move the rectangle
step = 50
 
# by default the key repeat is disabled
# call set_repeat() to enable it
pygame.key.set_repeat(50, 50)
y1 =50
t=50
x1=300
pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)


def  readkey():
    global x,y,screen,step,clock,size,white,red,BLUE,GREEN,y1,x1,yellow
    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('motorcycle.wav'))    
    while True:
        y1+=20
        if y1>700:
            y1=50
            x1 = random.randrange(10,500,20)
            
    #pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
    #pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
    #pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
    #pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)
    
    #pygame.draw.ellipse(screen, red, (300, 200, 40, 80), 1)
    #pygame.draw.rect(screen, red, (200, 150, 100, 50))

    
         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # check if key is pressed
            # if you use event.key here it will give you error at runtime
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= step
                if event.key == pygame.K_RIGHT:
                    x += step
                #if event.key == pygame.K_UP:
                   # y -= step
                #if event.key == pygame.K_DOWN:
                   # y += step
                # checking if left modifier is pressed
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    if event.key == pygame.K_LEFT:
                        x = 0
                    if event.key == pygame.K_RIGHT:
                        x = 640 - step
                    if event.key == pygame.K_UP:
                        y = 0
                    if event.key == pygame.K_DOWN:
                        y = 480 - step
     
        # limit the rectangle from going out of the visible area
        if (x < 0): x = 0
        elif (x > (640-step)): x = 640-step
        if (y < 0): y = 0
        elif (y > (480-step)): y = 480-step
     
        screen.fill(BLUE)
     
        # draw a rectangle
        pygame.draw.rect(screen, red, ((x, y), (step, step)), 0)
        pygame.draw.circle(screen, yellow, (x1, y1), 20, 0)
        
        
        pygame.display.update()
        clock.tick(200)


'''
if __name__=='__main__':
     p1 = Process(target = readkey)
     p1.start()
     p2 = Process(target = dropcircle)
     p2.start()

'''

readkey()
