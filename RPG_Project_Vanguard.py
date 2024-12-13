import pygame
import os
import entities
import gui_objects
import inventory
import gui_objects
import items
import map_objects

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0

player = entities.Player("Burymuru", inventory.equipement_cells)
enemy = None

# various fonts
inventory_cell_font = pygame.font.SysFont("Consolas", 15)
common_button_font = pygame.font.SysFont("Consolas", 25)
fight_font = pygame.font.SysFont("Consolas", 35)

# asset loading
def load_asset(path: str):
        return pygame.Surface.convert(pygame.image.load(path))

dirname = os.path.dirname(__file__)

camp_background_dir = os.path.join(dirname, fr"Assets\pics\Mapa_RPG-P.V._v1.0.0.png")
slime_plains_background_dir = os.path.join(dirname, fr"Assets\pics\slimeplains.png")
golem_ruins_background_dir = os.path.join(dirname, fr"Assets\pics\golemruins.png")
wyvern_mountains_background_dir = os.path.join(dirname, fr"Assets\pics\wyvernmountains.png")
dragon_lair_background_dir = os.path.join(dirname, fr"Assets\pics\dragonlair.png")
player_image_dir = os.path.join(dirname, fr"Assets\pics\tucnak_warm.png")

camp_background = load_asset(camp_background_dir)
slime_plains_background = load_asset(slime_plains_background_dir)
golem_ruins_background = load_asset(golem_ruins_background_dir)
wyvern_mountains_background = load_asset(wyvern_mountains_background_dir)
dragon_lair_background = load_asset(dragon_lair_background_dir)
player_image = load_asset(player_image_dir)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# vars and constants for button screens




## vars and constants for menu

menu_buttons = {}

menu_buttons["back to last screen"] = pygame.Rect(540, 310, 300, 80)

## vars and constants for inventory

### backpack
backpack_cells = {}
backpack_cells.update(inventory.inventory_cells)
backpack_cells.update(inventory.equipement_cells)


### chest
chest_cells = {}
chest_cells.update(inventory.inventory_cells)
chest_cells.update(inventory.chest_cells)

other_chest_buttons = {}
other_chest_buttons["back_to_game"] = gui_objects.Common_back_button(1000, 20)

all_chest_butons = {}
all_chest_butons.update(chest_cells)
all_chest_butons.update(other_chest_buttons)

## vars and constants for combat


combat_buttons = {}
combat_buttons["Attack"] = gui_objects.Common_menu_button(95*1 + (gui_objects.Common_menu_button.common_width) * 0, screen.get_height() - gui_objects.Common_menu_button.common_height - 50)
combat_buttons["Heal"] = gui_objects.Common_menu_button(95*2 + (gui_objects.Common_menu_button.common_width) * 1, screen.get_height() - gui_objects.Common_menu_button.common_height - 50)
combat_buttons["Flee"] = gui_objects.Common_menu_button(95*3 + (gui_objects.Common_menu_button.common_width) * 2, screen.get_height() - gui_objects.Common_menu_button.common_height - 50)

##vars and constants for skill screen

skill_buttons = {}
skill_buttons["health_lvl_add"] = gui_objects.Skill_modify_button(425,      25 + 40*10, 1)
skill_buttons["health_lvl_sub"] = gui_objects.Skill_modify_button(425 + 40, 25 + 40*10, -1)
skill_buttons["damage_lvl_add"] = gui_objects.Skill_modify_button(425,      25 + 40*11, 1)
skill_buttons["damage_lvl_sub"] = gui_objects.Skill_modify_button(425 + 40, 25 + 40*11, -1)
skill_buttons["healing_lvl_add"] = gui_objects.Skill_modify_button(425,      25 + 40*12, 1)
skill_buttons["healing_lvl_sub"] = gui_objects.Skill_modify_button(425 + 40, 25 + 40*12, -1)

other_skill_buttons = {}
other_skill_buttons["back_to_game"] = gui_objects.Common_back_button(1000, 20)

all_skill_buttons = {}
all_skill_buttons.update(skill_buttons)
all_skill_buttons.update(other_skill_buttons)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# vars and constants for movement screen




## maps
map_border = pygame.Rect(5, 5, 1270, 710)

## camp
camp_wall_hitboxes = []

wall_1 = pygame.Rect(200, 260, 30, 200)
camp_wall_hitboxes.append(wall_1)

wall_2 = pygame.Rect(200, 260, 200, 30)
camp_wall_hitboxes.append(wall_2)

wall_3 = pygame.Rect(200, 460, 200, 30)
camp_wall_hitboxes.append(wall_3)


camp_interactable_hitboxes = {}

PORTAL_DISPLACEMENT_Y = 64
camp_interactable_hitboxes["slime_plains_portal"] = map_objects.Portal_rect(1270, PORTAL_DISPLACEMENT_Y)
camp_interactable_hitboxes["golem_ruins_portal"] = map_objects.Portal_rect(1270, 2*PORTAL_DISPLACEMENT_Y + camp_interactable_hitboxes["slime_plains_portal"].height)
camp_interactable_hitboxes["wyvern_mountains_portal"] = map_objects.Portal_rect(1270, 3*PORTAL_DISPLACEMENT_Y + camp_interactable_hitboxes["slime_plains_portal"].height + camp_interactable_hitboxes["golem_ruins_portal"].height)
camp_interactable_hitboxes["dragon_lair_portal"] = map_objects.Portal_rect(1270, 4* PORTAL_DISPLACEMENT_Y + camp_interactable_hitboxes["slime_plains_portal"].height + camp_interactable_hitboxes["golem_ruins_portal"].height + camp_interactable_hitboxes["wyvern_mountains_portal"].height)
camp_interactable_hitboxes["skill_merchant"] = pygame.Rect(265, 325, 100, 100)
## slime plains

slime_wall_hitboxes = []

slime_interactable_hitboxes = {}
slime_interactable_hitboxes["camp_portal"] = map_objects.Portal_rect(0, (screen.get_height() - map_objects.Portal_rect.common_height)/2)
slime_interactable_hitboxes["slime_enemy"] = map_objects.Entity_rect((screen.get_width() - map_objects.Entity_rect.common_width)/2, (screen.get_height() - map_objects.Entity_rect.common_height)/2)
## golem ruins

golem_wall_hitboxes = []

golem_interactable_hitboxes = {}
golem_interactable_hitboxes["camp_portal"] = map_objects.Portal_rect(0, (screen.get_height() - map_objects.Portal_rect.common_height)/2)
golem_interactable_hitboxes["golem_enemy"] = map_objects.Entity_rect((screen.get_width() - map_objects.Entity_rect.common_width)/2, (screen.get_height() - map_objects.Entity_rect.common_height)/2)

## wyvern montains

wyvern_wall_hitboxes = []

wyvern_interactable_hitboxes = {}
wyvern_interactable_hitboxes["camp_portal"] = map_objects.Portal_rect(0, (screen.get_height() - map_objects.Portal_rect.common_height)/2)
wyvern_interactable_hitboxes["wyvern_enemy"] = map_objects.Entity_rect((screen.get_width() - map_objects.Entity_rect.common_width)/2, (screen.get_height() - map_objects.Entity_rect.common_height)/2)

## dragon's lair

dragon_wall_hitboxes = []

dragon_interactable_hitboxes = {}
dragon_interactable_hitboxes["camp_portal"] = map_objects.Portal_rect(0, (screen.get_height() - map_objects.Portal_rect.common_height)/2)
dragon_interactable_hitboxes["dragon_enemy"] = map_objects.Entity_rect((screen.get_width() - map_objects.Entity_rect.common_width)/2, (screen.get_height() - map_objects.Entity_rect.common_height)/2)


# player
BASE_PLAYER_SPEED = 300

player_hitbox = pygame.Rect(screen.get_width()/2, screen.get_height()/2, player_image.get_width(), player_image.get_height())


# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# custom functions




## screen handling
def quit_game():
    global running
    running = False

def update_screen():
    global delta_time, clock
    pygame.display.flip()
    delta_time = clock.tick(144) / 1000

def switch_screens():
    global game_screen, current_screen, previous_screen
    temp_screen = current_screen
    current_screen = previous_screen
    previous_screen = temp_screen
    print(game_screen, current_screen, previous_screen)

def back_to_game():
    global game_screen, current_screen, previous_screen
    previous_screen = current_screen
    current_screen = "ingame"
    print(game_screen, current_screen, previous_screen)

def render_walls(rects: list):
    for rect in rects:
        pygame.draw.rect(screen, "black", rect)
    
def render_interactables(rects: dict):
    for key, rect in rects.items():
        pygame.draw.rect(screen, "red", [rect.x, rect.y, rect.width, rect.height])
 
def render_inventory_cells(rects: dict, previously_clicked_cell):
    for rect in rects.values():
        bg_color = "white"
        if rect == previously_clicked_cell:
            bg_color = "red"
        pygame.draw.rect(screen, bg_color, [rect.x, rect.y, rect.width, rect.height])
        if rect.item != None:
            screen.blit(inventory_cell_font.render(rect.item.name, True, "black", None, 100), [rect.x, rect.y, rect.width, rect.height])
        elif rect.name == "head" or rect.name == "weapon" or rect.name == "chest" or rect.name == "legs":
            screen.blit(inventory_cell_font.render(rect.name, True, "black", None, 100), [rect.x, rect.y, rect.width, rect.height])

def render_skill_buttons(buttons):
    for rect in buttons.values():
        pygame.draw.rect(screen, "white", [rect.x, rect.y, rect.width, rect.height])
        if rect.projected_value == 1: operand = "+" 
        else: operand = "-"
        screen.blit(fight_font.render(operand, True, "white", "black", 300), [rect.x, rect.y, rect.width, rect.height])

def render_buttons(rects: dict):
    for key, rect in rects.items():
        pygame.draw.rect(screen, "white", [rect.x, rect.y, rect.width, rect.height])
        screen.blit(common_button_font.render(key, True, "black", None, 300), [rect.x, rect.y, rect.width, rect.height])

def render_text(text, x, y, width, height):
    screen.blit(fight_font.render(text, True, "white", None, width), [x, y, width, height])

def render_stats(entity, x, y):
    text = f"{entity.name} lvl:{entity.lvl}; HP: {entity.current_hp}/{entity.max_hp}"

    screen.blit(fight_font.render(text, True, "white", None, 500), [x, y, 615, 100])


## common button interact

def pressed_button(buttons):
    for key, button in buttons.items():
            if (button.left < pygame.mouse.get_pos()[0] < (button.left + button.width)) and (button.top < pygame.mouse.get_pos()[1] < (button.top + button.height)):
                clicked = key
                return clicked


## colision handling system

def colision_detection(player_hitbox, old_x, old_y, temp_x, temp_y, wall):
    colision_x = False
    colision_y = False
    if  temp_x <= wall.x + wall.width and temp_x + player_hitbox.width >= wall.x and old_y <= wall.y + wall.height and old_y + player_hitbox.height >= wall.y:
        colision_x = True
    if  old_x <= wall.x + wall.width and old_x + player_hitbox.width >= wall.x and temp_y <= wall.y + wall.height and temp_y + player_hitbox.height >= wall.y:
        colision_y = True
    return [colision_x, colision_y]

def list_colision_detection(player_hitbox, old_x, old_y, temp_x, temp_y, stationary_hitboxes):
    colisions = [False, False]
    for object in stationary_hitboxes:
        colision = colision_detection(player_hitbox, old_x, old_y, temp_x, temp_y, object)
        if colision[0] == True: colisions[0] = True
        if colision[1] == True: colisions[1] = True

    return colisions

def dict_colision_detection(player_hitbox, old_x, old_y, temp_x, temp_y, interactable_hitboxes):
    colisions = [False, False]
    colided_with = None
    for name, object in interactable_hitboxes.items():
        colision = colision_detection(player_hitbox, old_x, old_y, temp_x, temp_y, object)
        if colision[0] == True: colisions[0] = True
        if colision[1] == True: colisions[1] = True
        if (colisions[0] or colisions[1]) and colided_with == None:
            colided_with = name
    
    return [colisions[0], colisions[1], colided_with]

def colision_management(player_hitbox: pygame.Rect, old_x: int, old_y: int, temp_x: int, temp_y: int, stationary_hitboxes: list, interactable_hitboxes: dict):
    disable_x, disable_y = False, False

    list_colisions = list_colision_detection(player_hitbox, old_x, old_y, temp_x, temp_y, stationary_hitboxes)
    dict_colisions = dict_colision_detection(player_hitbox, old_x, old_y, temp_x, temp_y, interactable_hitboxes)

    if list_colisions[0] == True or dict_colisions[0]: disable_x = True
    if list_colisions[1] == True or dict_colisions[1]: disable_y = True


    if disable_x and disable_y:
        print("2way colision")
        final_x, final_y = old_x, old_y
    elif disable_x and not disable_y:
        final_x, final_y = old_x, temp_y
        print("x would cause colision")
    elif not disable_x and disable_y:
        final_x, final_y = temp_x, old_y
        print("y would cause colision")
    else:
        final_x, final_y = temp_x, temp_y

    return (final_x, final_y, dict_colisions[2])



def speed_normalization(movement_keys, player_speed, delta_time):
    number_of_pressed_keys = 0
    speed_normalizer = 1

    for key in movement_keys:
        if key == True: number_of_pressed_keys += 1
        if number_of_pressed_keys > 1:
            speed_normalizer = 1.41421
            break

    distance_coefitient = player_speed * delta_time / speed_normalizer
    return distance_coefitient

def interact(interacted_with, player_hitbox):
    global game_screen, current_screen, previous_screen, enemy, player
    if interacted_with == "slime_plains_portal":
        game_screen = "slime"
        player_hitbox.x, player_hitbox.y = 50, 330
    
    if interacted_with == "golem_ruins_portal":
        game_screen = "golem"
        player_hitbox.x, player_hitbox.y = 50, 330
    
    if interacted_with == "wyvern_mountains_portal":
        game_screen = "wyvern"
        player_hitbox.x, player_hitbox.y = 50, 330
    
    if interacted_with == "dragon_lair_portal":
        game_screen = "dragon"
        player_hitbox.x, player_hitbox.y = 50, 330
    
    if interacted_with == "skill_merchant":
        previous_screen = current_screen
        current_screen = "skills"
        player.update_stats(inventory.equipement_cells)

    if interacted_with == "camp_portal":
        game_screen = "camp"
        player_hitbox.x, player_hitbox.y = screen.get_width() - 100, 330
        player.update_stats(inventory.equipement_cells)
        player.max_heal()
    
    if interacted_with == "slime_enemy":
        previous_screen = current_screen
        current_screen = "combat"
        enemy = entities.Slime()
        enemy.update_stats()    
    
    if interacted_with == "golem_enemy":
        previous_screen = current_screen
        current_screen = "combat"
        enemy = entities.Golem()
        enemy.update_stats()
    
    if interacted_with == "wyvern_enemy":
        previous_screen = current_screen
        current_screen = "combat"
        enemy = entities.Wyvern()
        enemy.update_stats()
        
    if interacted_with == "dragon_enemy":
        previous_screen = current_screen
        current_screen = "combat"
        enemy = entities.Dragon()
        enemy.update_stats()


## main interaction/movement processor

def move(player, screen, stationary_hitboxes, interactable_hitboxes, player_speed, delta_time):
    movement_keys = [keys_pressed[pygame.K_w], keys_pressed[pygame.K_s], keys_pressed[pygame.K_a], keys_pressed[pygame.K_d]]
    old_x = player.x
    old_y = player.y
    tempx = player.x
    tempy = player.y

    distance_coefitient = speed_normalization(movement_keys, player_speed, delta_time)

    if movement_keys[0]:
        tempy = pygame.math.clamp(tempy - distance_coefitient, 0, screen.get_height() - player.height)

    if movement_keys[1]:
        tempy = pygame.math.clamp(tempy + distance_coefitient, 0, screen.get_height() - player.height)

    if movement_keys[2]:
        tempx = pygame.math.clamp(tempx - distance_coefitient, 0, screen.get_width() - player.width)

    if movement_keys[3]:
        tempx = pygame.math.clamp(tempx + distance_coefitient, 0, screen.get_width() - player.width)


    new_coords_and_colision = colision_management(player, old_x, old_y, round(tempx), round(tempy), stationary_hitboxes, interactable_hitboxes)
    player_hitbox.x, player_hitbox.y = new_coords_and_colision[0], new_coords_and_colision[1]
    
    interact(new_coords_and_colision[2], player)

## combat functions


def attack(entity_1, entity_2):
    end = False
    entity_2.current_hp = entity_2.current_hp - entity_1.damage_per_hit
    if entity_2.current_hp <= 0:
        end = True
    return (entity_2, end)


def heal(entity):
    entity.current_hp = entity.current_hp + entity.healing_amount
    return entity

def enemy_action(enemy: entities.Enemy, player: entities.Player):
    end = False
    if enemy.max_hp - enemy.current_hp > enemy.healing_amount and enemy.current_hp/enemy.max_hp <= 1/3:
        enemy = heal(enemy)
    else:
        attack_result = attack(enemy, player)
        player = attack_result[0]
        end = attack_result[1]
    
    return(enemy, player, end)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# setup shits... idk



# variables for game navigation
current_screen = "ingame"
previous_screen  = "ingame"
game_screen = "camp"

# variables for inv handling
clicked_cell = None
previously_clicked_cell = None




## code for testing

player.free_skill_points = 2

# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# the game





while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    keys_pressed = pygame.key.get_pressed()
    keys_down = pygame.key.get_just_pressed()

    if keys_down[pygame.K_ESCAPE] == True:
        if current_screen == "menu":
            current_screen = previous_screen
            previous_screen = "menu"
        else:
            previous_screen = current_screen
            current_screen = "menu"
        print(game_screen, current_screen, previous_screen)
            
    
    if keys_down[pygame.K_e] == True and current_screen != "menu" and current_screen != "skills":
        if current_screen == "inventory" and inventory_type == "backpack":
            back_to_game()
        elif current_screen == "ingame":
            previous_screen = current_screen
            current_screen = "inventory"
            inventory_type = "backpack"
        print(game_screen, current_screen, previous_screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()



    if current_screen == "menu":
        screen.fill("black")
        render_buttons(menu_buttons)

        pressed_menu_button = None
        if pygame.mouse.get_pressed()[0]:
            pressed_menu_button = pressed_button(menu_buttons)  
            if pressed_menu_button == "back to last screen":
                switch_screens()
        
    
    if current_screen == "inventory":
        screen.fill("black")
        render_inventory_cells(inventory.inventory_cells, previously_clicked_cell)
        pressed_inventory_button = None

        if inventory_type == "backpack":
            render_inventory_cells(inventory.equipement_cells, previously_clicked_cell)
            all_buttons_on_screen, active_inventory = backpack_cells, backpack_cells

        
        elif inventory_type == "chest":
            render_inventory_cells(inventory.chest_cells, previously_clicked_cell)
            render_buttons(other_chest_buttons)
            all_buttons_on_screen, active_inventory = all_chest_butons, chest_cells
        
        
        if pygame.mouse.get_just_pressed()[0]:
            pressed_inventory_button = pressed_button(all_buttons_on_screen)
            if pressed_inventory_button not in active_inventory.keys():
                previously_clicked_cell = None
                if pressed_inventory_button == "back_to_game":
                    inventory.clear_chest(inventory.chest_cells)
                    back_to_game()

            else:
                clicked_cell = active_inventory[pressed_inventory_button]
                transfare_output = inventory.item_transfare_handler(previously_clicked_cell, clicked_cell, active_inventory)
                previously_clicked_cell, clicked_cell = transfare_output[0], transfare_output[1]
                if transfare_output[2] != None or transfare_output[3] != None:
                    active_inventory[transfare_output[2].name], active_inventory[transfare_output[3].name] = transfare_output[2], transfare_output[3]
                    player.update_stats(inventory.equipement_cells)



    if current_screen == "ingame":
        if game_screen == "camp":
            screen.blit(camp_background, (0, 0))
                
            render_walls(camp_wall_hitboxes)
            render_interactables(camp_interactable_hitboxes)

            move(player_hitbox, screen, camp_wall_hitboxes, camp_interactable_hitboxes, BASE_PLAYER_SPEED, delta_time)
            screen.blit(player_image, player_hitbox)
        
        if game_screen == "slime":
            screen.blit(slime_plains_background, (0, 0))
            
            render_walls(slime_wall_hitboxes)
            render_interactables(slime_interactable_hitboxes)

            move(player_hitbox, screen, slime_wall_hitboxes, slime_interactable_hitboxes, BASE_PLAYER_SPEED, delta_time)
            screen.blit(player_image, player_hitbox)

        if game_screen == "golem":
            screen.blit(golem_ruins_background, (0, 0))
                
            render_interactables(golem_interactable_hitboxes)

            move(player_hitbox, screen, golem_wall_hitboxes, golem_interactable_hitboxes, BASE_PLAYER_SPEED, delta_time)
            screen.blit(player_image, player_hitbox)

        if game_screen == "wyvern":
            screen.blit(wyvern_mountains_background, (0, 0))
            
            render_interactables(wyvern_interactable_hitboxes)

            move(player_hitbox, screen, wyvern_wall_hitboxes, wyvern_interactable_hitboxes, BASE_PLAYER_SPEED, delta_time)
            screen.blit(player_image, player_hitbox)
        
        if game_screen == "dragon":
            screen.blit(dragon_lair_background, (0, 0))
                
            render_interactables(dragon_interactable_hitboxes)

            move(player_hitbox, screen, dragon_wall_hitboxes, dragon_interactable_hitboxes, BASE_PLAYER_SPEED, delta_time)
            screen.blit(player_image, player_hitbox)


    if current_screen == "combat":
        screen.fill("black")
        
        render_buttons(combat_buttons)

        render_stats(player, 25, 25)
        render_stats(enemy, 640 + 25, 450)


        if pygame.mouse.get_just_pressed()[0]:
            pressed_combat_button = pressed_button(combat_buttons)
            match(pressed_combat_button):
                case("Attack"):
                    # current_screen = "writing"
                    attack_result = attack(player, enemy)
                    enemy = attack_result[0]
                    if attack_result[1] == False:
                        enemy_action_result = enemy_action(enemy, player)
                        enemy = enemy_action_result[0]
                        player = enemy_action_result[1]

                        if enemy_action_result[2] == True:
                            current_screen = "ingame"
                            game_screen = "camp"
                            player.update_stats(inventory.equipement_cells)
                            player.max_heal()
                            enemy = None
                    else:
                        current_screen = "inventory"
                        inventory_type = "chest"
                        inventory.assign_drops(inventory.chest_cells, items.generate_drops(enemy))
                        player.gain_xp(enemy.xp)
                        enemy = None
                   
                case("Heal"):
                    # current_screen = "writing"
                    player = heal(player)
                    enemy_action_result = enemy_action(enemy, player)
                    enemy = enemy_action_result[0]
                    player = enemy_action_result[1]

                    if enemy_action_result[2] == True:
                        current_screen = "ingame"
                        game_screen = "camp"
                        player.update_stats(inventory.equipement_cells)
                        player.max_heal()
                        enemy = None

                case("Flee"):
                    # current_screen = "writing"
                    switch_screens()
                    enemy = None


    if current_screen == "skills":
        screen.fill("black")
        render_text(f"Name:             {player.name}", 25, 25, 600, 40)
        render_text(f"lvl:              {player.lvl}", 25, 25 + 40*1, 600, 40)
        render_text(f"XP:               {player.xp}/{player.xp_treshold}", 25, 25 + 40*2, 600, 40)
        render_text(f"Max HP:           {player.max_hp}", 25, 25 + 40*3, 600, 40)
        render_text(f"Damage:           {player.damage_per_hit}", 25, 25 + 40*4, 600, 40)
        render_text(f"Healing:          {player.healing_amount}", 25, 25 + 40*5, 600, 40)

        render_text("------------------------------", 25, 25 + 40*7, 600, 40)

        render_text(f"Free skill point: {player.free_skill_points}", 25, 25 + 40*9, 600, 40)
        render_text(f"Halth LVL:        {player.health_lvl}", 25, 25 + 40*10, 400, 40)
        render_text(f"Damage LVL:       {player.damage_lvl}", 25, 25 + 40*11, 400, 40)
        render_text(f"Healing LVL:      {player.healing_lvl}", 25, 25 + 40*12, 400, 40)

        # 6 butttonů na modifikaci skillů
        
        render_skill_buttons(skill_buttons)
        render_buttons(other_skill_buttons)

        if pygame.mouse.get_just_pressed()[0]:
            pressed_skill_button = pressed_button(all_skill_buttons)
            if pressed_skill_button == "back_to_game":
                switch_screens()

            elif pressed_skill_button in skill_buttons:
                if pressed_skill_button.startswith("health_lvl") and (player.health_lvl + skill_buttons[pressed_skill_button].projected_value) != 0 and (player.free_skill_points - skill_buttons[pressed_skill_button].projected_value) != -1:
                    player.health_lvl += skill_buttons[pressed_skill_button].projected_value
                    player.free_skill_points -= skill_buttons[pressed_skill_button].projected_value
                    player.update_stats(inventory.equipement_cells)
                elif pressed_skill_button.startswith("damage_lvl") and (player.damage_lvl + skill_buttons[pressed_skill_button].projected_value) != 0 and (player.free_skill_points - skill_buttons[pressed_skill_button].projected_value) != -1:
                    player.damage_lvl += skill_buttons[pressed_skill_button].projected_value
                    player.free_skill_points -= skill_buttons[pressed_skill_button].projected_value
                    player.update_stats(inventory.equipement_cells)
                elif pressed_skill_button.startswith("healing_lvl") and player.healing_lvl + skill_buttons[pressed_skill_button].projected_value != -1 and (player.free_skill_points - skill_buttons[pressed_skill_button].projected_value) != -1:
                    player.healing_lvl += skill_buttons[pressed_skill_button].projected_value
                    player.free_skill_points -= skill_buttons[pressed_skill_button].projected_value
                    player.update_stats(inventory.equipement_cells)
    
    
    
    
    # if current_screen == "writing":
    #     ...




    update_screen()

pygame.quit()

# To Do List:
# chest screen
# skill screen (skylly a exp na konci boje)
# welcome screen