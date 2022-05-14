import sys
import pygame
import pygame.gfxdraw
import random
from src import Calendar
from src import Notes
from src import Screen
from src import Button

class Controller:
  
  def __init__(self, width=800, height=625):
    '''initializes variables, objects, screen'''
    pygame.init()
    self.notChar = 1
    self.user_txt = ''
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.screen.fill((170,170,255))
    pygame.display.flip()
    #self.
    self.month = 3
    self.calendarCont = Calendar.Calendar(self.screen)
    self.calendarCont.createGrid(self.screen)
    self.calendarCont.setMonth(self.screen, self.month)

    
    pygame.font.init()
    self.todoNote = Notes.Notes()

    
    self.buttons = pygame.sprite.Group()
    self.buttons.add(Button.Button(0, 0, "assets/left_arrow.png","small"))
    self.buttons.add(Button.Button(55, 0, "assets/right_arrow.png","small"))
    self.allSprites =  pygame.sprite.Group(tuple(self.buttons)) 
    self.notesCont = Notes.Notes()
    self.notesCont.txtBox(self.screen)
    self.state = "MENU_SCREEN"

    

  
  def menuloop(self):
    '''loops the menu code and gives user interaction'''
    while self.state == "MENU_SCREEN":
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        mouse_xCor = pygame.mouse.get_pos()[0]
        mouse_yCor = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
          
            if (mouse_xCor <= 50) and (mouse_yCor <= 50):
              self.month -= 1
              if self.month >= 0:
                self.calendarCont.setMonth(self.screen, self.month)
              elif self.month < 0:
                self.month = 11
                self.calendarCont.setMonth(self.screen, self.month)
              else:
                self.month = 0
            elif (mouse_xCor>=55 and mouse_xCor<=105) and (mouse_yCor <= 50):
              self.month += 1
              if self.month<=11:
                self.calendarCont.setMonth(self.screen, self.month)
                #print(str(self.month))
              if self.month >= 12:
                self.month = 0
                self.calendarCont.setMonth(self.screen, self.month)
              else:
                self.month = 0
                
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE:
            self.user_txt = self.notesCont.deleteText(self.user_txt)
            self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)
          else: 
            if(self.notesCont.linecntr < self.notChar):
              self.user_txt = self.notesCont.updateText(self.user_txt,event.unicode)
              
              self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)
              print("lincntr{}".format(self.notesCont.linecntr))
            else:
              print("this has hit the else")
              print(self.user_txt[32:])
              self.notChar += 1
              self.user_txt = self.notesCont.updateText(self.user_txt[32*self.notesCont.linecntr:],event.unicode)
              self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)
              
          
      self.screen.blit(self.screen, (0, 0))
      self.allSprites.draw(self.screen)
      pygame.display.flip()





      
  







            
