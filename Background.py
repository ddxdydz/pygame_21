import pygame

from local import IMAGE_PATHS
from local import COORDINATES_OF_POSITIONS


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.background_image = pygame.image.load(IMAGE_PATHS["background"]).convert_alpha()
        self.background_rect = self.background_image.get_rect()
        self.background_rect.x, self.background_rect.y = COORDINATES_OF_POSITIONS["background"]

        self.player_image = pygame.image.load(IMAGE_PATHS["player_profile"]).convert_alpha()
        self.player_rect = self.player_image.get_rect()
        self.player_rect.x, self.player_rect.y = COORDINATES_OF_POSITIONS["player_profile"]

        self.computer_image = pygame.image.load(IMAGE_PATHS["computer_profile"]).convert_alpha()
        self.computer_rect = self.computer_image.get_rect()
        self.computer_rect.x, self.computer_rect.y = COORDINATES_OF_POSITIONS["computer_profile"]

        self.win_mark_image = pygame.image.load(IMAGE_PATHS["win_mark"]).convert_alpha()
        self.win_mark_rect = self.computer_image.get_rect()

        self.player_wins_count = 0
        self.computer_wins_count = 0

    def add_computer_win(self):
        self.computer_wins_count += 1

    def add_player_win(self):
        self.player_wins_count += 1

    def draw(self, screen_for_draw):
        screen_for_draw.blit(self.background_image, self.background_rect)

        # Выводим на экран картинки профилей игрока и компьютера:
        screen_for_draw.blit(self.player_image, self.player_rect)
        screen_for_draw.blit(self.computer_image, self.computer_rect)

        # Выводим на экран отмеки показателей кол-ва побед для компьютера:
        for i in range(self.computer_wins_count):
            self.win_mark_rect.x, self.win_mark_rect.y = \
                COORDINATES_OF_POSITIONS["computer_win_marks"][i]
            screen_for_draw.blit(self.win_mark_image, self.win_mark_rect)

        # Выводим на экран отмеки показателей кол-ва побед для игрока:
        for i in range(self.player_wins_count):
            self.win_mark_rect.x, self.win_mark_rect.y = \
                COORDINATES_OF_POSITIONS["player_win_marks"][i]
            screen_for_draw.blit(self.win_mark_image, self.win_mark_rect)
