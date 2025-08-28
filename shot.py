import pygame
from circleshape import *
from constants import *

# shot class set up
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen): # method for drawing asteroid to screen
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
    
    def update(self, dt): # method for changing behavior of asteroid
        self.position += self.velocity * dt
