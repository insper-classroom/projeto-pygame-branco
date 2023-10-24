import pygame
from game import *

class events:
  
  def __init__(self):
    pass
  
  
  def all_events(self):
    
    # all events
    for event in pygame.event.get():  
      
      # if player kills game 
      if event.type == pygame.QUIT:
        return False
          # ----- #
    return True