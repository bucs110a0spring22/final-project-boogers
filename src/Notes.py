import pygame
import textwrap

pygame.init()

class Notes:
  def __init__(self):
    self.linecntr = 0
    self.char = 1
    self.linecountj = 0
    self.font = pygame.font.Font(None, 32)
    self.rect = pygame.Rect(475, 170, 300, 300)
    self.active_color = pygame.Color('blue')
    self.passive_color = pygame.Color('purple')
    self.active = False
    if self.active == False:
      self.color = self.passive_color
    else:
      self.color = self.active_color

    self.inRect = True


    
  def txtBox(self, screen):
    pygame.draw.rect(screen,self.color,self.rect)


  def updateText(self, noteText, input):
    noteText += input
    return noteText
    
  def deleteText(self, noteText): 
    noteText = noteText[:-1]
    
    return noteText

  def drawText(self, surface, text, aa=False):
    
    rect = self.rect
    y = rect.top
    x = rect.left
    lineSpacing = -2
    color = 'white'

    # get the height of the font
    fontHeight = self.font.size("Tg")[1]
    #j = 0
    
    
    while text:
        self.char = 1

        if y + fontHeight > rect.bottom:
          break

        while (self.font.size(text[:self.char])[0] < rect.width and self.char < len(text)):
            x += 1
            self.char += 1
            print("i{}".format(self.char))
            print("len{}".format(len(text)))
        
            

        
        if self.char < len(text): 
            
            print("we are in i<len(text)")
            self.char = text.rfind(" ", 0, self.char) + 1
            lineSpacing += 50
            x = rect.left
            self.char = 1

            self.linecntr += 1
            
        
        image1 = self.font.render(text[:self.char], aa, color)
        print(self.linecountj)
        surface.blit(image1, (rect.x, rect.y + self.linecountj*50))
        y += fontHeight + lineSpacing

        
        if (self.char< len(text)):
          self.linecountj += 1
        if (self.linecntr >= 1):
          break;

        
    return text
    

  def wrap_text(self, message, wraplimit):
    return textwrap.wrap(message)

  def message_display(self, surface, color, xy, wrap, message=" "):
    xy = xy[:] # so we won't modify the original values
    message = self.wrap_text(message, 10)
    for part in message.split('\n'):
         rendered_text = self.font.render(part, True, (color))
         surface.blit(rendered_text,(xy))
         xy[1] += [15, 148, 10]
         pygame.display.update()