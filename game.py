import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

class Game:
  __screen_width = SCREEN_WIDTH
  __screen_height = SCREEN_HEIGHT
  __screen: pygame.Surface = None
  __is_running: bool = False
  __clock: pygame.time.Clock = None
  __player: Player = None
  __updatable: pygame.sprite.Group = None
  __drawable: pygame.sprite.Group = None
  __inputable: pygame.sprite.Group = None
  __asteroids: pygame.sprite.Group = None
  __dt = 0

  def run():
    if Game.__is_running:
      return
    Game.__is_running = True
    pygame.init()
    Game.__screen = pygame.display.set_mode(
      (Game.__screen_width, Game.__screen_height)
    )
    Game.__clock = pygame.time.Clock()
    Game.__dt = 0
    Game.__updatable = pygame.sprite.Group()
    Game.__drawable = pygame.sprite.Group()
    Game.__inputable = pygame.sprite.Group()
    Game.__asteroids = pygame.sprite.Group()
    Player.containers = Game.__updatable, Game.__drawable, Game.__inputable
    Game.__player = Player(
      Game.__screen_width // 2,
      Game.__screen_height // 2,
      PLAYER_RADIUS
    )
    Asteroid.containers = Game.__updatable, Game.__drawable, Game.__asteroids
    AsteroidField.containers = Game.__updatable
    AsteroidField()

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
    keys = pygame.key.get_pressed()
    for inputable in Game.__inputable:
      inputable.input(keys, dt=Game.__dt)

  def __update():
    for updatable in Game.__updatable:
      updatable.update(Game.__dt)
      
    Game.__dt = Game.__clock.tick(60) / 1000.0

    for asteroid in Game.__asteroids:
      if asteroid.collide(Game.__player):
        print("Game over!")
        pygame.quit()
        exit()


  def __render():
    Game.__screen.fill((0, 0, 0))  # Fill the screen with black
    for drawable in Game.__drawable:
      drawable.draw(Game.__screen)
    

    pygame.display.flip()  # Update the display
    return