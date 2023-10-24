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
    pass

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



# run the game