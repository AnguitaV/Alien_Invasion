
import pygame

class Settings:

    def __init__(self):
        #initializing game settings:
        
        #SCREEN
        self.screen_width  = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)

        #ship settings:
        self.ship_limit = 3

        #bullet settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 8

        #alien settings:
        
        
        self.speed_up_scale = 1.5
        self.score_scale = 2
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed  = 1.0
        self.fleet_drop_speed = 10
        #1 = right, -1  = left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.fleet_drop_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scale)








