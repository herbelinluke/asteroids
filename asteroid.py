import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            one = random.uniform(20, 50)
            onev = self.velocity.rotate(one)
            twov = self.velocity.rotate(-one)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            a = Asteroid(self.position[0], self.position[1], new_radius)
            b = Asteroid(self.position[0], self.position[1], new_radius)
            a.velocity = onev * 1.2
            b.velocity = twov * 1.2


