import pygame
from constants import *


class game:
  def __init__(self):
    pygame.init()
    
    # screen size
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # game name
    pygame.display.set_caption('alpha')
    
    # clock
    self.clock = pygame.time.Clock()
    
    
    
    # assets ---------------------------- #
    self.assets = {
      
    }
    # assets ---------------------------- #
    
    
    # state ----------------------------- #
    self.state = {
    # if running == true, the game will run
    'running': True
    }
    # state ----------------------------- #
    
  def game_loop(self):
    while self.state['running']:
      self.state['running']
      draw

class events:
  
  def __init__(self):
    pass
  
  
  def all_events(self):
    
    # all events
    for event in pygame.event.get():  
      
      # if player kills game 
      if event.type == pygame.QUIT:
        return False
          # ----- #
    return True


class draw:
  def __init__(self):
    pass
  
  screen = game().screen
  
  screen.fill(white)
  
  pygame.display.update()



# run the game