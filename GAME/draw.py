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
    
    # behind pillars and cars
    screen.blit(self.assets['target_sr'][0], (770, 520))  
    screen.blit(self.assets['target_sr'][6], (200, 520))
    screen.blit(self.assets['target_sr'][7], (450, 460)) 
    screen.blit(self.assets['target_sr'][9], (1060, 450))
    screen.blit(self.assets['target_sr'][10], (1345, 480))
    
    # gound
    screen.blit(self.assets['target_sr'][8], (980, 600))
    screen.blit(self.assets['pillars_sr'], (0, 0))
    
    # on top 
    screen.blit(self.assets['target_sr'][1], (550, 200)) 
    screen.blit(self.assets['target_sr'][2], (800, 230)) 
    screen.blit(self.assets['target_sr'][3], (950, 220)) 
    screen.blit(self.assets['target_sr'][4], (35, 250)) 
    screen.blit(self.assets['target_sr'][5], (1500, 220)) 
     
    
    screen.blit(self.assets['cars_sr'], (100, 100))
    screen.blit(self.assets['box_sr'], (0, self.assets['screen_h'] - 179))
    
    # buttons 
    screen.blit(self.assets['button'], (0, 675))
    
    # press w to start shootingrange
    if not self.state['sr_started']:
      screen.blit(self.assets['press_w'], (70, 500))
      
      
    
    # crosshair
    screen.blit(self.assets['crosshair'], (self.state['mouse_x'] - 26, self.state['mouse_y'] - 31))
    
    pygame.display.update()
    
  