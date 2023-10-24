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
  
  
# run the game

run = game()

run.game_loop()