import pygame

from local import COORDINATES_OF_POSITIONS
from Player import Player
from WeightCard import WeightCard
from BonusCardTake import BonusCardTake


class Computer(Player):
    def __init__(self):
        super().__init__()

    def add_card(self, card):
        card.open()
        self.deck.append(card)
        card_position = self.get_count_cards() - 1  # Получаем ид позиции карты
        card.switch_position(COORDINATES_OF_POSITIONS["computer_deck"][card_position])
        # Закрываем первую карту без бонуса:
        self.close_first_weight_card()

    def close_first_weight_card(self):
        self.show_cards()
        for card in self.deck:
            if type(card) == WeightCard:
                card.close()
                break

    def show_cards(self):
        for card in self.deck:
            card.open()

    def get_a_move(self, *args, **kwargs):
        game = kwargs["game"]

        # Если в колоде закончились карты:
        if game.deck.get_count_cards() == 0:
            print("Компьютер пропускает ход из-за пустой колоды")
            return "pass"

        # Если заполнена колода:
        if self.get_count_cards() == 8:
            print("Компьютер пропускает ход из-за пустой колоды")
            return "pass"

        # Если следующая карта бонусная:
        if game.deck.deck[-1].is_bonus_card():
            print("BonusCard")
            return "pass"

        # Количество очков при взятии следующей карты:
        next_score = self.get_score() + game.deck.deck[-1].get_weight()
        # Если количество очков первышает лимит:
        if next_score > 21:
            print("Компьютер пропускает ход из-за лимита очков")
            return "pass"
        # Если следующая карта улучшает пложение:
        next_win_distance = abs(21 - (self.get_score() + game.deck.deck[-1].get_weight()))
        if next_win_distance < self.get_win_distance():
            print("Компьютер улучшает своё положение")
            return "get"

        # Если следующим ходом игрок победит:
        if game.player.get_win_distance() < self.get_win_distance():
            print("Компьютер берёт карту")
            return "get"

        print("Компьютер пропускает")
        return "pass"


