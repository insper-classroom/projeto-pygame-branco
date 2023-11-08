import pygame
from constants import *
from draw import draw
from events import *

class game:
  
  '''inicializa o jogo'''
  
  def __init__(self):
    pygame.init()
    
    
    
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
    hostage = pygame.transform.scale(pygame.image.load('assets/refem.png'), (55, 77))
    
    
    self.assets = {
      
      'background_sr': pygame.transform.scale(pygame.image.load('assets/fundo_shootingrange.png'), (screen_w + 100, screen_h + 155)),
      'pillars_sr': pygame.transform.scale(pygame.image.load('assets/shooting_range.png'), (screen_w + 100, screen_h - 200)),
      'box_sr': pygame.transform.scale(pygame.image.load('assets/box.png'), (screen_w + 100, 179 + 50)),
      'cars_sr': pygame.transform.scale(pygame.image.load('assets/cars.png'), (screen_w, screen_h - 100)),
      'props_sr': pygame.transform.scale(pygame.image.load('assets/props.png'), (screen_w * 0.41, (screen_h - 100) * 0.2)),
      'crosshair': pygame.image.load('assets/crosshair.png'),
      'button_off': pygame.image.load('assets/botao_off.png'),
      'button_on': pygame.image.load('assets/botao_on.png'),
      'button': pygame.image.load('assets/botao_off.png'),
      'tela_inicial': pygame.transform.scale(pygame.image.load('assets/mira_vesga.png'), (screen_w + 100, screen_h + 155)),
      'target_sr': [
        [pygame.transform.rotate(target, -30), False], # 0
        [target, False], # 1
        [target, False], # 2
        [target, False], # 3
        [target, False], # 4
        [target, False], # 5
        [pygame.transform.rotate(target, -15), False], # 6
        [pygame.transform.rotate(target, 35), False], # 7
        [target, False], # 8
        [pygame.transform.rotate(target, 35), False], # 9 
        [target, False], # 10
        [hostage, True], # 11
        [hostage, True], # 12
        [hostage, True], # 13
        [hostage, True], # 14
      ],
      'gun_sr': pygame.image.load('assets/pistol.png'),
      'bang': pygame.image.load('assets/tiro.png'),
      'bang_mark': pygame.transform.scale(pygame.image.load('assets/marca_tiro.png'), (10, 10)),
      'player': pygame.image.load('assets/player.png'),
      'screen_w': screen_w,
      'screen_h': screen_h,
      'sound': pygame.mixer.Sound('assets/tiro.mp3'),
      'sound2': pygame.mixer.Sound('assets/certo.mp3')
      
    }
    # assets ---------------------------- #
    
    
    # state ----------------------------- #
    self.state = {

    'initial_screen': True,
    
    # player name
    'user_input': '',
      
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
    'hit': False,
    
    # where the target is 
    'target_info': (0, 0, 55, 77),
    
    # player_points 
    'points_sr': 0,
    
    'end_game': False,
    
    'restart': False
    
    }
    # state ----------------------------- #
    
  def game_loop(self):
    
    '''loop principal do jogo, carrega a classe desenha e eventos para gerar as interacoes e rodar o jogo'''
    
    # fps
    self.clock.tick(60)
    
    # import class draw
    draw_win = draw(self.assets, self.state, self.clock)
    
    # main loop
    while self.state['running']:
      # import class events
      loop = events(self.assets, self.state, self.clock)

      # while running == True, loop runs
      self.state['running'] = loop.all_events()
        
      # draw window
      if self.state['end_game'] == False:
      
        if self.state['initial_screen'] == True:
          draw_win.draw_initial_screen(self.screen)
        else:
          draw_win.draw_sr(self.screen)
      
      else:
        draw_win.draw_final_screen(self.screen)
        if self.state['restart'] == True:
          run = game()

          run.game_loop()
      
# run the game

run = game()

run.game_loop()
