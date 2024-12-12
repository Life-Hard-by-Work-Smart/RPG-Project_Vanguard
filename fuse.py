import pygame
import random

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spojování předmětů")

class Item:
    def __init__(self, name, dmg, hp, type_):
        self.name = name
        self.dmg = dmg
        self.hp = hp
        self.type = type_
        self.image = pygame.Surface((50, 50))
        self.image.fill((random.randint(100, 255), 0, 0))
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

items = [
    Item("Bouncy Helmet", 0, 3, "head"),
    Item("Half-Liquid Sword", 1, 0, "weapon")
    Item("Bouncy Chestplate", 0, 6, "chest"),
    Item("Gooey Chestplate", 0, 10, "chest"),
    Item("Bouncy Leggings", 0, 3, "legs"),
    Item("Gooey Leggings", 0, 5, "legs"),
    Item("Half-Liquid Sword", 1, 0, "weapon"),
    Item("Slime Slinging Slasher", 4, 0, "weapon"),
    Item("Rock with eyelids", -2, 8, "head"),
    Item("Living Helmet", 0, 8, "head"),
    Item("Rocklike Chestplate", -4, 16, "chest"),
    Item("Living Chestplate", 0, 16, "chest"),
    Item("Rocks glued to legs", -2, 8, "legs"),
    Item("Living Leggings", 0, 8, "legs"),
    Item("Golem's Arm", 5, 2, "weapon"),
    Item("Floating Boulder", 8, 5, "weapon"),
    Item("Scale Helmet", 0, 15, "head"),
    Item("Bacta Helmet", 0, 20, "head"),
    Item("Scale Chestplate", 0, 30, "chest"),
    Item("Bacta Chestplate", 0, 40, "chest"),
    Item("Scale Leggings", 0, 15, "legs"),
    Item("Bacta Leggings", 0, 20, "legs"),
    Item("Wyvern Incisor Dagger", 16, -5, "weapon"),
    Item("Sword of The Fallen Hero", 30, 0, "weapon"),
    Item("Melted Dragon Slayer Helmet", 999, -4, "head"),
    Item("Triumph of the Dragon's Lair Chestplate", -100, 20, "chest"),
    Item("Ice Walker Leggings", 0, 300, "legs"),
    Item("Swift Dragon Webbing Scythe", 999, 0, "weapon")
]

combine_zone = pygame.Rect(550, 200, 200, 200)
combined_item = None

def combine_items(selected):
    if len(selected) < 2:
        return None
    base = selected[0]
    return Item(f"Upgraded {base.name}", base.dmg + 1, base.hp + 2, base.type)

running = True
selected_items = []
dragging_item = None

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for item in items:
                if item.rect.collidepoint(event.pos):
                    dragging_item = item
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_item and combine_zone.collidepoint(event.pos):
                selected_items.append(dragging_item)
                items.remove(dragging_item)
                if len(selected_items) >= 2:
                    combined_item = combine_items(selected_items)
                    selected_items = []
            dragging_item = None
        elif event.type == pygame.MOUSEMOTION and dragging_item:
            dragging_item.rect.topleft = event.pos

    pygame.draw.rect(screen, GRAY, (50, 50, 400, 500))
    for i, item in enumerate(items):
        item.rect.topleft = (60 + i * 60, 60)
        item.draw(screen)

    pygame.draw.rect(screen, GRAY, combine_zone)
    if combined_item:
        combined_item.rect.topleft = combine_zone.center
        combined_item.rect.x -= combined_item.rect.width // 2
        combined_item.rect.y -= combined_item.rect.height // 2
        combined_item.draw(screen)

    pygame.display.flip()

