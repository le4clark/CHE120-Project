import pygame, sys, random
from pygame.locals import *
import player
import player2
import music

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
bg = pygame.image.load("BackgroundV1.0.png").convert()
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
p2 = player2.Player2(windowMain.get_rect().center)
Music = music.music()

#Makes list of all game objects ~MA
#for rn just p1
#objects = [p1,p2]

#MY: velocity variables in x & y directions
x_velocity = 0
y_velocity = 0
x_velocity2 = 0
y_velocity2 = 0
#MY: Player's initial position is at ground level,
#MY: Initial position set to be ground level
on_ground = True
on_ground2 = True
ground_level = p1.pos.bottom
#MY: Initial position is in stand animation
p1Facing = True
p2Facing = True
#dictates facing direction for idle animation, true if right, false if left ~AS
animation = p1.p1StandIdleAnim[0]
animation2 = p2.p2StandIdleAnim[0]
"""Game ending"""
attacking = False
attacking2 = False
#Preventing movement while attacking
while True:
    animFrame = round(pygame.time.get_ticks()/200)%2
    #returns 1 or zero to cycle between idle animations ~AS
    #MY: gets a list of all keys being pressed
    keys = pygame.key.get_pressed()
    
    #MY: If w is among those pressed
    if keys[pygame.K_w] == True and not attacking:
        #MY: You can only jump if you're on the ground
        if on_ground:
            #MY: velocity of y movement is set
            y_velocity = -12
            #MY: if you jump, you are no longer on the ground
            on_ground = False
    #MY: If s is among those pressed
    if keys[pygame.K_s] == True and not attacking:
        #MY: You can only go downwards if you're in the air
        if not on_ground:
            #MY: Downwards movement velocity
            y_velocity = 10
        else:
            if p1Facing: animation = p1.p1CrouchIdleAnim[0]
            else: animation = pygame.transform.flip(p1.p1CrouchIdleAnim[0], True, False)
            #crouch anim ~AS
            
            if x_velocity > 0: x_velocity = 7
            elif x_velocity < 0: x_velocity = -7
            #Crouch Sliding for extra speed ~AS
    #MY: If a is among those pressed
    if keys[pygame.K_a] == True and not attacking:
        #MY: animation changes to walk and velocity to the left
        animation = pygame.transform.flip(p1.p1StandWalkAnim[animFrame], True, False)
        
        x_velocity = -5
        p1Facing = False
        #sets facing to left ~AS
    #MY: If d is among those pressed
    elif keys[pygame.K_d] == True and not attacking:
        #MY: animation changes to walk and velocity to the right
        animation = p1.p1StandWalkAnim[animFrame]
        x_velocity = 5
        p1Facing = True
        #sets facing to right ~AS
    #MY: If a or d are no longer being pressed;
    elif keys[pygame.K_a] == False and keys[pygame.K_d] == False and keys[pygame.K_s] == False and not attacking:
        #MY: change animation to standing
        if p1Facing: animation = p1.p1StandIdleAnim[animFrame]
        else: animation = pygame.transform.flip(p1.p1StandIdleAnim[animFrame], True, False)
        #left and right standing idle facing animations ~AS
        #MY: and set velocity to 0
        x_velocity = 0
    
    #MY: change animation to flying if not on ground
    if not on_ground:
        if p1Facing: animation = p1.p1JumpIdleAnim[animFrame]
        #Right facing jump idle animation ~AS
        else: animation = pygame.transform.flip(p1.p1JumpIdleAnim[animFrame], True, False)
        #Left facing jump idle animation ~AS
    
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
        #animation = p1.p1StandIdleAnim[0]
    if p1.pos.centerx < 40: p1.pos.centerx = 41
    if p1.pos.centerx > 916: p1.pos.centerx = 915
    print(clock.get_fps())
    #prevention from players going out of bounds




    
    #MY: If w is among those pressed
    if keys[pygame.K_i] == True and not attacking2:
        #MY: You can only jump if you're on the ground
        if on_ground2:
            #MY: velocity of y movement is set
            y_velocity2 = -12
            #MY: if you jump, you are no longer on the ground
            on_ground2 = False
    #MY: If s is among those pressed
    if keys[pygame.K_k] == True and not attacking2:
        #MY: You can only go downwards if you're in the air
        if not on_ground2:
            #MY: Downwards movement velocity
            y_velocity2 = 10
        else:
            if p2Facing: animation2 = p2.p2CrouchIdleAnim[0]
            else: animation2 = pygame.transform.flip(p2.p2CrouchIdleAnim[0], True, False)
            #crouch anim ~AS
            
            if x_velocity2 > 0: x_velocity2 = 7
            elif x_velocity2 < 0: x_velocity2 = -7
            #Crouch Sliding for extra speed ~AS
    #MY: If a is among those pressed
    if keys[pygame.K_j] == True and not attacking2:
        #MY: animation changes to walk and velocity to the left
        animation2 = pygame.transform.flip(p2.p2StandWalkAnim[animFrame], True, False)
        
        x_velocity2 = -5
        p2Facing = False
        #sets facing to left ~AS
    #MY: If d is among those pressed
    elif keys[pygame.K_l] == True and not attacking2:
        #MY: animation changes to walk and velocity to the right
        animation2 = p2.p2StandWalkAnim[animFrame]
        x_velocity2 = 5
        p2Facing = True
        #sets facing to right ~AS
    #MY: If a or d are no longer being pressed;
    elif keys[pygame.K_j] == False and keys[pygame.K_l] == False and keys[pygame.K_k] == False and not attacking2:
        #MY: change animation to standing
        if p2Facing: animation2 = p2.p2StandIdleAnim[animFrame]
        else: animation2 = pygame.transform.flip(p2.p2StandIdleAnim[animFrame], True, False)
        #left and right standing idle facing animations ~AS
        #MY: and set velocity to 0
        x_velocity2 = 0
    
    #MY: change animation to flying if not on ground
    if not on_ground2:
        if p2Facing: animation2 = p2.p2JumpIdleAnim[animFrame]
        #Right facing jump idle animation ~AS
        else: animation2 = pygame.transform.flip(p2.p2JumpIdleAnim[animFrame], True, False)
        #Left facing jump idle animation ~AS
 
    #MY: adding gravity acceleration
    y_velocity2 += 0.3
    
    #MY: redefines position of p1 hitbox according to velocities
    p2.pos = p2.pos.move(x_velocity2, y_velocity2)
    
    #MY: if the bottom of the hitbox is at ground level;
    if p2.pos.bottom >= ground_level:
        #MY: if below, moved to ground level
        p2.pos.bottom = ground_level
        #MY: the goose is on the ground
        on_ground2 = True
        #MY: animation changes from flying to stand
        #animation = p1.p1StandIdleAnim[0]
    if p2.pos.centerx < 40: p2.pos.centerx = 41
    if p2.pos.centerx > 916: p2.pos.centerx = 915
    print(clock.get_fps())
    #prevention from players going out of bounds










    #Constant check
    for event in pygame.event.get():
        if event.type == QUIT:
            #Checks to see if the game is ended ~AS
            pygame.quit()
            #ends pygame ~AS
            sys.exit()
            #closes window ~AS
    windowMain.blit(bg, (0,0))
    windowMain.blit(animation,p1.pos)
    windowMain.blit(animation2,p2.pos)

    pygame.display.update()
    #caps the game at 60 fps ~MA
    clock.tick(60)
