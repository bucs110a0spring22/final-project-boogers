import pygame

pygame.init()

class Calendar:
  def __init__(self, surface):
    self.screen = surface
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
    february23 =	{"days": 31, "title": "February 2023", "start day": 3}
    march23 =	{"days": 31, "title": "March 2023", "start day": 3}
    april23 =	{"days": 31, "title": "April 2023", "start day": 6}
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
    
  def setWeek(self, input):
    #changes the week displayed on the calendar
    month = False
    week = True

    return self
  def setMonth(self, surface, ctr=0):
    #changes the month displayed ont he Calendar
    #ctr = 0
    currentMonth = self.monthList[ctr]
    self.makeCalendar(surface,currentMonth["start day"], currentMonth)
    font = pygame.font.Font(None, 100)
    font = font.render(str(currentMonth["title"]), True, 'black')
    surface.blit(font, (5,65))
    
    
    
    return self

  def makeCalendar(self, surface, startDay=1, month={"days": 31, "title": "January 2023"}):
    #startDay is the day of the week that our month starts on
    print("bruh")
    print(month.get("days"))
    """
    month = self.monthList[9]
    if(monthName == "february"):
      month = self.monthList[10]
    """

    weekCount = 1
    weekDay = startDay
    for i in range(1, month["days"]):#month["days"]):
      weekmod = (i+startDay-1)%7
      if(weekmod == 1):
        weekCount += 1
        weekDay = 1
      
      #print("hell yeah")
      font = pygame.font.Font(None, 50)
      text = font.render(str(i), True, 'black')
      textRect = text.get_rect()
      textRect.center = ((weekDay*60), 70 + weekCount*85)
      #print(40 + weekCount*70)
      weekDay += 1
      surface.blit(text, textRect)
    
  def changeCalendar(self):
    
    #if(pygame.sprite.collide_rect())    
    #changes from weekly to monthly calendar and vice versa
    return self

  # def createGrid(self, surface):
  #   #creates a grid out of notes so that person can write on the calendar directly
  #   rect = (400,400)
  #   pygame.gfxdraw.rectangle(surface,rect,(255,255,255))
  #   """
  #   calendarGrid = {}
  #   if (weeklyOrMonthly == "WEEKLY"):
  #     for i in range(7):
  #       d["day{}".format(i+1)] = new Notes()
  #   """
  #   return self
  def createGrid(self, surface):
    offset = 60
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
    