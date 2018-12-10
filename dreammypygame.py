#have to set guns on fire and awaits till some seconds an append level
#moveing rectangles: save snakes
#Profile loader
import pygame
import time
import random 
x = pygame.init()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
bg = (45,240,214)
black = (0,0,0)
blue = (0,0,255)
color1=(154,216,247)
color2=(218,176,11)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('GK GAME')





clock =pygame.time.Clock()
FPS = 80

font = pygame.font.SysFont("Comic Sans MS", 55)

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2,display_height/2])
    
def gameLoop():
    gameExit=False
    gameOver=False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    randChickX = random.randrange(10, display_width-10)
    randChickY = random.randrange(10, display_height-10)
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(color1)
            message_to_screen("You LOSE!! Wanna try again? Press  y/n",color2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gameLoop()
                    if event.key == pygame.K_n:
                        gameExit=True
                        gameOver=False
                    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -2
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 2
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -2
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 2
                    lead_x_change = 0
            
           
                    
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(bg)
        pygame.draw.circle(gameDisplay, blue, (randChickX,randChickY),8)
        gameDisplay.fill(red, rect=[lead_x,lead_y,10,10])
        gameDisplay.fill(black, rect=[0,0,10,287.5])
        gameDisplay.fill(black, rect=[0,312.5,10,287.5])
        gameDisplay.fill(black, rect=[790,0,10,287.5])
        gameDisplay.fill(black, rect=[790,312.5,10,287.5])
        
        gameDisplay.fill(black, rect=[0,0,247.5,10])
        gameDisplay.fill(black, rect=[272.5,0,250,10])
        gameDisplay.fill(black, rect=[542.5,0,257.5,10])
        

        if lead_x < 10 and lead_y < 287.5:
            gameOver = True
        elif lead_x < 10 and lead_y > 312.5:
            gameOver = True
        elif lead_x > 790 and lead_y < 287.5:
            gameOver = True
        elif lead_x > 790 and lead_y > 312.5:
            gameOver = True
        elif lead_x < 247.5 and lead_y < 8:
            gameOver = True
        elif lead_x > 272.5 and lead_x < 522.5 and lead_y < 8:
            gameOver = True
        elif lead_x > 542.5 and lead_x < 600 and lead_y < 8:
            gameOver = True 
        
        
        pygame.display.update()

        clock.tick(FPS)
        
   



    pygame.quit()
    quit()
gameLoop()
