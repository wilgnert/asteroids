from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, SHOT_SPEED

class Shot(CircleShape):
  def __init__(self, x, y, direction):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = direction * SHOT_SPEED

  def draw(self, screen):
    pygame.draw.circle(
      screen, 
      "white", 
      (self.position.x, self.position.y), 
      self.radius, 
      2
    )

  def update(self, dt):
    self.position += self.velocity * dt
