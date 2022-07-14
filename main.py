
import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

class AlienInvasion:
    """overall class to manage game assets and behaviour:"""

    def __init__(self):
        pygame.init()
        
        #create att settings as an instance of the class Settings to access the game setting methods and atts.
        self.settings = Settings()
        #create display window
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_hight = self.screen.get_rect().height
        #set title:
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb  = ScoreBoard(self)
        
        #create instance for ship while defining it as an attribute for AlienInvasion
        #This lets us access the ships attr and methods through this instance
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #make play button
        self.play_button = Button(self, "Play")
    
    def _ship_hit(self):
        
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships(
                
            )
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _create_fleet(self):
        alien = Alien(self)
        #nmbr of aliens in one row (x)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width -  (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #detrmine nmbr of rows that fit
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_hight - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (alien_height * 2)

        #create full fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + (2 * alien_width * alien_number)
            alien.rect.x = alien.x
            alien.rect.y = alien_height + 2 * alien.rect.height * row_number 
            self.aliens.add(alien)
        
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        #check if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #same result as if ship got hit
                self._ship_hit()
                break

    def run_game(self):
        """start main loop for game:"""
        while True:
            #listen for keyboard and mouse events:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
        
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        #look for alien-ship collisisons
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #check if any aliens reach  the bottom
        self._check_aliens_bottom()

    def _update_bullets(self):
        #updates bullet position
        self.bullets.update()
        #get rid of old disapearing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        #fill screen with background color
        self.screen.fill((self.settings.bg_color))
        #draw ship at current location
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
        #make most recently drawn screen visible:
        pygame.display.flip()

    def _check_bullet_alien_collision(self):
        #check for collisions:
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.check_high_score()
        #if no more aliens:
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

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
            #press play_button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        #start a new game when player clicks play
        button_clicked =  self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.aliens.empty()
            self.bullets.empty()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        #key presses.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #press Q:
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _fire_bullet(self):
        #create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _check_keyup_events(self, event):
        #key releases.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



if __name__ == "__main__":
    #make game instance and run:
    ai = AlienInvasion()
    ai.run_game()

