import pygame
from constants import *

class Game:
  __screen_width = SCREEN_WIDTH
  __screen_height = SCREEN_HEIGHT
  __screen: pygame.Surface = None
  __is_running: bool = False
  __clock: pygame.time.Clock = None
  __dt = 0
  __t = 0

  def run():
    if Game.__is_running:
      return
    Game.__is_running = True
    pygame.init()
    Game.__screen = pygame.display.set_mode((Game.__screen_width, Game.__screen_height))
    Game.__clock = pygame.time.Clock()
    Game.__dt = 0
    Game.__t = 0


    Game.__loop()
  
  def __loop():
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
    Game.__dt = Game.__clock.tick(60) / 1000.0

  def __render():
    Game.__screen.fill((0, 0, 0))  # Fill the screen with black
    font = pygame.font.Font(None, 36)
    text = font.render(f"Deltatime: {int(Game.__dt * 1000)} ms", True, (255, 255, 255))
    text_rect = text.get_rect(center=(Game.__screen_width // 2, Game.__screen_height // 2)) 
    Game.__screen.blit(text, text_rect)  # Draw the text on the screen
    

    pygame.display.flip()  # Update the display
    return