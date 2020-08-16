class GameStats():
    '''Track the statistics for Space Invaders.'''
    def __init__(self,ai_settings):
        '''Initialize the statistic class.'''
        self.game_active=True
        self.ai_settings=ai_settings
        self.reset_stats()

    def reset_stats(self):
        '''Initialize statistics that can change during the game'''
        self.ships_left=self.ai_settings.ship_limit
