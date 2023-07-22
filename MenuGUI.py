import pygame
import pygame_gui

from local import IMAGE_PATHS
from local import WINDOW_SIZE


class MenuGUI:
    def __init__(self):
        self.manager = pygame_gui.UIManager(WINDOW_SIZE)
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 200), (300, 100)),
            text='ИГРАТЬ',
            manager=self.manager
        )
        self.rules_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 350), (300, 100)),
            text='ПРАВИЛА',
            manager=self.manager
        )
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 500), (300, 100)),
            text='ВЫХОД',
            manager=self.manager
        )
        with open(r'data\rules.txt', mode='rt', encoding='UTF-8') as file:
            self.rules = file.read()
        self.menu_background = pygame.image.load(IMAGE_PATHS["menu_background"])