  
import pygame

pygame.init()

class Notes:
  def __init__(self, x, y, h, w, i, f):
    self.pos = (x, y)
    self.rect = (h, w)
    self.input = i
    self.font = pygame.font.Font(f, 32)
    #self.screen = new Screen()
    self.color = "white"
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(user_text, True, (255, 255, 255))
    rect.w = max(100, text_surface.get_width()+10)

  clock = pygame.time.Clock()
  
  user_text = ''
  pygame.display.flip()

  def display(self, input):
    """
    displays what the user has inputted into the note
    """

    while True:
      for event in pygame.event.get():
        if event.key == pygame.K_BACKSPACE:
          user_text = user_text[:-1]
          else:
            user_text += event.unicode

  




    
    return self
  
