class GameStats:
    #track statistics for Alien Invasion.
    def __init__(self, ai_game):
        #initilize statistics
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        #initialize statistics that can change during the game.
        self.ships_left = self.settings.ship_limit
        
        #start Lien Invasion in an active state.
        self.game_active = True