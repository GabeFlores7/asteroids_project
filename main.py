# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
import sys
from shot import *

def main():
    #Initialize modules, vars, and objects needed
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Create display
    clock = pygame.time.Clock() #Create time tracking object

    #Initialize Groups
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Assign groups to their respective containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

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

        for asteroid in asteroids:
            if(asteroid.collision_with(player)): #If asteroid collides with player, then "Game over!"
                sys.exit("Game over!")

            for shot in shots:
                if (asteroid.collision_with(shot)): #If asteroid collides with asteroid, then destroy both
                    asteroid.kill()
                    shot.kill()

        #Render to screen
        screen.fill("black") # fill the screen with the color black
        for obj in drawable: #Iterate over drawable group
            obj.draw(screen) #Render each player class object onto screen
        pygame.display.flip() # refresh screen

        #limit framerate to 60 FPS
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()