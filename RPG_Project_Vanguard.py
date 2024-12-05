import pygame
import os


# pygame setup
pygame.init()


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
delta_time = 0
current_screen = "camp"
previous_screen  = None


# asset loading
dirname = os.path.dirname(__file__)

camp_background_dir = os.path.join(dirname, fr'Assets\pics\Mapa_RPG-P.V._v1.0.0.png')
camp_background = pygame.Surface.convert(pygame.image.load(camp_background_dir))

player_image_dir = os.path.join(dirname, fr'Assets\pics\tucnak_warm.png')
player_image = pygame.Surface.convert(pygame.image.load(player_image_dir))




## vars and constants for menu

buttons = {}

buttons["back to game"] = pygame.Rect(540, 310, 100, 50)





### vars and constants for movement screen
## maps
map_border = pygame.Rect(5, 5, 1270, 710)

# camp
camp_wall_hitboxes = []

wall_1 = pygame.Rect(200, 260, 30, 200)
camp_wall_hitboxes.append(wall_1)

wall_2 = pygame.Rect(200, 260, 200, 30)
camp_wall_hitboxes.append(wall_2)


camp_interactable_hitboxes = []

class portal_rect(pygame.Rect):
    
    def __init__(self):
        self.width = 10
        self.height = 100

portal_distance_y = 64
slime_plains_portal = pygame.Rect(1270, portal_distance_y, 10, 100)
golem_ruins_portal = pygame.Rect(1270, 2*portal_distance_y + 100, 10, 100)
wivern_mountains_portal =pygame.Rect(1270, 3*portal_distance_y + 2*100, 10, 100)
dragons_lair_portal =pygame.Rect(1270, 4* portal_distance_y + 3*100, 10, 100)



# slime plains


# golem ruins


# wivern montains


# dragon's lair




## player
BASE_PLAYER_SPEED = 200

player_hitbox = pygame.Rect(screen.get_width()/2, screen.get_height()/2, player_image.get_width(), player_image.get_height())
player_hitbox_perdiction = player_hitbox.copy()


# custom functions
def quit_game():
    global running
    running = False

def update_screen():
    global delta_time, clock
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000


def speed_normalization(movement_keys, player_speed, delta_time):
    number_of_pressed_keys = 0
    speed_normalizer = 1

    for key in movement_keys:
        if key == True : number_of_pressed_keys += 1

        if number_of_pressed_keys > 1:
            speed_normalizer = 1.4;
            break

    distance_coefitient = player_speed * delta_time / speed_normalizer
    return distance_coefitient


def colision_detection(player_hitbox: pygame.Rect, stationary_hitboxes: list, old_x: int, old_y: int):
    disable_x, disable_y = False, False
    for wall in stationary_hitboxes:

        if  player_hitbox.x <= wall.x + wall.width and player_hitbox.x + player_hitbox.width >= wall.x and old_y <= wall.y + wall.height and old_y + player_hitbox.height >= wall.y:
            print("x would cause colision")
            disable_x = True
        if  old_x <= wall.x + wall.width and old_x + player_hitbox.width >= wall.x and player_hitbox.y <= wall.y + wall.height and player_hitbox.y + player_hitbox.height >= wall.y:
            print("y would cause colision")
            disable_y = True

    if disable_x and disable_y:
        print("2way colision")
        final_x, final_y = old_x, old_y
    elif disable_x and not disable_y:
        final_x, final_y = old_x, player_hitbox.y
    elif not disable_x and disable_y:
        final_x, final_y = player_hitbox.x, old_y
    else:
        final_x, final_y = player_hitbox.x, player_hitbox.y
    return (final_x, final_y)

def move(movement_keys, player, screen, stationary_hitboxes, player_speed, delta_time):
    tempy = player.y
    tempx = player.x

    distance_coefitient = speed_normalization(movement_keys, player_speed, delta_time)

    if movement_keys[0]:
        player.y = pygame.math.clamp(player.y - round(distance_coefitient), 0, screen.get_height() - player.height)

    if movement_keys[1]:
        player.y = pygame.math.clamp(player.y + round(distance_coefitient), 0, screen.get_height() - player.height)

    if movement_keys[2]:
        player.x = pygame.math.clamp(player.x - round(distance_coefitient), 0, screen.get_width() - player.width)

    if movement_keys[3]:
        player.x = pygame.math.clamp(player.x + round(distance_coefitient), 0, screen.get_width() - player.width)

    coords_after_colisions = colision_detection(player, stationary_hitboxes, tempx, tempy)
    player.x = coords_after_colisions[0]
    player.y = coords_after_colisions[1]



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

        print(current_screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()


    if current_screen == "menu":
        movement = False
        screen.fill("black")
        for button in buttons.values():
            pygame.draw.rect(screen, "white", button)
        for name, button in buttons.items():
            if pygame.mouse.get_pressed()[0] and (button.left < pygame.mouse.get_pos()[0] < (button.left + button.width)) and (button.top < pygame.mouse.get_pos()[1] < (button.top + button.height)):
                if name == "back to game":
                    previous_screen = current_screen
                    current_screen = "camp"
        
        

    if current_screen == "camp":
        movement = True
        screen.blit(camp_background, (0, 0))
        for i_stationary_hitbox in range(len(camp_wall_hitboxes)):
            pygame.draw.rect(screen, "black", camp_wall_hitboxes[i_stationary_hitbox])

        for i_interactable_hitbox in range(len(camp_interactable_hitboxes)):
            pygame.draw.rect(screen, "red", camp_interactable_hitboxes[i_interactable_hitbox])
    

    if current_screen == "slime plains":
        movement = True
        #screen.blit(camp_background, (0, 0))
        #pygame.draw.rect(screen, "black", camp_wall_hitboxes[1])


    if movement:
        movement_keys = [keys_pressed[pygame.K_w], keys_pressed[pygame.K_s], keys_pressed[pygame.K_a], keys_pressed[pygame.K_d]]

        move(movement_keys, player_hitbox, screen, camp_wall_hitboxes, BASE_PLAYER_SPEED, delta_time)

        screen.blit(player_image, player_hitbox)
    


    
    update_screen()

pygame.quit()