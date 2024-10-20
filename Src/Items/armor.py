from common_items import * 

# třídy

class Armor(Item):
    health_modifier = 0
    
    def __init__(self, name, health_modifier, drop_chance):
        self.name = name
        self.health_modifier = health_modifier
        self.drop_chance = drop_chance        
    
class Headgear(Armor):
    equipement_type = HEADGEAR
    
    
class Chestplate(Armor):
    equipement_type = CHESTPLATE
    
    
class Leggear(Armor):
    equipement_type = LEGGEAR
    

# Slime Plains
slime_armors = []



# Golem Ruins
golem_armors = []



# Wyvern Mountains
wyvern_armors = []



# Dragon's Lair
Dragon_armors = []







## tbd:
## vytvořit konstantní instance různých armorů
## přidat je do arrays podle toho z koho padaj