import pygame
import pygame_gui

from local import WINDOW_SIZE, FPS
from MenuGUI import MenuGUI
from GameLoader import GameLoader
from Messanger import Messanger


def main():
    game_loader = GameLoader()
    menu_gui = MenuGUI()
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
                if event.ui_element == menu_gui.start_button:
                    game_loader.load(screen)
                elif event.ui_element == menu_gui.rules_button:
                    main_menu_messanger.show_message(menu_gui.rules, screen)
                elif event.ui_element == menu_gui.quit_button:
                    running = False
            menu_gui.manager.process_events(event)

        menu_gui.manager.update(FPS)
        screen.blit(menu_gui.menu_background, (0, 0))
        menu_gui.manager.draw_ui(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("21")
    screen = pygame.display.set_mode(WINDOW_SIZE)
    main()
