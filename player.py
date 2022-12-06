import pygame, sys

class Player1:
   def __init__(self, center):

      #declares all the animations for the player ~MA
      self.p1StandIdleAnim = [pygame.image.load("CanGooseAnimations/frame0000.png"),pygame.image.load("CanGooseAnimations/frame0001.png")]
      self.p1StandWalkAnim = [pygame.image.load("CanGooseAnimations/frame0001.png"),pygame.image.load("CanGooseAnimations/frame0002.png")]
      self.p1StandAttackAnim = [pygame.image.load("CanGooseAnimations/frame0002.png"),pygame.image.load("CanGooseAnimations/frame0003.png")]
      self.p1CrouchIdleAnim = [pygame.image.load("CanGooseAnimations/frame0004.png")]
      self.p1CrouchWalkAnim = [pygame.image.load("CanGooseAnimations/frame0004.png"),pygame.image.load("CanGooseAnimations/frame0005.png")]
      self.p1CrouchAttackAnim = [pygame.image.load("CanGooseAnimations/frame0006.png"),pygame.image.load("CanGooseAnimations/frame0007.png")]
      self.p1JumpIdleAnim = [pygame.image.load("CanGooseAnimations/frame0008.png"),pygame.image.load("CanGooseAnimations/frame0009.png")]
      self.p1JumpAttackAnim = [pygame.image.load("CanGooseAnimations/frame0010.png")]
      self.kbx = 0
      self.kby = 0
      #Knockback ~LC
      self.health = 100
      #Player health ~LC
      #temp just one image ~MA
      self.image = self.p1StandIdleAnim[0]
      #gets image rect ~MA
      imagerec = self.image.get_rect()
      #centers it and places at location ~MA
      imagerec.center = center
      self.pos = imagerec.move(-300, 200)