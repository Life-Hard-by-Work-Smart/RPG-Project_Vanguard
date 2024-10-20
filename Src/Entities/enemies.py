from common_entities import *

class Enemy(Entity):
    ...



slime_enemy = Enemy("Slime", 1, 1, 1, 1, 50)

golem_enemy = Enemy("Golem", 6, 0, 2, 6, 500)

wyvern_enemy = Enemy("Wyvern", 5, 6, 7, 16, 2000)

dragon_enemy = Enemy("Dragon", 20, 5, 10, 35, 10000)