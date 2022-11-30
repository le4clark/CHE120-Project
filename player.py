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
      #temp just one image ~MA
      self.image = self.p1StandIdleAnim[0]
      #gets image rect ~MA
      imagerec = self.image.get_rect()
      #centers it and places at location ~MA
      imagerec.center = center
      self.pos = imagerec.move(-300, 200)
class Player2:
   def __init__(self, center):

      #declares all the animations for the player ~MA
      self.p2StandIdleAnim = [pygame.image.load("WhiGooseAnimations/frame0000.png"),pygame.image.load("WhiGooseAnimations/frame0001.png")]
      self.p2StandWalkAnim = [pygame.image.load("WhiGooseAnimations/frame0001.png"),pygame.image.load("WhiGooseAnimations/frame0002.png")]
      self.p2StandAttackAnim = [pygame.image.load("WhiGooseAnimations/frame0002.png"),pygame.image.load("WhiGooseAnimations/frame0003.png")]
      self.p2CrouchIdleAnim = [pygame.image.load("WhiGooseAnimations/frame0004.png")]
      self.p2CrouchWalkAnim = [pygame.image.load("WhiGooseAnimations/frame0004.png"),pygame.image.load("WhiGooseAnimations/frame0005.png")]
      self.p2CrouchAttackAnim = [pygame.image.load("WhiGooseAnimations/frame0006.png"),pygame.image.load("WhiGooseAnimations/frame0007.png")]
      self.p2JumpIdleAnim = [pygame.image.load("WhiGooseAnimations/frame0008.png"),pygame.image.load("WhiGooseAnimations/frame0009.png")]
      self.p2JumpAttackAnim = [pygame.image.load("WhiGooseAnimations/frame0010.png")]
      #temp just one image ~MA
      self.image = self.p2StandIdleAnim[0]
      #gets image rect ~MA
      imagerec = self.image.get_rect()
      #centers it and places at location ~MA
      imagerec.center = center
      self.pos = imagerec.move(-300, 200)