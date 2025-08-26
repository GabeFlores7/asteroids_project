import pygame
from circleshape import *

# Asteroid class set up
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen): # method for drawing asteroid to screen
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt): # method for changing behavior of asteroid
        self.position += self.velocity * dt