import pygame

class events:
  
  def __init__(self, state):
    
    # keys being pressed
    self.keys = pygame.key.get_pressed()
    
    # dic with state of things
    self.state = state

  
  def all_events(self):
    
    # all events
    for event in pygame.event.get():  
      # if player kills game 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          return False
          # ----- #
    return True