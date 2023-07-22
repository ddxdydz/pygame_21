import pygame
from random import shuffle

from Card import Card
from local import COORDINATES_OF_POSITIONS
from local import CARDS_IDS


class Deck:
    def __init__(self):
        self.deck = []
        self.coordinates = COORDINATES_OF_POSITIONS["main_deck"]
        self.restart()

    def transfer_card_for_object(self, obj):
        if self.deck:
            transfer_card = self.deck.pop(-1)  # Удаляем последнюю карту из колоды
            obj.add_card(transfer_card)  # Передаем эту карту получателю

    def get_count_cards(self):
        return len(self.deck)

    def restart(self):
        self.deck.clear()
        for card_id in CARDS_IDS:
            self.deck.append(Card(card_id, self.coordinates))
        shuffle(self.deck)  # Мешаем колоду

    def draw(self, screen_for_draw):
        for card in self.deck:
            card.draw(screen_for_draw)
