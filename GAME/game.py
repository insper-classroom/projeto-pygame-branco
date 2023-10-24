import pygame
from constants import *
from draw import draw
from events import *

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
      'background_sr': pygame.transform.scale(pygame.image.load('../assets/fundo_shootingrange.png'), (1280, 720)),
  
    }
    # assets ---------------------------- #
    
    
    # state ----------------------------- #
    self.state = {
    'running': True
    }
    # state ----------------------------- #
    
  def game_loop(self):
    
    # import class draw
    draw_win = draw(self.assets)
    
    # main loop
    while self.state['running']:
      
      # import class events
      loop = events(self.state)
      
      # draw window
      draw_win.draw_game(self.screen)
      
      # while running == True, loop runs
      self.state['running'] = loop.all_events()
  
  
# run the game

run = game()

run.game_loop()
