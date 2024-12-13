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
        self.xp = 50
        self.update_stats()

class Golem(Enemy):
    drops = items.golem_drops
    def __init__(self):
        self.name = "Golem"
        self.health_lvl = 6
        self.healing_lvl = 0
        self.damage_lvl = 2
        self.lvl = 6
        self.xp = 500
        self.update_stats()

class Wyvern(Enemy):
    drops = items.wyvern_drops
    def __init__(self):
        self.name = "Wyvern"
        self.health_lvl = 5
        self.healing_lvl = 6
        self.damage_lvl = 7
        self.lvl = 16
        self.xp = 2000
        self.update_stats()

class Dragon(Enemy):
    drops = items.dragon_drops
    def __init__(self):
        self.name = "Dragon"
        self.health_lvl = 20
        self.healing_lvl = 5
        self.damage_lvl = 10
        self.lvl = 35
        self.xp = 100000
        self.update_stats()



class Player():

    def bombice(self):
        print("bombice")

    def update_stats(self, equipement_slots: dict):
        self.health_modifier = 0
        self.damage_modifier = 0
       
        for slot in equipement_slots.values():
            if not slot.item == None:
                self.health_modifier += slot.item.health_modifier
                self.damage_modifier += slot.item.damage_modifier

        self.max_hp = self.health_lvl * 10 + self.health_modifier
        self.healing_amount = self.healing_lvl * self.healing_lvl
        self.damage_per_hit = self.damage_lvl * 3 + self.damage_modifier
        self.expTreshold = 100 + 50 * self.lvl
        self.bombice()

    def lvl_up(self):
        self.max_heal()
        self.lvl += 1
        self.free_skill_points += 1
        self.xp -= self.xp_treshold
        if self.xp >= self.xp_treshold:
            self.lvl_up()

    def gain_xp(self, gained_xp):
        self.xp += self.xp + gained_xp 
        if self.xp >= self.xp_treshold:
            self.lvl_up()

    def max_heal(self):
        self.current_hp = self.max_hp

    def __init__(self, name, equipement_slots):
        self.name = name
        self.lvl = 1
        self.free_skill_points = 0
        self.health_lvl = 1
        self.damage_lvl = 1
        self.healing_lvl = 0
        self.xp = 0
        self.xp_treshold = 100 + 50 * self.lvl

        self.update_stats(equipement_slots)
        self.max_heal()


