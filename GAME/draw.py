import pygame
from constants import *
from random import *

class draw:
  
  def __init__(self, assets, state, clock):
    self.assets = assets

    self.clock = clock
    
    self.state = state
    
    # to keep targets changing
    self.cronometer = 0
    
    # random number to print different targets 
    self.random_number = randint(0, 10)
    
    # when the time changes the target changes too
    self.last_target_time = - 1
    
    # makes the bullet mark and smoke appear for a certain amount of time 
    self.last_shoot_time = -1
    
    
    
    # targets organized
    self.target_list = [
      (self.assets['target_sr'][0], (770, 520)),  
      (self.assets['target_sr'][6], (200, 520)),
      (self.assets['target_sr'][7], (450, 460)), 
      (self.assets['target_sr'][9], (1060, 450)),
      (self.assets['target_sr'][10], (1345, 480)),
      (self.assets['target_sr'][8], (980, 600)),
      (self.assets['target_sr'][1], (550, 200)), 
      (self.assets['target_sr'][2], (800, 230)), 
      (self.assets['target_sr'][3], (950, 220)), 
      (self.assets['target_sr'][4], (35, 250)), 
      (self.assets['target_sr'][5], (1500, 220)),
    ]
  
    self.target = self.target_list[self.random_number][0]
  
  
  def draw_initial_screen(self, screen):
    screen.blit(self.assets['tela_inicial'], (0, 0))
    
    # press w to start shootingrange
    if not self.state['sr_started']:
      screen.blit(self.assets['press_w'], (70, 500))
      
    pygame.display.update()
    
  
  def draw_sr(self, screen):
    
    mouse_pos_x, mouse_pos_y = self.state['fired_pos']
    
    self.cronometer += self.clock.get_time()
    
    target_time = self.cronometer // 750
    
    shoot_time = self.cronometer // 200
    
    target_list = self.target_list
    
    if self.last_target_time != target_time:
      self.random_number = randint(0, 10)
      self.state['hit'] = False
    self.last_target_time = target_time
    
    
    screen.fill(black)

    # background
    screen.blit(self.assets['background_sr'], (0, 0))
    screen.blit(self.assets['props_sr'], (485, 410))
    
    # behind pillars and cars
    if self.state['hit'] == False:
      if self.random_number >= 0 and self.random_number <= 4:
      
        screen.blit(target_list[self.random_number][0], target_list[self.random_number][1])
        self.state['target_info'] = pygame.Rect(target_list[self.random_number][1][0], target_list[self.random_number][1][1], 55, 77)
      
      
    screen.blit(self.assets['pillars_sr'], (0, 0))
    
    # on top 
    if self.state['hit'] == False:
      if self.random_number > 4 and self.random_number <= 10:
      
        screen.blit(target_list[self.random_number][0], target_list[self.random_number][1])
        self.state['target_info'] = pygame.Rect(target_list[self.random_number][1][0], target_list[self.random_number][1][1], 55, 77)
      
     
    screen.blit(self.assets['cars_sr'], (100, 100))
    screen.blit(self.assets['box_sr'], (0, self.assets['screen_h'] - 179))
    
    # buttons 
    screen.blit(self.assets['button'], (0, 675))
    
    
    # crosshair
    screen.blit(self.assets['crosshair'], (self.state['mouse_x'] - 26, self.state['mouse_y'] - 31))
    
    # gun 
    if self.state['mouse_y'] >= 180:
      if self.state['fired'] == True:
        screen.blit(self.assets['bang'], (self.state['mouse_x'], self.state['mouse_y'] + 100))
        
      screen.blit(self.assets['gun_sr'], (self.state['mouse_x'] + 50, self.state['mouse_y'] + 150))
    else:
      if self.state['fired'] == True:
        screen.blit(self.assets['bang'], (self.state['mouse_x'], 300))
        
      screen.blit(self.assets['gun_sr'], (self.state['mouse_x'] + 50, 330))
    
    if self.state['fired'] == True:
      screen.blit(self.assets['bang_mark'], (mouse_pos_x - 5, mouse_pos_y - 5))
    
    if self.last_shoot_time != shoot_time:
      self.state['fired'] = False
      self.state['fired_mark'] = False
    self.last_shoot_time = shoot_time
    
    # POINTS 
    font = pygame.font.Font(None, 36)
    points = self.state['points_sr']
    points_text = font.render(f'Points: {points}', True, white)
    points_rect = points_text.get_rect()
    points_rect.topleft = (10, 10)
    screen.blit(points_text, points_rect)
    
    pygame.display.update()
    
    
  def draw_final_screen(self, screen):
    
    screen.fill(black)
    
    
    font = pygame.font.Font(None, 70)
    parabens_text = font.render('PARABÉNS', True, white)
    parabens_rect = parabens_text.get_rect()
    parabens_rect.topleft = (650, 200)
    screen.blit(parabens_text, parabens_rect)
    
    pygame.display.update()