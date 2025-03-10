import pygame
import random
from circleshape import *
from constants import *

# Asteroid is based in CircleShape
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    #circle shape instead of polygon
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,  width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector_one * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = vector_two * 1.2

        self.kill()