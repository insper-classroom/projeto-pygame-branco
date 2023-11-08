import pygame


class events:
  
  '''classe que analiza eventos'''
  
  def __init__(self, assets, state, clock):
    
    # keys being pressed
    self.keys = pygame.key.get_pressed()
    
    # dic with state of things
    self.state = state

    # dic with assets
    self.assets = assets
  
    self.clock = clock
    
    
  def all_events(self):
    
    '''cerebe todos os eventos do jogo e analiza para fazer acoes de acordo'''
    
    # no negative points
    if self.state['points_sr'] < 0:
      self.state['points_sr'] = 0
    
    # move crosshair 
    self.state['mouse_x'], self.state['mouse_y'] = pygame.mouse.get_pos()
    
    # all events
    for event in pygame.event.get():  

      if self.state['initial_screen'] == True:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            self.state['initial_screen'] = False 
            self.assets['button'] = self.assets['button_on']
            self.state['sr_started'] = True
            
          
          if event.key == pygame.K_BACKSPACE:
            self.state['user_input'] = self.state['user_input'][:-1]
          
          else:
            self.state['user_input'] += event.unicode
            
      elif self.state['end_game'] == False:   
        pygame.mouse.set_visible(False) 

        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            self.state['fired'] = True
            self.state['fired_mark'] = True
            self.state['fired_pos'] = event.pos
            self.assets['sound'].play()

            if self.state['target_info'][0].collidepoint(event.pos):
              self.state['hit'] = True

              if self.state['target_info'][1] == False:
                self.state['points_sr'] += 1 
                self.assets['sound2'].play()
              
              else:
                self.state['points_sr'] -= 3

      else:

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE: 
            self.state['restart'] = True
        
            
            
            
    return True


    
    