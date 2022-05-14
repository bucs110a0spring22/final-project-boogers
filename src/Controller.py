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
    #pygame.display.init()
    self.i = 1
    self.j = 0
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

    #self.calendarCont.makeCalendar(self.screen, 1, {"days":31})
    
    pygame.font.init()
    self.todoNote = Notes.Notes()

    
    self.buttons = pygame.sprite.Group()
    #self.buttons.add(Button.Button(550, 0, "assets/settings_gear.png","small"))
    self.buttons.add(Button.Button(0, 0, "assets/left_arrow.png","small"))
    self.buttons.add(Button.Button(55, 0, "assets/right_arrow.png","small"))
    #self.buttons.add(Button.Button(217, 0, "assets/monthly.png","large"))
   # self.buttons.add(Button.Button(323, 0, "assets/weekly.png","large"))
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
              #print("left button pressed!")
              self.month -= 1
              if self.month >= 0:
                self.calendarCont.setMonth(self.screen, self.month)
                #print(str(self.month))
              elif self.month < 0:
                self.month = 11
                self.calendarCont.setMonth(self.screen, self.month)
                #print(str(self.month))
              else:
                self.month = 0
                #print(str(self.month))
            elif (mouse_xCor>=55 and mouse_xCor<=105) and (mouse_yCor <= 50):
              #print("right button pressed!")
              self.month += 1
              if self.month<=10:
                self.calendarCont.setMonth(self.screen, self.month)
                #print(str(self.month))
              if self.month > 11:
                self.month = 0
                self.calendarCont.setMonth(self.screen, self.month)
                #print(str(self.month))
              else:
                self.month - 0
                #print(str(self.month))
              '''
            elif (mouse_xCor >=550 and mouse_xCor <= 600) and (mouse_yCor <= 50):
              print("settings button pressed!")
            elif (mouse_xCor >= 225 and mouse_xCor <= 325) and (mouse_yCor <= 50):
              print("monthly button pressed!")
              #self.week = -1
            elif (mouse_xCor >= 330 and mouse_xCor <= 430) and (mouse_yCor <= 50):
              
             # self.week = 
              



              
              print("weekly button pressed!")
              '''
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_BACKSPACE:
            self.user_txt = self.notesCont.deleteText(self.user_txt)
            self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)#self.notesCont.message_display(self.screen, "white", [0,0], True, self.user_txt) #self.notesCont.drawText(self.screen, self.user_txt)
          else: 
            if(self.notesCont.linecntr < self.i):
              self.user_txt = self.notesCont.updateText(self.user_txt,event.unicode)
              
              self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)
              #self.j += 1
              print("lincntr{}".format(self.notesCont.linecntr))
            else:
              print("this has hit the else")
              print(self.user_txt[32:])
              self.i += 1
              self.user_txt = self.notesCont.updateText(self.user_txt[32*self.notesCont.linecntr:],event.unicode)
              self.user_txt = self.notesCont.drawText(self.screen, self.user_txt)
              
              #self.notesCont.message_display(self.screen, "white", [0,0], True, self.user_txt) #self.notesCont.drawText(self.screen, self.user_txt)
          
      #self.buttons.update()
      self.screen.blit(self.screen, (0, 0))
      #self.buttons.draw(self.screen)
      #print("gets to this part of code")
      self.allSprites.draw(self.screen)
      pygame.display.flip()





      
  







            
