import pygame
from random import choice

from local import IMAGE_PATHS
from local import COORDINATES_OF_POSITIONS
from Card import Card


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.background_image0 = pygame.image.load(IMAGE_PATHS["Table1"]).convert_alpha()
        self.background_image1 = pygame.image.load(IMAGE_PATHS["Table2"]).convert_alpha()
        self.background_image2 = pygame.image.load(IMAGE_PATHS["Table3"]).convert_alpha()
        self.background_rect = self.background_image1.get_rect()
        self.background_rect.x, self.background_rect.y = COORDINATES_OF_POSITIONS["background"]

        self.player_image = pygame.image.load(IMAGE_PATHS["player_profile"]).convert_alpha()
        self.player_image_angry = pygame.image.load(IMAGE_PATHS["player_angry"]).convert_alpha()
        self.player_rect = self.player_image.get_rect()
        self.player_rect.x, self.player_rect.y = COORDINATES_OF_POSITIONS["player_profile"]

        self.computer_image = pygame.image.load(IMAGE_PATHS["computer_profile"]).convert_alpha()
        self.computer_image_angry = pygame.image.load(IMAGE_PATHS["computer_angry"]).convert_alpha()
        self.computer_rect = self.computer_image.get_rect()
        self.computer_rect.x, self.computer_rect.y = COORDINATES_OF_POSITIONS["computer_profile"]

        self.defeat_mark_image0 = pygame.image.load(IMAGE_PATHS["lose_marker"]).convert_alpha()
        self.defeat_mark_image1 = pygame.image.load(IMAGE_PATHS["lose_marker1"]).convert_alpha()
        self.defeat_mark_image2 = pygame.image.load(IMAGE_PATHS["lose_marker2"]).convert_alpha()
        self.defeat_mark_rect = self.computer_image.get_rect()

        self.card_place = pygame.image.load(IMAGE_PATHS["card_place"]).convert_alpha()
        self.card_place1 = pygame.image.load(IMAGE_PATHS["card_place1"]).convert_alpha()
        self.card_place2 = pygame.image.load(IMAGE_PATHS["card_place2"]).convert_alpha()
        self.card_place_rect = self.card_place.get_rect()

        self.pass_card = Card(coordinates=COORDINATES_OF_POSITIONS["pass_button"], image_id="pass")
        self.pass_card.open()

        self.computer_places_cards = []
        self.player_places_cards = []
        self.init_places_cards()

        self.player_defeats_count = 0
        self.computer_defeats_count = 0

    def add_computer_defeat(self):
        self.computer_defeats_count += 1

    def add_player_defeat(self):
        self.player_defeats_count += 1

    def init_places_cards(self):
        places_cards = (self.card_place, self.card_place, self.card_place, self.card_place,
                        self.card_place, self.card_place, self.card_place, self.card_place,
                        self.card_place, self.card_place, self.card_place1, self.card_place2)
        for _ in range(8):
            self.computer_places_cards.append(choice(places_cards))
        for _ in range(8):
            self.player_places_cards.append(choice(places_cards))

    def draw_background(self, screen_for_draw):
        if self.player_defeats_count == 1:
            screen_for_draw.blit(self.background_image1, self.background_rect)
        elif self.player_defeats_count == 2:
            screen_for_draw.blit(self.background_image2, self.background_rect)
        else:
            screen_for_draw.blit(self.background_image0, self.background_rect)

    def draw_places_cards(self, screen_for_draw):
        for pos_id, card_img in enumerate(self.computer_places_cards):
            self.card_place_rect.x, self.card_place_rect.y = \
                COORDINATES_OF_POSITIONS["computer_deck"][pos_id]
            screen_for_draw.blit(card_img, self.card_place_rect)
        for pos_id, card_img in enumerate(self.player_places_cards):
            self.card_place_rect.x, self.card_place_rect.y = \
                COORDINATES_OF_POSITIONS["player_deck"][pos_id]
            screen_for_draw.blit(card_img, self.card_place_rect)

    def draw_profiles(self, screen_for_draw):
        if self.player_defeats_count < 2:
            screen_for_draw.blit(self.player_image, self.player_rect)
        else:
            screen_for_draw.blit(self.player_image_angry, self.player_rect)
        if self.computer_defeats_count < 2:
            screen_for_draw.blit(self.computer_image, self.computer_rect)
        else:
            screen_for_draw.blit(self.computer_image_angry, self.computer_rect)

    def draw_pass_button(self, screen_for_draw):
        self.pass_card.draw(screen_for_draw)

    def draw_defeat_marks(self, screen_for_draw):
        # Выводим места для отметок:
        for pos_id in range(3):
            self.defeat_mark_rect.x, self.defeat_mark_rect.y = \
                COORDINATES_OF_POSITIONS["player_defeat_marks"][pos_id]
            screen_for_draw.blit(self.defeat_mark_image0, self.defeat_mark_rect)
            self.defeat_mark_rect.x, self.defeat_mark_rect.y = \
                COORDINATES_OF_POSITIONS["computer_defeat_marks"][pos_id]
            screen_for_draw.blit(self.defeat_mark_image0, self.defeat_mark_rect)

        # Выводим на экран отмеки показателей кол-ва поражений для компьютера:
        for i in range(self.computer_defeats_count):
            if i == 2:
                self.defeat_mark_rect.x, self.defeat_mark_rect.y = \
                    COORDINATES_OF_POSITIONS["computer_defeat_marks"][i]
                screen_for_draw.blit(self.defeat_mark_image2, self.defeat_mark_rect)
            else:
                self.defeat_mark_rect.x, self.defeat_mark_rect.y = \
                    COORDINATES_OF_POSITIONS["computer_defeat_marks"][i]
                screen_for_draw.blit(self.defeat_mark_image1, self.defeat_mark_rect)

        # Выводим на экран отмеки показателей кол-ва поражений для игрока:
        for i in range(self.player_defeats_count):
            if i == 2:
                self.defeat_mark_rect.x, self.defeat_mark_rect.y = \
                    COORDINATES_OF_POSITIONS["player_defeat_marks"][i]
                screen_for_draw.blit(self.defeat_mark_image2, self.defeat_mark_rect)
            else:
                self.defeat_mark_rect.x, self.defeat_mark_rect.y = \
                    COORDINATES_OF_POSITIONS["player_defeat_marks"][i]
                screen_for_draw.blit(self.defeat_mark_image1, self.defeat_mark_rect)

    def draw(self, screen_for_draw):
        self.draw_background(screen_for_draw)
        self.draw_defeat_marks(screen_for_draw)
        self.draw_profiles(screen_for_draw)
        self.draw_pass_button(screen_for_draw)
        self.draw_places_cards(screen_for_draw)
