import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
  def __init__(self, x, y, fileName, btnType):
    pygame.sprite.Sprite.__init__(self)
    if btnType == "small":
      self.image = pygame.image.load(fileName).convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.image = pygame.transform.scale(self.image,(50,50))
    elif btnType == "large":
      self.image = pygame.image.load(fileName).convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.image = pygame.transform.scale(self.image,(100,50))
    
    