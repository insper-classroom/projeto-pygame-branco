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
    
    # all events
    for event in pygame.event.get():  
      print(event)
      
      # if player kills game 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          return False
          # ----- #
      
      # move crosshair
      if event.type == pygame.MOUSEMOTION:
        self.state['mouse_x'], self.state['mouse_y'] = event.pos
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          self.assets['button'] = self.assets['button_on']
          self.state['sr_started'] = True
      if event.type == pygame.KEYUP:
        self.assets['button'] = self.assets['button_off']
        
    return True
  

    
    