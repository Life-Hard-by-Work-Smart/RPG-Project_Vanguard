import pygame

class Common_menu_button(pygame.Rect):
    common_width = 300
    common_height = 75
    def __init__(self, x, y):
        self.width = Common_menu_button.common_width # x offset bude cca 76
        self.height = Common_menu_button.common_height # y offset nebude, budou vedle sebe
        self.x = x
        self.y = y

class Common_back_button(pygame.Rect):
    common_width = 200
    common_height = 100
    def __init__(self, x, y): 
        self.width = Common_back_button.common_width
        self.height = Common_back_button.common_height
        self.x = x
        self.y = y

class Skill_modify_button(pygame.Rect):
    common_dimension = 40
    def __init__(self, x, y, add_or_subtract):
        self.x = x
        self.y = y
        self.width = Skill_modify_button.common_dimension
        self.height = Skill_modify_button.common_dimension
        self.projected_value = add_or_subtract
