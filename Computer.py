import pygame

from Player import Player
from local import COORDINATES_OF_POSITIONS


class Computer(Player):
    def __init__(self):
        super().__init__()

    def add_card(self, card):
        self.deck.append(card)
        card_position = self.get_count_cards() - 1  # Получаем ид позиции карты
        card.switch_position(COORDINATES_OF_POSITIONS["computer_deck"][card_position])
        if card_position != 0:
            card.open()

    def show_first_card(self):
        if self.deck:
            self.deck[0].open()

    def get_a_move(self, *args, **kwargs):
        game = kwargs["game"]

        # Количество очков при взятии следующей карты:
        next_score = self.get_score() + game.deck.deck[-1].get_weight()
        # Если количество очков первышает лимит:
        if next_score > 21:
            print("Компьютер пропускает ход из-за лимита")
            return "pass"
        # Если следующая карта улучшает пложение:
        next_win_distance = abs(21 - (self.get_score() + game.deck.deck[-1].get_weight()))
        if next_win_distance < self.get_win_distance():
            print("Компьютер улучшает своё положение")
            return "get"

        # Если игрок выигрывает:
        if game.player.get_win_distance() < self.get_win_distance():
            print("Компьютер берёт карту")
            return "get"
        print("Компьютер пропускает")
        return "pass"


