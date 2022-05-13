import pygame

pygame.init()

class Notes:
  def __init__(self):
    self.font = pygame.font.Font(None, 32)
    self.rect = pygame.Rect(475, 120, 300, 300)
    self.active_color = pygame.Color('blue')
    self.passive_color = pygame.Color('purple')
    self.active = False
    if self.active == False:
      self.color = self.passive_color
    else:
      self.color = self.active_color
    
  def txtBox(self, screen):
    pygame.draw.rect(screen,self.color,self.rect)


  def updateText(self, noteText, input):
    noteText += input
    return noteText
    
  def deleteText(self, noteText):
    noteText = noteText[:-1]
    return noteText

  def drawText(self, surface, text, aa=False, bkg=None):
    rect = self.rect
    y = rect.top
    lineSpacing = -2
    color = 'white'

    # get the height of the font
    fontHeight = self.font.size("Tg")[1]

    while text:
        i = 1

        #determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
          #print(str(rect.bottom))
          break

        # determine maximum width of line
        while self.font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            self.txtBox(surface)
            image = self.font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            self.txtBox(surface)
            image = self.font.render(text[:i], aa, color)

        surface.blit(image, (rect.x, rect.y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        #text = text[i:]

    return text
