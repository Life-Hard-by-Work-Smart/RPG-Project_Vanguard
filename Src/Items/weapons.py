from common_items import * 

# třídy

class weapon(Item):
    damage_modifier = 0
    equipement_type = WEAPON
    
    def __init__(self, name, damage_modifier, drop_chance):
        self.name = name
        self.health_modifier = damage_modifier
        self.drop_chance = drop_chance 

# Slime Plains
slime_weapons = []



# Golem Ruins
golem_weapons = []



# Wyvern Mountains
wyvern_weapons = []



# Dragon's Lair
Dragon_weapons = []
 
        
## tbd:
## vytvořit konstantní instance různých zbraní
## přidat je do arrays podle toho z koho padaj