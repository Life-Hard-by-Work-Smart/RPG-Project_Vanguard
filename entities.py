import items

class Enemy:
    
    def update_stats(self):
        self.max_hp = self.health_lvl * 10
        self.current_hp = self.max_hp
        self.healing_amount = self.healing_lvl*self.healing_lvl
        self.damage_per_hit = self.damage_lvl * 3

    def __init__(self):
        
        
        self.update_stats()
            

class Slime(Enemy):
    drops = items.slime_drops
    def __init__(self):
        self.name = "Slime"
        self.health_lvl = 1
        self.healing_lvl = 1
        self.damage_lvl = 1
        self.lvl = 1
        self.exp = 50
        self.update_stats()

class Golem(Enemy):
    drops = items.golem_drops
    def __init__(self):
        self.name = "Golem"
        self.health_lvl = 6
        self.healing_lvl = 0
        self.damage_lvl = 2
        self.lvl = 6
        self.exp = 500
        self.update_stats()

class Wyvern(Enemy):
    drops = items.wyvern_drops
    def __init__(self):
        self.name = "Wyvern"
        self.health_lvl = 5
        self.healing_lvl = 6
        self.damage_lvl = 7
        self.lvl = 16
        self.exp = 2000
        self.update_stats()

class Dragon(Enemy):
    drops = items.dragon_drops
    def __init__(self):
        self.name = "Dragon"
        self.health_lvl = 20
        self.healing_lvl = 5
        self.damage_lvl = 10
        self.lvl = 35
        self.exp = 100000
        self.update_stats()



class Player():

    def update_stats(self, equipement_slots):
        health_modifier = 0
        damage_modifier = 0
       
        for slot in equipement_slots:
            if not slot.stored_item == None:
                health_modifier += slot.stored_item.health_modifier
                damage_modifier += slot.stored_item.damage_modifier

        self.max_hp = self.health_lvl * 10 + self.health_modifier
        self.current_hp = self.max_hp
        self.healing_amount = self.healing_lvl * self.healing_lvl
        self.damage_per_hit = self.damage_lvl * 3 + self.damage_modifier
        self.expTreshold = 100 + 50 * self.lvl


    def __init__(self, equipement_slots):
        self.lvl = 1
        self.free_skill_points = 0
        self.health_lvl = 1;
        self.damage_lvl = 1;
        self.healing_lvl = 0;
        self.exp_treshold = 100 + 50 * self.lvl

        self.update_stats(equipement_slots)
    
