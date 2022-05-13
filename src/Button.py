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
    
    #self.input = i
    #self.leftSprite = left_img
    #self.rightSprite = right_imgt

  def display(self, input):
    
    """
    displays what the user has inputted into the note
    """
    return self
  def switch(self, calendar, screen):
    """
    switches between calendar types if it returns true or false
    """
    #if (weekly) == True:
    #    pass
    #elif (monthly) == True:
    #    pass
    #return self
  