import pygame, sys, random
from pygame.locals import *
import player

"""Game Setup"""

pygame.init()
#Starts Pygame ~AS

"""Main variable setup"""

gameCamptionNameList = ["HJONK", "NOT THE GEEEEEEEEEEEEEEEEEEESE!", "Wait, isn't that a duck?", "duck,duck, who?"]
#List of window names ~AS
pygame.display.set_caption(gameCamptionNameList[random.randint(0, len(gameCamptionNameList)-1)])
#Sets window name ~AS

#makes clock object just so animatioins and everything aren't timed to frames ~MA
clock = pygame.time.Clock()

try:
    bg = pygame.image.load("BackgroundV1.0.png")
    #Gets background image ~AS
except:
    print("Background failed to load, terminating program")
    event = QUIT
    #Error handiling incase of failed load ~AS
windowMain = pygame.display.set_mode((320*3, 224*3),0,32)
#Setting screen size, harcoded due to fixed image size ~AS
bgRect = bg.get_rect()
#Gets bacground image size ~AS
bgRect.centerx = windowMain.get_rect().centerx
#Sets background image centerx ~AS
bgRect.centery = windowMain.get_rect().centery
#Sets background image centery ~AS

"""Game and game updates"""

windowMain.blit(bg, bgRect)
#What to update on screen ~AS
pygame.display.update()
#updates screen ~AS

# Makes player one ~MA
p1 = player.Player1(windowMain.get_rect().center)

#Makes list of all game objects ~MA
#for rn just p1
objects = [p1]

"""Game ending"""

while True:
    #Constant check
    for event in pygame.event.get():
        if event.type == QUIT:
            #Checks to see if the game is ended ~AS
            pygame.quit()
            #ends pygame ~AS
            sys.exit()
            #closes window ~AS
    #loops to update all game objects ~MA
    for object in objects:
        #updates background and then updates object in background ~MA
        windowMain.blit(bg, object.pos,object.pos)
        windowMain.blit(object.p1StandIdleAnim[0],object.pos)
    pygame.display.update()
    #caps the game at 60 fps ~MA
    clock.tick(60)