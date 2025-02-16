from circleshape import *
from constants import *

#Create 'Player' class that inherits from 'CircleShape' class
class Player(CircleShape): 
    def __init__(self, x, y): # x,y should be int data types
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
        surface = screen, 
        color = "white", 
        points = self.triangle(), 
        width = 2
        )