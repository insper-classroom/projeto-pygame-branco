import pygame

class events:
  
  def __init__(self, assets, state, clock):
    
    # keys being pressed
    self.keys = pygame.key.get_pressed()
    
    # dic with state of things
    self.state = state

    # dic with assets
    self.assets = assets
  
    self.clock = clock
    
  def all_events(self):
    
    # move crosshair 
    self.state['mouse_x'], self.state['mouse_y'] = pygame.mouse.get_pos()
    
    # all events
    for event in pygame.event.get():  
      print(event)
      
      # if player kills game 
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_RETURN:
          self.state['initial_screen'] = True 

        if event.key == pygame.K_ESCAPE:
          return False
          # ----- #
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          self.assets['button'] = self.assets['button_on']
          self.state['sr_started'] = True
        
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          self.state['fired'] = True
          self.state['fired_mark'] = True
          self.state['fired_pos'] = event.pos

          if self.state['target_info'].collidepoint(event.pos):
            print('ACERTOU')
            self.state['points_sr'] += 1 
          
    return True


    
    