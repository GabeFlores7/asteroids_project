# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():

    pygame.init() #initialize pygame
    clock = pygame.time.Clock() # initialize object to keep track of time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # create object for display
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # initialize player obj to screen's center
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: # run game indefinitely

        for event in pygame.event.get(): # check if user exits
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0)) # make the screen black (r,g,b)
        player.draw(screen) # draw player to screen

        player.update(dt) # update player behavior 
        pygame.display.flip() # update screen

        clock.tick(60) # pause loop for 1/60th of a second (i.e. 60fps)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
