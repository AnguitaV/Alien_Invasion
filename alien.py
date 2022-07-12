 
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class that represents a single alien in the fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        #set alien to top left of screen (top left corner = (0,0))
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store aliens exact horizontal position
        self.x = float(self.rect.x)
    
    def update(self):
        #move alien to the right or left
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right  >= screen_rect.right or self.rect.left <= 0:
            #change dir (hit an edge)
            return True



