import pygame
import textwrap

pygame.init()

class Notes:
  def __init__(self):
    self.font = pygame.font.Font(None, 32)
    self.rect = pygame.Rect(475, 170, 300, 300)
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

  def drawText(self, surface, text, aa=False):
    #xy = xy[:]
    
    rect = self.rect
    y = rect.top
    x = rect.left
    lineSpacing = -2
    color = 'white'

    # get the height of the font
    fontHeight = self.font.size("Tg")[1]
    j = 0
    
    
    while text:
        i = 1

        #determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
          #print(str(rect.bottom))
          break

        # determine maximum width of line
        while (self.font.size(text[:i])[0] - j*294 < rect.width and i < len(text)):
            print(self.font.size(text[:i])[0] - j*294)  
            x += 1
            i += 1
        
            
        
        """
        if self.font.size(text[:i])[0] > rect.width:
          i = text.rfind(" ", 0, i) + 1
            lineSpacing += 50
            x = rect.left
            i = 1
            j += 1
        """
        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            print("we are in i<len(text)")
            i = text.rfind(" ", 0, i) + 1
            lineSpacing += 50
            x = rect.left
            i = 1
            j += 1
            print("j: {}".format(j))
            #self.drawText(surface, text)
        else:
            #message = new font object
            #font object.y + 10
            #
          
      

        # render the line and blit it to the surface      
        self.txtBox(surface)
        image = self.font.render(text[:i], aa, color)

        surface.blit(image, (rect.x, rect.y + j*50))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        #text = text[i:]
    #print(text)
    return text
    

  def wrap_text(self, message, wraplimit):
    #textwrapp = textwrap.TextWrapper()
    return textwrap.wrap(message)

  def message_display(self, surface, color, xy, wrap, message=" "):
    xy = xy[:] # so we won't modify the original values
    message = self.wrap_text(message, 10)
    for part in message.split('\n'):
         rendered_text = self.font.render(part, True, (color))
         surface.blit(rendered_text,(xy))
         xy[1] += [15, 148, 10]
         pygame.display.update()