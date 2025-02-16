from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface = screen,
            color = "white",
            center = self.position,
            radius = self.radius,
            width = 2
        )
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self): #Method to split asteroids
    
        #If asteroid is too small to split, then kill object
        if (self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return

        # Generate new angles, radii, and velocities for generated asteroids
        random_angle = random.uniform(20,50)
        new_radii = self.radius - ASTEROID_MIN_RADIUS
        new_v1 = self.velocity.rotate(random_angle)
        new_v2 = self.velocity.rotate(-random_angle)

        #Generate asteroid one of two using above arguments
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid1.velocity = new_v1 * 1.05

        #Generate asteroid two of two using above arguments
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radii)
        new_asteroid2.velocity = new_v2 * .95

        self.kill()
    