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

#MY: velocity variables in x & y directions
x_velocity = 0
y_velocity = 0
#MY: Player's initial position is at ground level,
#MY: Initial position set to be ground level
on_ground = True
ground_level = p1.pos.bottom
#MY: Initial position is in stand animation
animation = p1.p1StandIdleAnim[0]

"""Game ending"""

while True:
    
    #MY: gets a list of all keys being pressed
    keys = pygame.key.get_pressed()
    
    #MY: If w is among those pressed
    if keys[pygame.K_w] == True:
        #MY: You can only jump if you're on the ground
        if on_ground:
            #MY: velocity of y movement is set
            y_velocity = -12
            #MY: if you jump, you are no longer on the ground
            on_ground = False
    #MY: If s is among those pressed
    if keys[pygame.K_s] == True:
        #MY: You can only go downwards if you're in the air
        if not on_ground:
            #MY: Downwards movement velocity
            y_velocity = 10
    #MY: If a is among those pressed
    if keys[pygame.K_a] == True:
        #MY: animation changes to walk and velocity to the left
        animation = p1.p1StandWalkAnim[0]
        x_velocity = -5
    #MY: If d is among those pressed
    if keys[pygame.K_d] == True:
        #MY: animation changes to walk and velocity to the right
        animation = p1.p1StandWalkAnim[0]
        x_velocity = 5
    #MY: If a or d are no longer being pressed;
    if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
        #MY: change animation to standing
        animation = p1.p1StandIdleAnim[0]
        #MY: and set velocity to 0
        x_velocity = 0
    
    #MY: change animation to flying if not on ground
    if not on_ground:
        animation = p1.p1JumpIdleAnim[0]
    
    #MY: adding gravity acceleration
    y_velocity += 0.3
    
    #MY: redefines position of p1 hitbox according to velocities
    p1.pos = p1.pos.move(x_velocity, y_velocity)
    
    #MY: if the bottom of the hitbox is at ground level;
    if p1.pos.bottom >= ground_level:
        #MY: if below, moved to ground level
        p1.pos.bottom = ground_level
        #MY: the goose is on the ground
        on_ground = True
        #MY: animation changes from flying to stand
        animation = p1.p1StandIdleAnim[0]
        
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
        windowMain.blit(bg, (0,0))
        windowMain.blit(bg, object.pos,object.pos)
        windowMain.blit(animation,object.pos)
    pygame.display.update()
    #caps the game at 60 fps ~MA
    clock.tick(60)
