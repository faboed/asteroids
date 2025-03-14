# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

#starts/ initiates the pygame module
pygame.init()

#keeps track of time to be used for limiting FPS
clock = pygame.time.Clock()
dt = 0 #delta time as initial variable

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#while loop creates the window with Width and Height, fills it black and refreshes it with .flip
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #groups for the loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for entitiy in drawable:
            entitiy.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collision(player) == False:
                raise SystemExit("Game over!")

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot) == False:
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        dt = clock.tick(60) / 1000 #60 frames per second

        updatable.update(dt)
        player.timer -= dt

if __name__ == "__main__":
    main()