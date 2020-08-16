
class Settings():
    '''A class to store all settings fo Alien Invasion.'''

    def __init__(self):
        '''Initialize setting class'''

        #Screen settings-------------------------------------------------
        self.screen_width=720
        self.screen_height=600
        self.bg_color=(230,230,230)

        #Ship settings-----------------------------------------------------
        self.ship_speed=0.75#pixels per loop
        self.ship_limit=3
        
        #Bullets settings--------------------------------------------------
        self.bullet_width=5
        self.bullet_height=10
        self.bullet_color=(0,0,0)
        self.bullet_speed=1
        self. bullets_allowed=3

        #Aliens settings-----------------------------------------------------
        self.alien_speed=0.75
        self.fleet_drop_speed=10
        #fleet_direction of 1 -->,   fleet direction of -1 <--
        self.fleet_direction=1

        #Stars settings-------------------------------------------------------
        self.stars_number=10
        self.star_speed=0.25 