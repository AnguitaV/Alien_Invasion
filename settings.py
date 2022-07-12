
import pygame

class Settings:

    def __init__(self):
        #initializing game settings:
        #SCREEN
        self.screen_width  = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)

        #ship settings:
        self.ship_speed = 1.5

        #bullet settings:
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 8

        #alien settings:
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #1 = right, -1  = left.
        self.fleet_direction = 1







