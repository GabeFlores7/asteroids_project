# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init() #initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Initialize the screen to be played on


    print("Starting asteroids!") #print information to console when starting program
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: # Game loop portion of file
        screen.fill((0,0,0)) # fill the screen with the color black
        pygame.display.flip() # refresh screen
if __name__ == "__main__":
    main()