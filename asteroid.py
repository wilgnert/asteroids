from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.color = (random.randint(123, 255), random.randint(123, 255), random.randint(123, 255))

  def draw(self, screen):
    pygame.draw.circle(
      screen,  
      self.color, 
      (self.position.x, self.position.y), 
      self.radius, 
      2
    )

  def update(self, dt):
    self.position += self.velocity * dt
    
