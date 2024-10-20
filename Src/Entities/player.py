
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
    
