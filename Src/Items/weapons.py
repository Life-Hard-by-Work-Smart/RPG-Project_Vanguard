from common_items import * 

# třídy

class Weapon(Item):
    equipement_type = WEAPON
    



#objekty

# Slime Plains
slime_weapons = []

slime_weapon_1 = Weapon("Half-Liquid SWord", 1, 0, 0.3)
slime_weapon_2 = Weapon("Slime Slinging Slasher", 4, 0, 0.04)

slime_weapons = [slime_weapon_1, slime_weapon_2]

# Golem Ruins
golem_weapons = []

golem_weapon_1 = Weapon("Golem's Arm", 5, 2, 0.5)
golem_weapon_2 = Weapon("Floating Boulder", 8, 5, 0.2)

golem_weapons = [golem_weapon_1, golem_weapon_2]

# Wyvern Mountains
wyvern_weapons = []

wyvern_weapon_1 = Weapon("Wyvern Incisor Dagger", 16, -5, 0.3)
wyvern_weapon_2 = Weapon("Sword of The Fallen Hero", 30, 0, 0.02)

wyvern_weapons = [wyvern_weapon_1, wyvern_weapon_2]

# Dragon's Lair
Dragon_weapons = []
 
dragon_weapon_1 = Weapon("Swift Dragon Webbing Scythe", 999, 0, 1)

Dragon_weapons = [dragon_weapon_1]

## tbd:
## vytvořit konstantní instance různých zbraní
## přidat je do arrays podle toho z koho padaj