"""tracks statistics for space invaders"""

class GameStats:

    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()
        self.high_score = 0
        


    def reset_stats(self):
        #initialize changing stats
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

