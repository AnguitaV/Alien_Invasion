
import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initializing ship and starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rectangle (all images have own surface and rectangle that contains them).
        #try to save images in bmp format because pygame reads this format as default.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at bottom cebter of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store decimal value for ships horizontal position.
        self.x = float(self.rect.x)

        #movement flags:
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updates ships position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect object:
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)



