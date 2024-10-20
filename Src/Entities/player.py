from common_entities import *

class Player(Entity):
    exp_treshold = 0
    free_skill_points = 0

    def UpdateStats():
        ... 


    def __init__(self):
        self.lvl = 1
        self.free_skill_points = 0
        self.health_lvl = 1;
        self.damage_lvl = 1;
        self.healing_lvl = 0;
        self.expTreshold = 100 + 50 * self.lvl