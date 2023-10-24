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
      print(event)
      
      # if player kills game 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          return False
          # ----- #
      
      # move mouse
      if event.type == pygame.MOUSEMOTION:
        self.state['mouse_x'], self.state['mouse_y'] = event.pos
      
      if self.keys[pygame.K_w]:
        self.assets['button'] = self.assets['button_on']
      
    return True
  
  def inside_rect(m_x, m_y, rect_x, rect_y, rect_w, rect_h):
    if m_x >= rect_x and \
    m_x <= rect_x + rect_w and \
    m_y >= rect_y and \
    m_y <= rect_y + rect_h:
      return True
    return False
    
    