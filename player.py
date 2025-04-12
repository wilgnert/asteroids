from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.rotation = 0

  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = (
      pygame.Vector2(0, 1).rotate(self.rotation + 90) * (
        self.radius / 1.5
      )
    )    
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)

  def handle_event(self, event, *args):
    pass

  def input(self, keys, **kwargs):
    if keys[pygame.K_a]:
      self.rotate(-kwargs["dt"])
    if keys[pygame.K_d]:
      self.rotate(kwargs["dt"])
    if keys[pygame.K_w]:
      self.move(kwargs["dt"])
    if keys[pygame.K_s]:
      self.move(-kwargs["dt"])
  
  def update(self, dt):
    pass
  
  def rotate(self, dt):
    self.rotation += dt * PLAYER_TURN_SPEED
    self.rotation %= 360
    
  def move(self, dt):
    self.position += (
      pygame.Vector2(0, 1).rotate(self.rotation) * dt * PLAYER_SPEED
    )