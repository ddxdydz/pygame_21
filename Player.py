import pygame

from local import COORDINATES_OF_POSITIONS
from local import BUTTON_DECK_PARAMETERS
from local import BUTTON_PASS_PARAMETERS


class Player:
    def __init__(self):
        self.is_passed = False
        self.count_defeats = 0
        self.deck = []

        self.button_deck_rect = pygame.Rect(*BUTTON_DECK_PARAMETERS)
        self.button_pass_rect = pygame.Rect(*BUTTON_PASS_PARAMETERS)

    def restart(self):
        self.deck.clear()
        self.is_passed = False

    def to_pass(self):
        self.is_passed = True

    def to_open(self):
        self.is_passed = False

    def get_count_cards(self):
        return len(self.deck)

    def add_defeat(self):
        self.count_defeats += 1

    def get_count_defeats(self):
        return self.count_defeats

    def add_card(self, card):
        self.deck.append(card)
        card_position = self.get_count_cards() - 1  # Получаем ид позиции карты
        card.switch_position(COORDINATES_OF_POSITIONS["player_deck"][card_position])
        card.open()

    def get_score(self):
        score = 0
        for card in self.deck:
            score += card.get_weight()
        return score

    def get_win_distance(self):
        return abs(21 - self.get_score())

    def draw_deck(self, screen_for_draw):
        for card in self.deck:
            card.draw(screen_for_draw)

    def check_mouse_button_hover(self, *args, **kwargs):
        mouse_pos = pygame.mouse.get_pos()
        game = kwargs["game"]
        if self.button_pass_rect.collidepoint(mouse_pos):
            game.background.pass_card.enable_raising()
        else:
            game.background.pass_card.disable_raising()
        if game.deck.get_count_cards() != 0:
            if self.button_deck_rect.collidepoint(mouse_pos):
                game.deck.deck[-1].enable_raising()
            else:
                game.deck.deck[-1].disable_raising()

    def get_a_move(self, *args, **kwargs):

        # Проверяем наведение на кнопки:
        self.check_mouse_button_hover(*args, **kwargs)

        # Проверяем нажатие на кнопки:
        events = kwargs["events"]
        game = kwargs["game"]
        if events and events[0].type == pygame.MOUSEBUTTONDOWN:
            # Если нажата кнопка для пропуска хода:
            if self.button_pass_rect.collidepoint(events[0].pos):
                return "pass"
            # Если нажата кнопка для взятия карты:
            elif self.button_deck_rect.collidepoint(events[0].pos):
                if game.deck.get_count_cards() != 0:  # опускаем взятую карту
                    game.deck.deck[-1].disable_raising()
                return "get"
        return "waiting..."
