import pygame
from random import shuffle

from local import COORDINATES_OF_POSITIONS
from local import WEIGHT_CARDS_IDS
from local import BONUS_TAKE_CARDS_IDS
from WeightCard import WeightCard
from BonusCardTake import BonusCardTake
from BonusDeletePlayerCard import BonusDeletePlayerCard
from BonusDeleteComputerCard import BonusDeleteComputerCard


class Deck:
    def __init__(self):
        self.deck = []
        self.coordinates = COORDINATES_OF_POSITIONS["main_deck"]
        self.available_bonus_cards = []
        self.fill_available_bonus_cards_list()
        self.restart()

    def fill_available_bonus_cards_list(self):
        for weight in BONUS_TAKE_CARDS_IDS:
            self.available_bonus_cards.append(
                BonusCardTake(
                    coordinates=self.coordinates,
                    image_id=f"bonus_take_{weight}",
                    card_weight_to_take=int(weight)
                )
            )
        self.available_bonus_cards.append(
            BonusDeletePlayerCard(coordinates=self.coordinates)
        )
        self.available_bonus_cards.append(
            BonusDeleteComputerCard(coordinates=self.coordinates)
        )
        shuffle(self.available_bonus_cards)

    def get_count_cards(self):
        return len(self.deck)

    def get_deck(self):
        return self.deck

    def transfer_card_for_object(self, obj):
        if self.deck and obj.get_count_cards() < 8:
            transfer_card = self.deck.pop(-1)  # Удаляем последнюю карту из колоды
            obj.add_card(transfer_card)  # Передаем эту карту получателю

    def add_weight_cards(self):
        for card_id in WEIGHT_CARDS_IDS:  # Заполнение колоды картами с весами
            self.deck.append(
                WeightCard(coordinates=self.coordinates, image_id=card_id, weight=int(card_id))
            )

    def add_bonus_card(self):
        if self.available_bonus_cards:
            self.deck.append(self.available_bonus_cards.pop(-1))

    def restart(self, add_bonus_cards=True):
        self.deck.clear()
        self.add_weight_cards()
        if add_bonus_cards:
            self.add_bonus_card()
        shuffle(self.deck)  # Мешаем колоду

    def draw(self, screen_for_draw):
        for card in self.deck:
            card.draw(screen_for_draw)
