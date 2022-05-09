import pygame

pygame.init()

class Calendar:
  def __init__(self, d, g, x, y, h, w, i, m):
    self.date = d
    self.rect.x = x
    self.rect.y = y
    self.height = h
    self.width = w
    self.image = i
    self.weeklyOrMonthly = m
  def setWeek(self, input):
    #changes the week displayed on the calendar
    month = False
    week = True

    return self
  def setMonth(self, input):
    #changes the month displayed ont he Calendar
    week = False
    month = True
    
    
    return self
  def changeCalendar(self):
    #changes from weekly to monthly calendar and vice versa
    return self
  def createGrid(self):
    #creates a grid out of notes so that person can write on the calendar directly
    """
    calendarGrid = {}
    if (weeklyOrMonthly == "WEEKLY"):
      for i in range(7):
        d["day{}".format(i+1)] = new Notes()
    """
    return self
    