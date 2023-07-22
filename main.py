import pygame
import pygame_gui

from local import WINDOW_SIZE, FPS
from local import IMAGE_PATHS
from GameLoader import GameLoader
from Messanger import Messanger


pygame.init()
pygame.display.set_caption("21")
screen = pygame.display.set_mode(WINDOW_SIZE)

manager = pygame_gui.UIManager(WINDOW_SIZE)
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 200), (300, 100)),
    text='ИГРАТЬ',
    manager=manager
)
rules_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 350), (300, 100)),
    text='ПРАВИЛА',
    manager=manager
)
quit_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 500), (300, 100)),
    text='ВЫХОД',
    manager=manager
)
with open(r'data\rules.txt', mode='rt', encoding='UTF-8') as file:
    rules = file.read()
menu_background = pygame.image.load(IMAGE_PATHS["menu_background"])


def main():
    game_loader = GameLoader()
    main_menu_messanger = Messanger()
    main_menu_messanger.background_screen_color = pygame.Color(20, 20, 20, 255)
    main_menu_messanger.message_font_size = 30
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get().copy():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    game_loader.load(screen)
                elif event.ui_element == rules_button:
                    main_menu_messanger.show_message(rules, screen)
                elif event.ui_element == quit_button:
                    running = False
            manager.process_events(event)
        manager.update(FPS)
        screen.blit(menu_background, (0, 0))
        manager.draw_ui(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
