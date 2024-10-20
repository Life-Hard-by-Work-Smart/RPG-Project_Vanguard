import random #teoriticky můžeme pak změnit co z toho portovat

WEAPON = 0
HEADGEAR = 1
CHESTPLATE = 2
LEGGEAR = 3


class Item:
    name = ""
    equipement_type = -1
    drop_chance = 0.0

    def __init__(self, name, damage_modifier, health_modifier, drop_chance):
        self.name = name
        self.damage_modifier = damage_modifier
        self.health_modifier = health_modifier
        self.drop_chance = drop_chance  
    
def generate_drops(enemy):
    ...

# vytvořit funkci na generování lootu z poražených enemies (vstup bude nejspíš daný nepřítel)