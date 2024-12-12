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