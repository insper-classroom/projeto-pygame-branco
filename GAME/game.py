import pygame
from constants import *
from draw import draw
from events import *

class game:
  def __init__(self):
    pygame.init()
    
    pygame.mouse.set_visible(False)
    
    # gets the user resolution
    screen_info = pygame.display.Info() 
    screen_w, screen_h = screen_info.current_w, screen_info.current_h 

    # Inicializa a tela em tela cheia
    self.screen = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)
    
    # game name
    pygame.display.set_caption('mira vesga')
    
    # clock
    self.clock = pygame.time.Clock()
    
    # assets ---------------------------- #
    
    target = pygame.transform.scale(pygame.image.load('assets/alvo.png'), (55, 77))
    
    self.assets = {
      
      'background_sr': pygame.transform.scale(pygame.image.load('assets/fundo_shootingrange.png'), (screen_w + 100, screen_h + 155)),
      'pillars_sr': pygame.transform.scale(pygame.image.load('assets/shooting_range.png'), (screen_w + 100, screen_h - 200)),
      'box_sr': pygame.transform.scale(pygame.image.load('assets/box.png'), (screen_w + 100, 179 + 50)),
      'cars_sr': pygame.transform.scale(pygame.image.load('assets/cars.png'), (screen_w, screen_h - 100)),
      'props_sr': pygame.transform.scale(pygame.image.load('assets/props.png'), (screen_w * 0.41, (screen_h - 100) * 0.2)),
      'crosshair': pygame.image.load('assets/crosshair.png'),
      'button_off': pygame.image.load('assets/botao_off.png'),
      'button_on': pygame.image.load('assets/botao_on.png'),
      'press_w': pygame.transform.scale(pygame.image.load('assets/press_w.png'), (177, 153)),
      'button': pygame.image.load('assets/botao_off.png'),
      'target_sr': [
        pygame.transform.rotate(target, -30), # 0
        target, # 1
        target, # 2
        target, # 3
        target, # 4
        target, # 5
        pygame.transform.rotate(target, -15), # 6
        pygame.transform.rotate(target, 35), # 7
        target, # 8
        pygame.transform.rotate(target, 35), # 9 
        pygame.transform.rotate(target, -35), # 10
      ],
      'gun_sr': pygame.image.load('assets/pistol.png'),
      'bang': pygame.image.load('assets/tiro.png'),
      'bang_mark': pygame.transform.scale(pygame.image.load('assets/marca_tiro.png'), (10, 10)),
      'screen_w': screen_w,
      'screen_h': screen_h,
      
    }
    # assets ---------------------------- #
    
    
    # state ----------------------------- #
    self.state = {
      
    # if running == True, game runs
    'running': True,
    
    # mouse positioning
    'mouse_x': 0,
    'mouse_y': 0,
    
    # True == sr has started
    'sr_started': False,
    
    # if player shoots, fired = True
    'fired': False,
    'fired_mark': False,
    'fired_pos':(0, 0),
    
    # where the target is 
    'target_info': (0, 0, 55, 77),
    
    # player_points 
    'points_sr': 0
    
    }
    # state ----------------------------- #
    
  def game_loop(self):
    
    # fps
    self.clock.tick(60)
    
    # import class draw
    draw_win = draw(self.assets, self.state, self.clock)
    
    # main loop
    while self.state['running']:
      
      # import class events
      loop = events(self.assets, self.state, self.clock)
      
      # draw window
      draw_win.draw_sr(self.screen)
      
      # while running == True, loop runs
      self.state['running'] = loop.all_events()


# run the game

run = game()

run.game_loop()


