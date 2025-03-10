import pygame
from circleshape import *
from constants import *

# Asteroid is based in CircleShape
class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
    
    #circle shape instead of polygon
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,  width=2)

    def update(self, dt):
        self.position += self.velocity * dt