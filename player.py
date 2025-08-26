import pygame
from circleshape import *
from constants import *

# Player class set up
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen): # method for drawing player to screen
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)

    def rotate(self, dt): # method for rotating player
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt): # method used to control player obj via key inputs
        keys = pygame.key.get_pressed()
        # Make game compatible for full sized or compact keyboards
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
