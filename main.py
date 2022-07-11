

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """overall class to manage game assets and behaviour:"""

    def __init__(self):
        #initialize game and create game resources:
        pygame.init()
        #create att settings as an instance of the class Settings to access the game setting methods and atts.
        self.settings = Settings()
        #create display window. set_mode(x,y) => dimensions(pixels):
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_hight = self.screen.get_rect().height
        #set title:
        pygame.display.set_caption("Alien Invasion")
        #create instance for ship while defining it as an attribute for AlienInvasion
        #This lets us access the ships attr and methods through this instance
        self.ship = Ship(self)
    
    def run_game(self):
        """start main loop for game:"""
        while True:
            #listen for keyboard and mouse events:
            self._check_events()
            self.ship.update()
            self._update_screen()

    """TIP: '_' before method name indicates it is a helper method (not meant to be called through an instance)"""

    def _check_events(self):
        """response to mouse and keyboard"""
        for event in pygame.event.get():
            #Quit
            if event.type == pygame.QUIT:
                sys.exit()
            #press key
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            #release key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

                
    def _check_keydown_events(self, event):
        #key presses.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #press Q:
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        #key releases.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        #fill screen with background color
        self.screen.fill(self.settings.bg_color)
        #draw ship at current location
        self.ship.blitme()
        #make most recently drawn screen visible:
        pygame.display.flip()



if __name__ == "__main__":
    #make game instance and run:
    ai = AlienInvasion()
    ai.run_game()

