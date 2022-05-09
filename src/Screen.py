import pygame

pygame.init()

class Screen():
  def __init__(self, r, i, c):
    self.rect = r
    self.image = i
    self.color = c
  def setColor(self, color):
    """
    sets the color of the background of the screen
    """
    return self
  def setImage(self, image):
    """
    sets the image of the background of the screen
    """
    return self