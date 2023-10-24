from constants import *
from game import *

class draw:
  def __init__(self):
    pass
  
  
  
  def draw_game(self, screen):
    screen = game().screen
  
    screen.fill(white)
  
    pygame.display.update()