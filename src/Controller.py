import sys
import pygame
import pygame.gfxdraw
import random
from src import Calendar
from src import Notes
from src import Screen
from src import Button

class Controller:
  
  def __init__(self, width=800, height=600):
    '''initializes variables, objects, screen'''
    pygame.init()
    #pygame.display.init()
    self.user_txt = ''
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))

    self.background = pygame.Surface(self.screen.get_size()).convert()
    #self.screen = pygame.Surface(self.screen.get_size()).convert()
    self.screen.fill((170,170,255))
    pygame.display.flip()

    self.month = 0
    self.calendarCont = Calendar.Calendar(self.screen)
    self.calendarCont.createGrid(self.screen)
    self.calendarCont.setMonth(self.screen, self.month)

    #self.calendarCont.makeCalendar(self.screen, 1, {"days":31})
    
    pygame.font.init()
    
    self.buttons = pygame.sprite.Group()
    self.buttons.add(Button.Button(550, 0, "assets/settings_gear.png","small"))
    self.buttons.add(Button.Button(0, 0, "assets/left_arrow.png","small"))
    self.buttons.add(Button.Button(55, 0, "assets/right_arrow.png","small"))
    self.buttons.add(Button.Button(217, 0, "assets/monthly.png","large"))
    self.buttons.add(Button.Button(323, 0, "assets/weekly.png","large"))
    self.allSprites =  pygame.sprite.Group(tuple(self.buttons)) 
    self.notesCont = Notes.Notes()
    self.notesCont.txtBox(self.screen)
    self.state = "MENU_SCREEN"

    

  
  def menuloop(self):
    '''loops the menu code and gives user interaction'''
    while self.state == "MENU_SCREEN":
      #print("menuloop is activitated")
      #print("this is working")

      #if(pygame.sprite.collide_rect( self.buttons[1].rect(), pygame.mouse.get_pos())):
        #print("clicking left button")
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        mouse_xCor = pygame.mouse.get_pos()[0]
        mouse_yCor = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if (mouse_xCor <= 50) and (mouse_yCor <= 50):
              print("left button pressed!")
              self.calendarCont.setMonth(self.screen, self.month + 1)
              self.month += 1
              
            elif (mouse_xCor>=55 and mouse_xCor<=105) and (mouse_yCor <= 50):
              print("right button pressed!")
            elif (mouse_xCor >=550 and mouse_xCor <= 600) and (mouse_yCor <= 50):
              print("settings button pressed!")
            elif (mouse_xCor >= 225 and mouse_xCor <= 325) and (mouse_yCor <= 50):
              print("monthly button pressed!")
            elif (mouse_xCor >= 330 and mouse_xCor <= 430) and (mouse_yCor <= 50):
              print("weekly button pressed!")
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE:
            self.user_txt = self.notesCont.deleteText(self.user_txt)
            self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)
          else: 
            self.user_txt = self.notesCont.updateText(self.user_txt,event.unicode)
            self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)
          
      #self.buttons.update()
      self.screen.blit(self.screen, (0, 0))
      #self.buttons.draw(self.screen)
      #print("gets to this part of code")
      self.allSprites.draw(self.screen)
      pygame.display.flip()





      
  







            
