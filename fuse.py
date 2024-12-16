import pygame
import sys
import inventory


def run_fuse_screen(screen, back_to_game):
    pygame.init()

    # GUI
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    FONT = pygame.font.Font(None, 36)
    INVENTORY_FONT = pygame.font.Font(None, 17)

    screen_width, screen_height = screen.get_size()

    inventory_full_message = None  # když je inventář full, tak napíše zprávu

    back_button = pygame.Rect(50, 50, 75, 50)
    fuse_button = pygame.Rect((screen_width - 1200) / 2, screen_height - 100, 150, 50)

    item_slots = [
        pygame.Rect((screen_width / 2) - 580, (screen_height / 2) - 100, 80, 80),
        pygame.Rect((screen_width / 2) - 580, (screen_height / 2) - 10, 80, 80),
        pygame.Rect((screen_width / 2) - 580, (screen_height / 2) + 80, 80, 80),
    ]

    items = [None, None, None]
    fused_item = None

    def draw_items():
        for i, slot in enumerate(item_slots):
            pygame.draw.rect(screen, WHITE, slot)
            if items[i]:
                pygame.draw.rect(screen, GREEN, slot)  # Pokud je ve slotu předmět -> barva slotu je zelená
                item_text = INVENTORY_FONT.render(items[i].name, True, BLACK)
                screen.blit(item_text, (slot.x + 5, slot.y + 5))

    def fuse_items():
        nonlocal fused_item, inventory_full_message
        if all(items) and len(set(item.name for item in items)) == 1:
            fused_item = inventory.upgrade_item(items[0])
            for _, cell in inventory.inventory_cells.items():
                if cell.item is None:
                    cell.item = fused_item
                    fused_item = None
                    inventory_full_message = None 
                    break
            else:
                inventory_full_message = "Inventář je plnej!" 

            for i in range(3):
                items[i] = None
        else:
            fused_item = None

    def draw_inventory():
        for _, cell in inventory.inventory_cells.items():
            pygame.draw.rect(screen, BLACK, (cell.x, cell.y, cell.width, cell.height), 2)
            if cell.item:
                item_text = INVENTORY_FONT.render(cell.item.name, True, BLACK)
                screen.blit(item_text, (cell.x + 5, cell.y + 5))

            if inventory_full_message:
                message_text = FONT.render(inventory_full_message, True, RED)
                screen.blit(message_text, (screen_width // 2 - message_text.get_width() // 2, screen_height // 2 + 200))

    def handle_inventory_click(mouse_pos): # zpracuje kliknutí v inventáři -> do fuse slotu
        for _, cell in inventory.inventory_cells.items():
            if (
                cell.x <= mouse_pos[0] <= cell.x + cell.width
                and cell.y <= mouse_pos[1] <= cell.y + cell.height
                and cell.item
            ):
                for i, slot_item in enumerate(items):
                    if slot_item is None:
                        items[i] = cell.item  
                        cell.item = None  # najde první volný místo ve fuse slotu, dá tam item, odebere ho z inventáře
                        return

    def handle_slot_click(mouse_pos): # dělá to samý, ajko ta nad tím, ale naopak
        for i, slot in enumerate(item_slots):
            if slot.collidepoint(mouse_pos):
                if items[i]:
                    
                    for _, cell in inventory.inventory_cells.items():
                        if cell.item is None:
                            cell.item = items[i]  
                            items[i] = None  # dělá opak toho, co ta nahoře
                            return

    running = True
    while running:
        screen.fill(GRAY)

        pygame.draw.rect(screen, RED, back_button)
        pygame.draw.rect(screen, GREEN, fuse_button)
        screen.blit(FONT.render("Back", True, BLACK), (back_button.x + 10, back_button.y + 10))
        screen.blit(FONT.render("Fuse", True, BLACK), (fuse_button.x + 50, fuse_button.y + 10))

        draw_items()
        draw_inventory()

        if fused_item:
            result_text = FONT.render(f"Výsledek: {fused_item.name}", True, BLACK)
            screen.blit(result_text, ((screen_width - result_text.get_width()) / 2, screen_height / 2 + 150))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                if back_button.collidepoint(mouse_pos):
                    running = False
                    back_to_game()

                elif fuse_button.collidepoint(mouse_pos):
                    fuse_items()

                handle_inventory_click(mouse_pos)  
                handle_slot_click(mouse_pos)  

# TEST fuse.py - stejne nefunguje

if __name__ == "__main__":
    pygame.init()
    test_screen = pygame.display.set_mode((800, 600))

    def dummy_back_to_game():
        print("Zpátky do hry...")

    run_fuse_screen(test_screen, dummy_back_to_game)

