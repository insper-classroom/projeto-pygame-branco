import pygame
from constants import *


class draw:
  
  def __init__(self, assets, state):
    self.assets = assets

    self.state = state
  
  def draw_sr(self, screen):
  
    screen.fill(black)

    # background
    screen.blit(self.assets['background_sr'], (0, 0))
    screen.blit(self.assets['props_sr'], (485, 410))
    screen.blit(self.assets['pillars_sr'], (0, 0))
    screen.blit(self.assets['cars_sr'], (100, 100))
    screen.blit(self.assets['box_sr'], (0, self.assets['screen_h'] - 179))
    
    # buttons 
    # screen.blit(self.assets['button'], (0, 675))
    
    
      
    # crosshair
    screen.blit(self.assets['crosshair'], (self.state['mouse_x'] - 26, self.state['mouse_y'] - 31))
    
    pygame.display.update()
    
  