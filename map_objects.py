import pygame

# normálně bych nedělal class atributes, ale používám tenhle value na umístění objektů na screen... => nemám tolik magických čísel ^

class Portal_rect(pygame.Rect):
    common_width = 10
    common_height = 100

    def __init__(self, left, top):
        self.x = left
        self.y = top
        self.width = Portal_rect.common_width
        self.height = Portal_rect.common_height

class Entity_rect(pygame.Rect):
    common_width = 100
    common_height = 100

    def __init__(self, left, top):
        self.x = left
        self.y = top
        self.width = Entity_rect.common_width
        self.height = Entity_rect.common_height