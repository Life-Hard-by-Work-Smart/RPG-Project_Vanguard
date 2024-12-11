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

inventory_cell_font = pygame.font.SysFont("Consolas", 15)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0


# asset loading
dirname = os.path.dirname(__file__)

camp_background_dir = os.path.join(dirname, fr"Assets\pics\Mapa_RPG-P.V._v1.0.0.png")
camp_background = pygame.Surface.convert(pygame.image.load(camp_background_dir))

slime_plains_background_dir = os.path.join(dirname, fr"Assets\pics\slimeplains.png")
slime_plains_background = pygame.Surface.convert(pygame.image.load(slime_plains_background_dir))

player_image_dir = os.path.join(dirname, fr"Assets\pics\tucnak_warm.png")
player_image = pygame.Surface.convert(pygame.image.load(player_image_dir))




# vars and constants for button screens

class Common_menu_button(pygame.Rect):
    ...

class Common_back_button(pygame.Rect):
    ...

class Common_lower_bar_button(pygame.Rect):
    ...

### vymysli jak zařídit text

## vars and constants for menu

menu_buttons = {}

class Menu_button(pygame.Rect):
    ...

menu_buttons["back to game"] = Menu_button(540, 310, 100, 50)

## vars and constants for inventory

cells = {}
cells.update(inventory.inventory_cells)
cells.update(inventory.equipement_cells)

inventory_buttons = {}
inventory_buttons.update(cells)


## vars and constants for combat

class Button_for_combat(pygame.Rect):
    ...

## vars and constants for loot screen

chest_cells = []

##vars and constants for skill screen

class Skill_modify_button(pygame.Rect):
    ...


# vars and constants for movement screen
## maps
map_border = pygame.Rect(5, 5, 1270, 710)

## camp
camp_wall_hitboxes = []

wall_1 = pygame.Rect(200, 260, 30, 200)
camp_wall_hitboxes.append(wall_1)

wall_2 = pygame.Rect(200, 260, 200, 30)
camp_wall_hitboxes.append(wall_2)


camp_interactable_hitboxes = {}

PORTAL_DISPLACEMENT_Y = 64
camp_interactable_hitboxes["slime_plains_portal"] = map_objects.portal_rect(1270, PORTAL_DISPLACEMENT_Y)
camp_interactable_hitboxes["golem_ruins_portal"] = map_objects.portal_rect(1270, 2*PORTAL_DISPLACEMENT_Y + camp_interactable_hitboxes["slime_plains_portal"].height)
camp_interactable_hitboxes["wivern_mountains_portal"] = map_objects.portal_rect(1270, 3*PORTAL_DISPLACEMENT_Y + camp_interactable_hitboxes["slime_plains_portal"].height + camp_interactable_hitboxes["golem_ruins_portal"].height)
camp_interactable_hitboxes["dragons_lair_portal"] = map_objects.portal_rect(1270, 4* PORTAL_DISPLACEMENT_Y + camp_interactable_hitboxes["slime_plains_portal"].height + camp_interactable_hitboxes["golem_ruins_portal"].height + camp_interactable_hitboxes["wivern_mountains_portal"].height)



## slime plains

slime_wall_hitboxes = []

slime_interacrtable_hitboxes = {}

## golem ruins

golem_wall_hitboxes = []

golem_interacrtable_hitboxes = {}

## wyvern montains

wyvern_wall_hitboxes = []

wyvern_interacrtable_hitboxes = {}

## dragon's lair

dragon_wall_hitboxes = []

dragon_interacrtable_hitboxes = {}


# player
BASE_PLAYER_SPEED = 300

player_hitbox = pygame.Rect(screen.get_width()/2, screen.get_height()/2, player_image.get_width(), player_image.get_height())
print(player_image.get_height())
player_hitbox_perdiction = player_hitbox.copy()


# custom functions

## screen handling
def quit_game():
    global running
    running = False

def update_screen():
    global delta_time, clock
    pygame.display.flip()
    delta_time = clock.tick(144) / 1000

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


## common button interact

def pressed_button(buttons):
    for name, button in buttons.items():
            if (button.left < pygame.mouse.get_pos()[0] < (button.left + button.width)) and (button.top < pygame.mouse.get_pos()[1] < (button.top + button.height)):
                clicked = name
                print(clicked)
                return clicked

## colision handling system

def interact(with_what, player_hitbox):
    global current_screen
    if with_what == "slime_plains_portal":
        current_screen = "slime"
        player_hitbox.x, player_hitbox.y = 50, 330

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

def colision_management(player_hitbox: pygame.Rect, old_x: int, old_y: int, temp_x: int, temp_y: int, stationary_hitboxes: list, interactable_hitboxes: dict,):
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

# variables for game navigation
current_screen = "inventory"
previous_screen  = None


# variables for inv handling
clicked_cell = None
previously_clicked_cell = None




## code for testing
cells["0"].item = items.dragon_drops[0]
cells["1"].item = items.dragon_drops[1]
cells["2"].item = items.dragon_drops[2]
cells["3"].item = items.dragon_drops[3]

# the game

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    keys_pressed = pygame.key.get_pressed()
    keys_down = pygame.key.get_just_pressed()

    if keys_down[pygame.K_ESCAPE] == True:
        if current_screen == "menu":
            current_screen = previous_screen
        else:
            previous_screen = current_screen
            current_screen = "menu"
            print(previous_screen)

        print(current_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()


    if current_screen == "menu":
        screen.fill("black")
        for button in menu_buttons.values():
            pygame.draw.rect(screen, "white", button)

        pressed_menu_button = None
        if pygame.mouse.get_pressed()[0]:
            pressed_menu_button = pressed_button(menu_buttons)  
        if pressed_menu_button == "back to game":
            previous_screen = current_screen
            current_screen = "camp" ## tohle musíš změnit
    
        

    if current_screen == "camp":
        screen.blit(camp_background, (0, 0))
        for i_stationary_hitbox in range(len(camp_wall_hitboxes)):
            pygame.draw.rect(screen, "black", camp_wall_hitboxes[i_stationary_hitbox])

        for interactable_hitbox in camp_interactable_hitboxes.values():
            pygame.draw.rect(screen, "red", interactable_hitbox)

        move(player_hitbox, screen, camp_wall_hitboxes, camp_interactable_hitboxes, BASE_PLAYER_SPEED, delta_time)
        print(current_screen)
        screen.blit(player_image, player_hitbox)






    if current_screen == "slime":
        screen.blit(slime_plains_background, (0, 0))

        move(player_hitbox, screen, slime_wall_hitboxes, slime_interacrtable_hitboxes, BASE_PLAYER_SPEED, delta_time)
        screen.blit(player_image, player_hitbox)

    if current_screen == "golem":
        #screen.blit(golem_plains_background, (0, 0))

        move(player_hitbox, screen, golem_wall_hitboxes, golem_interacrtable_hitboxes, BASE_PLAYER_SPEED, delta_time)
        screen.blit(player_image, player_hitbox)

    if current_screen == "wyvern":
        #screen.blit(wyvern_plains_background, (0, 0))

        move(player_hitbox, screen, wyvern_wall_hitboxes, wyvern_interacrtable_hitboxes, BASE_PLAYER_SPEED, delta_time)
        screen.blit(player_image, player_hitbox)
    
    if current_screen == "dragon":
        #screen.blit(dragon_plains_background, (0, 0))

        move(player_hitbox, screen, dragon_wall_hitboxes, dragon_interacrtable_hitboxes, BASE_PLAYER_SPEED, delta_time)
        screen.blit(player_image, player_hitbox)





    if current_screen == "inventory":
        screen.fill("black")
        render_inventory_cells(inventory_buttons, previously_clicked_cell)
        pressed_inventory_button = None
        if pygame.mouse.get_just_pressed()[0]:
            pressed_inventory_button = pressed_button(inventory_buttons)
            if pressed_inventory_button not in cells.keys():
                previously_clicked_cell = None

        if pressed_inventory_button in cells.keys():
            clicked_cell = cells[pressed_inventory_button]
            transfare_output = inventory.item_transfare_handler(previously_clicked_cell, clicked_cell, cells)
            previously_clicked_cell, clicked_cell = transfare_output[0], transfare_output[1]
            if transfare_output[2] != None or transfare_output[3] != None:
                cells[transfare_output[2].name], cells[transfare_output[3].name] = transfare_output[2], transfare_output[3]

    update_screen()

pygame.quit()



# To Do List:
# zbytek lokací
# inventory screen
# combat screen
# loot screen
# skill screen