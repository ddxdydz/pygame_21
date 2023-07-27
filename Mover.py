import pygame

from WeightCard import WeightCard
from local import COORDINATES_OF_POSITIONS
from local import BUTTON_DECK_PARAMETERS
from local import BUTTON_PASS_PARAMETERS


class Mover:
    def __init__(self):
        self.is_passed = False
        self.count_defeats = 0
        self.deck = []

    def restart(self):
        self.delete_weight_cards()
        self.is_passed = False

    def delete_weight_cards(self):
        for pos_id in range(len(self.deck) - 1, -1, -1):
            if type(self.deck[pos_id]) == WeightCard:
                self.deck.pop(pos_id)

    def update_card_positions(self):
        for pos_id, card in enumerate(self.deck):
            x, _ = COORDINATES_OF_POSITIONS["player_deck"][pos_id]  # Передвижение идёт только по X
            y = card.rect.y  # Y без изменения
            card.switch_position((x, y))

    def delete_last_card(self):
        if self.get_count_cards():
            self.deck.pop(-1)

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

    def get_score(self):
        score = 0
        for card in self.deck:
            score += card.get_weight()
        return score

    def get_win_distance(self):
        return abs(21 - self.get_score())

    def draw_deck(self, screen_for_draw):
        self.update_card_positions()
        for card in self.deck:
            card.draw(screen_for_draw)
