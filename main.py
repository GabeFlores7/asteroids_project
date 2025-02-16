# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
def main():
    #Initialize modules, vars, and objects needed
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Create display
    clock = pygame.time.Clock() #Create time tracking object

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0 #create delta time var

    # Print to screen upon initialization
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Create game loop
    while True:
        #Check for Player Input
        for event in pygame.event.get(): # Check if user wanted to exit the program
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable: # iterate over updatable group
            obj.update(dt) #Update each player class object

        #Render to screen
        screen.fill("black") # fill the screen with the color black
        for obj in drawable: #Iterate over drawable group
            obj.draw(screen) #Render each player class object onto screen
        pygame.display.flip() # refresh screen

        #limit framerate to 60 FPS
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()