import pygame
import pygame_gui

from local import WINDOW_SIZE, FPS
from local import IMAGE_PATHS
from MenuGUI import MenuGUI
from GameLoader import GameLoader
from MusicManager import MusicManager


def main():
    game_loader = GameLoader()
    menu_gui = MenuGUI()
    music_manager = MusicManager()
    music_manager.load_menu_music()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get().copy():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    music_manager.to_pause()
                elif event.key == pygame.K_LEFT:
                    music_manager.decrease_volume()
                elif event.key == pygame.K_RIGHT:
                    music_manager.increase_volume()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == menu_gui.start_button:
                    game_loader.load(screen)
                    music_manager.load_menu_music()
                elif event.ui_element == menu_gui.rules_button:
                    menu_gui.show_rules(screen)
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
    pygame.display.set_icon(pygame.image.load(IMAGE_PATHS["icon"]))
    screen = pygame.display.set_mode(WINDOW_SIZE)
    main()
