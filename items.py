import random 

# třídy

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
    drops = []
    for enemy_drop in enemy.drops:
        if enemy_drop.drop_chance > random.random():
                drops.append(enemy_drop)
    return drops


class Headgear(Item):
    equipement_type = HEADGEAR
    
    
class Chestplate(Item):
    equipement_type = CHESTPLATE
    
    
class Leggear(Item):
    equipement_type = LEGGEAR

class Weapon(Item):
    equipement_type = WEAPON




# Slime Plains

slime_headgear_1 = Headgear("Bouncy Helmet", 0, 3, 0.3)
slime_headgear_2 = Headgear("Gooey Helmet", 0, 5, 0.08)
slime_chestplate_1 = Chestplate("Bouncy Chestplate", 0, 6, 0.3)
slime_chestplate_2 = Chestplate("Gooey Chestplate", 0, 10, 0.08)
slime_leggear_1 = Leggear("Bouncy Leggings", 0, 3, 0.3)
slime_leggear_2 = Leggear("Gooey Leggings", 0, 5, 0.08)

slime_weapon_1 = Weapon("Half-Liquid SWord", 1, 0, 0.3)
slime_weapon_2 = Weapon("Slime Slinging Slasher", 4, 0, 0.04)

slime_drops = [slime_headgear_1, slime_headgear_2, slime_chestplate_1, slime_chestplate_2, slime_leggear_1, slime_leggear_2, slime_weapon_1, slime_weapon_2]

# Golem Ruins

golem_headgear_1 = Headgear("Rock with eyelids", -2, 8, 0.5) 
golem_headgear_2 = Headgear("Living Helmet", 0, 8, 0.05)
golem_chestplate_1 = Chestplate("Rocklike Chestplate", -4, 16, 0.5)
golem_chestplate_2 = Chestplate("Living Chestplate", 0, 16, 0.05)
golem_leggear_1 = Leggear("Rocks glued to legs", -2, 8, 0.5)
golem_leggear_2 = Leggear("Living Leggings", 0, 8, 0.05)

golem_weapon_1 = Weapon("Golem's Arm", 5, 2, 0.5)
golem_weapon_2 = Weapon("Floating Boulder", 8, 5, 0.2)

golem_drops = [golem_headgear_1, golem_headgear_2, golem_chestplate_1, golem_chestplate_2, golem_leggear_1, golem_leggear_2, golem_weapon_1, golem_weapon_2]
# Wyvern Mountains

wyvern_headgear_1 = Headgear("Scale Helmet", 0, 15, 0.3)
wyvern_headgear_2 = Headgear("Bacta Helmet", 0, 20, 0.06)
wyvern_chestplate_1 = Chestplate("Scale Chestplate", 0, 30, 0.3)
wyvern_chestplate_2 = Chestplate("Bacta Chestplate", 0, 40, 0.06)
wyvern_leggear_1 = Leggear("Scale Leggings", 0, 15, 0.3)
wyvern_leggear_2 = Leggear("Bacta Leggings", 0, 20, 0.06)

wyvern_weapon_1 = Weapon("Wyvern Incisor Dagger", 16, -5, 0.3)
wyvern_weapon_2 = Weapon("Sword of The Fallen Hero", 30, 0, 0.02)

wyvern_drops = [wyvern_headgear_1, wyvern_headgear_2, wyvern_chestplate_1, wyvern_chestplate_2, wyvern_leggear_1, wyvern_leggear_2, wyvern_weapon_1, wyvern_weapon_2]

# Dragon's Lair

dragon_headgear = Headgear("Melted Dragon Slayer Helmet", 999, -4, 1)
dragon_chestplate = Chestplate( "Triumph of the Dragon's Lair Chestplate", -100, 20, 1)
dragon_leggear = Leggear("Ice Walker Leggings", 0, 300, 1)

dragon_weapon_1 = Weapon("Swift Dragon Webbing Scythe", 999, 0, 1)

dragon_drops = [dragon_headgear, dragon_chestplate, dragon_leggear, dragon_weapon_1]