import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
  def __init__(self, x, y, fileName):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(fileName).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    #self.input = i
    #self.leftSprite = left_img
    #self.rightSprite = right_img
  def display(self, input):
    """
    displays what the user has inputted into the note
    """
    return self
  def switch(self, calendar, screen):
    """
    switches between calendar types if it returns true or false
    """
    #self.hero.draw(self.screen)
    return self
