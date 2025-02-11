# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	background_color = (0,0,0)
	clock = pygame.time.Clock()
	dt = 0
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill(background_color)
		pygame.display.flip()
		dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()

