import pygame
import sys

def run_fuse_screen(screen, back_to_game):
    pygame.init()

    # gui
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    FONT = pygame.font.Font(None, 36)

    screen_width, screen_height = screen.get_size()

    back_button = pygame.Rect(50, 50, 75, 50)  
    fuse_button = pygame.Rect((screen_width - 200) / 2, screen_height - 100, 150, 50)  

    item_slots = [
        pygame.Rect((screen_width / 2) - 150, (screen_height / 2) - 100, 100, 100),  
        pygame.Rect((screen_width / 2) - 50, (screen_height / 2) - 100, 100, 100),  
        pygame.Rect((screen_width / 2) + 50, (screen_height / 2) - 100, 100, 100)    
    ]

    # placeholder pro itemy

    items = [None, None, None]  
    fused_item = None  

    def draw_items():
        for i, slot in enumerate(item_slots):
            pygame.draw.rect(screen, WHITE, slot) 
            if items[i]:
                pygame.draw.rect(screen, GREEN, slot)  # pokud je ve slotu předmět -> barva slotu je zelena

    def fuse_items():
        nonlocal fused_item
        if all(items):  
            fused_item = "evoluce itemu"  # pokud ve všech slotech je item -> evoluce
        else:
            fused_item = None

    running = True
    while running:
        screen.fill(GRAY)

        pygame.draw.rect(screen, RED, back_button)
        pygame.draw.rect(screen, GREEN, fuse_button)
        screen.blit(FONT.render("Back", True, BLACK), (back_button.x + 10, back_button.y + 10))
        screen.blit(FONT.render("Fuse", True, BLACK), (fuse_button.x + 50, fuse_button.y + 10))

        draw_items() # pro nejaky itemy

        if fused_item:
            result_text = FONT.render(f"Result: {fused_item}", True, BLACK)
            screen.blit(result_text, ((screen_width - result_text.get_width()) / 2, screen_height / 2 + 50)) # pro evoluci itemu až bude

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

               
                for i, slot in enumerate(item_slots):
                    if slot.collidepoint(mouse_pos):
                        if items[i]:
                            items[i] = None  
                        else:
                            items[i] = f"Item {i + 1}"  #kontrola přidání a odebrání itemu

# TEST fuse.py

if __name__ == "__main__":
    pygame.init()
    test_screen = pygame.display.set_mode((800, 600))

    def dummy_back_to_game():
        print("Returning to game...")

    run_fuse_screen(test_screen, dummy_back_to_game)

