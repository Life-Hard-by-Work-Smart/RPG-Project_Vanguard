class Enemy:
    
    def update_stats(self):
        self.max_hp = self.health_lvl * 10
        self.current_hp = self.max_hp
        self.healing_amount = self.healing_lvl*self.healing_lvl
        self.damage_per_hit = self.damage_lvl * 3

    def __init__(self):
        
        
        self.update_stats()
            

class Slime(Enemy):
    name = "Slime"
    health_lvl = 1
    healing_lvl = 1
    damage_lvl = 1
    lvl = 1
    exp = 50

class Golem(Enemy):
    name = "Golem"
    health_lvl = 6
    healing_lvl = 0
    damage_lvl = 2
    lvl = 6
    exp = 500

class Wyvern(Enemy):
    name = "Wyvern"
    health_lvl = 5
    healing_lvl = 6
    damage_lvl = 7
    lvl = 16
    exp = 2000

class Dragon(Enemy):
    name = "Dragon"
    health_lvl = 20
    healing_lvl = 5
    damage_lvl = 10
    lvl = 35
    exp = 100000
