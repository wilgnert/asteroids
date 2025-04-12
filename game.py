import pygame
from constants import *

class Game:
  screen_width = SCREEN_WIDTH
  screen_height = SCREEN_HEIGHT
  screen = None
  __is_running = False

  def run():
    if Game.__is_running:
      return
    Game.__is_running = True
    pygame.init()
    Game.screen = pygame.display.set_mode((Game.screen_width, Game.screen_height))
    while True:
      Game.__handle_events()
      Game.__input()
      Game.__update()
      Game.__render()
  
  def __handle_events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

  def __input():
    pass

  def __update():
    pass

  def __render():
    Game.screen.fill((0, 0, 0))  # Fill the screen with black
    

    pygame.display.flip()  # Update the display
    return