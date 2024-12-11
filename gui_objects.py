import pygame

class Common_menu_button(pygame.Rect):
    def __init__(self, x, y):
        self.width = 300 # x offset bude cca 76
        self.height = 75 # y offset nebude, budou vedle sebe
        self.x = x
        self.y = y

class Common_back_button(pygame.Rect):
    def __init__(self, x, y):
        self.width = 200
        self.height = 100
        self.x = x
        self.y = y

class Menu_button(pygame.Rect):
    ...