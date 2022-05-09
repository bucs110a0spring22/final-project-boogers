import sys
import pygame
import random
from src import Calendar
#from src import Notes
from src import Screen
from src import Button

class Controller:
  
  def __init__(self, width=400, height=400):
    pygame.init()
    #pygame.display.init()
    
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))

    self.background = pygame.Surface(self.screen.get_size()).convert()
    #self.screen = pygame.Surface(self.screen.get_size()).convert()
    self.screen.fill((133,133,255))
    pygame.display.flip()
    
    pygame.font.init()

    self.buttons = pygame.sprite.Group()
    self.buttons.add(Button.Button(200, 200, "assets/monthly_button.png"))
    print(Button.Button(200,200,"assets/left_arrow.png"))
    print(self.buttons)
    for b in self.buttons:
      print(b.rect.x)
    self.allSprites =  pygame.sprite.Group(tuple(self.buttons))   


    pygame.draw.circle(self.screen, (0,0,255), (200,200), 50, 0)
    self.state = "MENU_SCREEN"

    
    #setup pygame data
    
  #def mainloop(self):
    #select state loop
    #while True:
      #if (self.state == "MENU_SCREEN"):
       # self.menuloop
  
  ### below are some sample loop states ###
  """
  def mainloop(self):
    while True:
      if (self.state == "MENU_SCREEN"):
        self.menuloop()
  """
  
  def menuloop(self):
    while self.state == "MENU_SCREEN":
      #print("menuloop is activitated")
      #print("this is working")
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        mouse_xCor = pygame.mouse.get_pos()[0]
        mouse_yCor = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
          print("first if statement works")
          if event.button == 1:
            print("left mouse button pressed!")
      #self.buttons.update()
      self.screen.blit(self.screen, (0, 0))
      #self.buttons.draw(self.screen)
      #print("gets to this part of code")
      self.allSprites.draw(self.screen)
      pygame.display.flip()





      
  







            
      #event loop

      #update data

      #redraw
      
  #def gameloop(self):
      #event loop

      #update data

      #redraw
    
  #def gameoverloop(self):
      #event loop

      #update data

      #redraw
