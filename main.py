
#sys imports tools to quit game and exit program
import sys

#pygame module imports functionality for games (screen, graphics, etc.)
import pygame

class AlienInvasion:
    #overall class to manage game assets and behaviour:

    def __init__(self):
        #initialize game and create game resources:
        pygame.init()
        #set background color (RGB values => red, green and blue tones mix)
        # RGB values =>(0, 255):
        #RED = (255, 0, 0)
        #GREEN = (0, 255, 0)
        #BLUE = (0, 0, 255)
        self.bg_color = (230, 230, 255)

        #create display window. set_mode(x,y) => dimensions(pixels):
        self.screen = pygame.display.set_mode((1300,950))
        #set title:
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        #start main loop for game:
        while True:
            #listen for keyboard and mouse events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw screen during each pass through the loop
            self.screen.fill(self.bg_color)

            #make most recently drawn screen visible:
            pygame.display.flip()


if __name__ == "__main__":
    #make game instance and run:
    ai = AlienInvasion()
    ai.run_game()

