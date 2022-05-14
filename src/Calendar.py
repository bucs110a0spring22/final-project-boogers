import pygame

pygame.init()

class Calendar:
  def __init__(self, surface):
    self.screen = surface

    self.month = False


    
    self.monthList = []
    #start day refers to the day of the week the month starts on. 1 being monday, 7 being sunday
    may22 =	{"days": 31, "title": "May 2022", "start day": 7}
    june22 =	{"days": 30, "title": "June 2022", "start day": 3}
    july22 =	{"days": 31, "title": "July 2022", "start day": 5}
    august22 =	{"days": 31, "title": "August 2022", "start day": 1}
    september22 =	{"days": 30, "title": "September 2022", "start day": 4}
    october22 =	{"days": 31, "title": "October 2022", "start day": 6}
    november22 =	{"days": 30, "title": "November 2022", "start day": 2}
    december22 =	{"days": 31, "title": "Decmber 2022", "start day": 4}
    january23 =	{"days": 31, "title": "January 2023", "start day": 7}
    february23 =	{"days": 28, "title": "February 2023", "start day": 3}
    march23 =	{"days": 31, "title": "March 2023", "start day": 3}
    april23 =	{"days": 30, "title": "April 2023", "start day": 6}
    self.monthList.append(may22)
    self.monthList.append(june22)
    self.monthList.append(july22)
    self.monthList.append(august22)
    self.monthList.append(september22)
    self.monthList.append(october22)
    self.monthList.append(november22)
    self.monthList.append(december22)
    self.monthList.append(january23)
    self.monthList.append(february23)
    self.monthList.append(march23)
    self.monthList.append(april23)







  
  def createGrid(self, surface):
    offset = 90
    rect = (5,80+offset,450,350+86)
    self.grid = pygame.gfxdraw
    self.grid.rectangle(surface,rect,(0,0,0))
    self.grid.vline(surface,65,80+offset,429+offset+86,(0,0,0))
    self.grid.vline(surface,130,80+offset,429+offset+86,(0,0,0))
    self.grid.vline(surface,195,80+offset,429+offset+86,(0,0,0))
    self.grid.vline(surface,260,80+offset,429+offset+86,(0,0,0))
    self.grid.vline(surface,325,80+offset,429+offset+86,(0,0,0))
    self.grid.vline(surface,390,80+offset,429+offset+86,(0,0,0))
    self.grid.hline(surface,5,454,166+offset,(0,0,0))
    self.grid.hline(surface,5,454,252+offset,(0,0,0))
    self.grid.hline(surface,5,454,338+offset,(0,0,0))
    self.grid.hline(surface,5,454,424+offset,(0,0,0))
    return None
    
  def dayNames(self, surface, start_date):
    self.month = False
    self.week = True
    weekdayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    if start_date == 1:
      newFont = pygame.font.Font(None, 40)
      for i in range(0, len(weekdayNames)):
        newFont = newFont.render(str(weekdayNames[i]), True, 'black')
        rect = pygame.Rect(5,139,436,41)
        pygame.draw.rect(surface,(170,170,255),rect)
        if i == 0:
          surface.blit(newFont, (5,172))
        else:
          surface.blit(newFont, (5,172+(i*86)))
    
  def setMonth(self, surface, ctr):
    self.month = True
    
    currentMonth = self.monthList[ctr]
    font = pygame.font.Font(None, 100)
    font = font.render(str(currentMonth["title"]), True, 'black')
    rect1 = pygame.Rect(5,64,600,74)
    pygame.draw.rect(surface,(170,170,255),rect1)
    surface.blit(font, (5,65))
    rect2 = pygame.Rect(5,170,450,436)
    pygame.draw.rect(surface,(170,170,255),rect2)
    self.createGrid(surface)
    self.makeCalendar(surface, ctr)
    

  def makeCalendar(self, surface, month):
    offset = 30
    weekCount = 1
    startDay = self.monthList[month]["start day"] 
    startDay = 1
    weekDay = startDay
    for i in range(1, self.monthList[month]["days"]+1):
      weekmod = (i+startDay-1)%7
      if(weekmod == 1):
        weekCount += 1
        weekDay = 1
      font = pygame.font.Font(None, 40)
      text = font.render(str(i), True, 'black')
      textRect = text.get_rect()
      textRect.center = ((weekDay*60), 70 + weekCount*86)

      weekDay += 1
      if i == 1:
        surface.blit(text, (7,142+offset))
      elif i <= 7:
        surface.blit(text, (7+(i-1)*65,142+offset))
      elif i == 8:
        surface.blit(text, (7,230+offset))
      elif i <= 14:
        surface.blit(text, (7+(i-8)*65,230+offset))
      elif i == 15:
        surface.blit(text, (7,313+offset))
      elif i <= 21:
        surface.blit(text, (7+(i-15)*65,313+offset))
      elif i == 22:
        surface.blit(text, (7,399+offset))
      elif i <= 28 and i <= self.monthList[month]["days"]:
        surface.blit(text, (7+(i-22)*65,399+offset))
      elif i == 29 and i <= self.monthList[month]["days"]:
        surface.blit(text, (7,485+offset))
      elif i <= self.monthList[month]["days"]:
        surface.blit(text, (7+(i-29)*65,485+offset))
        

    