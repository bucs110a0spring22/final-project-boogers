import pygame

pygame.init()

class Screen():
  def __init__(self, r, i, c):
    self.rect = r
    self.image = i
    self.color = c
  