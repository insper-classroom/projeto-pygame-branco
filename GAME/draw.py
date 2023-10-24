import pygame
from constants import *


class draw:
  
  def __init__(self, assets):
    self.assets = assets
  
  
  def draw_game(self, screen):
  
    screen.fill(white)
  
    pygame.display.update()
    
  