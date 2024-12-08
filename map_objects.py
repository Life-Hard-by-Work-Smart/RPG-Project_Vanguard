import pygame

class portal_rect(pygame.Rect):
    
    def __init__(self, left, top):
        self.left = left
        self.top = top
        self.width = 10
        self.height = 100
