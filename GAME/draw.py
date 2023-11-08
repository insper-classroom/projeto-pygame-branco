import pygame
from constants import *
from random import *

class draw:
  '''
  desenha coisas na tela, cada funcao dessa classe desenha um tipo de tela
  '''
  
  
  
  def __init__(self, assets, state, clock):
    self.assets = assets

    self.clock = clock
    
    self.state = state
    
    # to keep targets changing
    self.cronometer = 0
    
    # random number to print different targets 
    self.random_number = randint(0, 14)
    
    # when the time changes the target changes too
    self.last_target_time = - 1
    
    # makes the bullet mark and smoke appear for a certain amount of time 
    self.last_shoot_time = -1
    
    # targets organized
    self.target_list = [
      (self.assets['target_sr'][0], (770, 520)),  
      (self.assets['target_sr'][6], (200, 520)),
      (self.assets['target_sr'][7], (450, 460)),    # bottom
      (self.assets['target_sr'][9], (1060, 450)),
      (self.assets['target_sr'][10], (1400, 480)), 
      (self.assets['target_sr'][13], (1400, 480)),   # hostages
      (self.assets['target_sr'][8], (980, 600)),  
      (self.assets['target_sr'][14], (980, 600)),# --- #
      
      (self.assets['target_sr'][1], (550, 200)), 
      (self.assets['target_sr'][11], (550, 200)),                     
      (self.assets['target_sr'][2], (800, 230)),    # top
      (self.assets['target_sr'][3], (950, 220)), 
      (self.assets['target_sr'][12], (950, 220)),                     
      (self.assets['target_sr'][4], (35, 250)), 
      (self.assets['target_sr'][5], (1500, 250)), # --- #
      
    ]
  
    self.target = self.target_list[self.random_number][0]
  
  
  def draw_initial_screen(self, screen):
    '''desenha a tela inicial, onde mostra o nome do jogo'''
    
    font = pygame.font.Font(None, 36)
    
    screen.blit(self.assets['tela_inicial'], (0, 0))
    
    # player name
    name = font.render('digite seu nome: ', True, black)
    player_input = font.render(self.state['user_input'], True, black)
    screen.blit(player_input, (100, 300))
    screen.blit(name, (100, 280)) 
     
    pygame.display.update()
    
  
  def draw_sr(self, screen):
    
    '''sr significa shooting range, essa funcao desenha esta tela, que é o jogo em si'''
    
    cronometer = (self.cronometer / 1000)
    
    if cronometer > 20:
      self.state['end_game'] = True
    
    
    mouse_pos_x, mouse_pos_y = self.state['fired_pos']
    
    self.cronometer += self.clock.get_time()
    
    target_time = self.cronometer // 1000
    
    shoot_time = self.cronometer // 200
    
    target_list = self.target_list
    
    if self.last_target_time != target_time:
      self.random_number = randint(0, 14)
      self.state['hit'] = False
    self.last_target_time = target_time
    
    
    screen.fill(black)

    # background
    screen.blit(self.assets['background_sr'], (0, 0))
    screen.blit(self.assets['props_sr'], (485, 410))
    
    # behind pillars and cars
    if self.state['hit'] == False:
      if self.random_number >= 0 and self.random_number <= 7:
      
        screen.blit(target_list[self.random_number][0][0], target_list[self.random_number][1])
        self.state['target_info'] = [pygame.Rect(target_list[self.random_number][1][0], target_list[self.random_number][1][1], 55, 77), target_list[self.random_number][0][1]]
      
      
    screen.blit(self.assets['pillars_sr'], (0, 0))
    
    # on top 
    if self.state['hit'] == False:
      if self.random_number > 7 and self.random_number <= 14:
      
        screen.blit(target_list[self.random_number][0][0], target_list[self.random_number][1])
        self.state['target_info'] = [pygame.Rect(target_list[self.random_number][1][0], target_list[self.random_number][1][1], 55, 77), target_list[self.random_number][0][1]]
      
     
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
    
    # POINTS and 20s
    font = pygame.font.Font(None, 36)
    points = self.state['points_sr']
    points_text = font.render(f'Points: {points}', True, white)
    points_rect = points_text.get_rect()
    points_rect.topleft = (10, 10)
    screen.blit(points_text, points_rect)
    
    seconds_text = font.render(f'{cronometer:.2f}', True, white)
    seconds_rect = seconds_text.get_rect()
    seconds_rect.topleft = (10, 40)
    screen.blit(seconds_text, seconds_rect)
    
    pygame.display.update()
    
    
  def draw_final_screen(self, screen):
    
    '''desenha a tela final, onde mostra a pontuacao do jogador'''
    
    screen.fill(gray)
    
    points = self.state['points_sr']
    
    font = pygame.font.Font(None, 70)
    
    nome = self.state['user_input']
    
    parabens_text = font.render(f'PARABÉNS  {nome}', True, white)
    parabens_rect = parabens_text.get_rect()
    parabens_rect.topleft = (550, 200)
    screen.blit(parabens_text, parabens_rect)
    
    points_text = font.render(f'sua pontuação foi: {points}', True, white)
    points_rect = points_text.get_rect()
    points_rect.topleft = (550, 250)
    screen.blit(points_text, points_rect)
    
    screen.blit(self.assets['player'], (100, 50))
    
    pygame.display.update()