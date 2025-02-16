from circleshape import *
from constants import *
from main import *
from shot import *

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
    
    def draw(self, screen): #Draw player to screen
        pygame.draw.polygon(
        surface = screen, 
        color = "white", 
        points = self.triangle(), 
        width = 2
        )

    def update(self, dt): #Update values based on key inputs
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def rotate(self, dt): #Rotate player
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt): #Move player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt): #Shoot ability
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        