import pygame

from local import COORDINATES_OF_POSITIONS
from local import BUTTON_DECK_PARAMETERS
from local import BUTTON_PASS_PARAMETERS


class Player:
    def __init__(self):
        self.is_passed = False
        self.count_wins = 0
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

    def add_win(self):
        self.count_wins += 1

    def get_count_wins(self):
        return self.count_wins

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

    def get_a_move(self, *args, **kwargs):
        # Проверяем нажатие на кнопки:
        events = kwargs["events"]
        if events and events[0].type == pygame.MOUSEBUTTONDOWN:
            # Если нажата кнопка для пропуска хода:
            if self.button_pass_rect.collidepoint(events[0].pos):
                return "pass"
            # Если нажата кнопка для взятия карты:
            elif self.button_deck_rect.collidepoint(events[0].pos):
                return "get"
        return "waiting..."
