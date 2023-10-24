import pygame
from constants import *


class draw:
  
  def __init__(self, assets):
    self.assets = assets
  
  
  def draw_game(self, screen):
  
    screen.fill(black)

    screen.blit(self.assets['background_sr'], (0, 0))
    
    pygame.display.update()
    
  