from local import COORDINATES_OF_POSITIONS
from Player import Player
from WeightCard import WeightCard
from BonusCardTake import BonusCardTake
from BonusDeletePlayerCard import BonusDeletePlayerCard
from BonusDeleteComputerCard import BonusDeleteComputerCard


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

    def is_profit(self, next_weight):
        next_score = self.get_score() + next_weight
        next_win_distance = abs(21 - next_score)
        if next_win_distance < self.get_win_distance() and next_score <= 21:
            return True
        return False

    def check_bonus_cards(self, game):
        weight_from_deck = game.deck.deck[-1].get_weight() if game.deck.get_deck() else 0
        for pos_id, card in enumerate(self.deck):
            if type(card) == BonusCardTake:
                # Проверяем наличие карты в колоде:
                for deck_card_pos_id, deck_card in enumerate(game.deck.get_deck()):
                    if type(deck_card) == WeightCard:
                        if deck_card.get_weight() == card.card_weight_to_take:  # Если карта есть в колоде
                            bonus_weight = card.card_weight_to_take
                            if not self.is_profit(weight_from_deck):
                                if self.is_profit(bonus_weight):
                                    card.activate(game, pos_id)
                                    print(f"Б Компьютер берёт карту с весом {bonus_weight}")
                                elif self.is_profit(weight_from_deck + bonus_weight):
                                    card.activate(game, pos_id)
                                    print(f"Б Компьютер берёт карту с весом {bonus_weight} (+{weight_from_deck})")
                            break
                else:
                    if self.get_count_cards() == 8 and game.deck.get_deck():  # освобождаем место
                        card.activate(game, pos_id)
                        print(f"Б Компьютер освобождает место")

            elif type(card) == BonusDeleteComputerCard:
                last_weight_card_id = len(self.deck) - 1
                if last_weight_card_id == pos_id:  # если удаляемая карта идёт за бонусной
                    last_weight_card_id -= 1
                if last_weight_card_id >= 0:  # Если существует такая карта
                    weight = self.deck[last_weight_card_id].get_weight()
                    if self.is_profit(-weight):
                        card.activate(game, pos_id)
                        print(f"Б Компьютер удалил у себя карту с весом {weight}")
                    elif self.is_profit(weight_from_deck - weight) and not self.is_profit(weight_from_deck):
                        card.activate(game, pos_id)
                        print(f"Б Компьютер удалил у себя карту с весом {weight} для взятия карты из колоды")

            elif type(card) == BonusDeletePlayerCard:
                last_weight_card_id = len(game.player.deck) - 1
                if last_weight_card_id == pos_id:  # если удаляемая карта идёт за бонусной
                    last_weight_card_id -= 1
                if last_weight_card_id >= 0:  # Если существует такая карта
                    weight = game.player.deck[last_weight_card_id].get_weight()
                    # если применение карты принесёт выгоду
                    if not self.is_profit(-weight):
                        card.activate(game, pos_id)
                        print(f"Б Компьютер удалил у игрока карту с весом {weight}")

    def get_a_move(self, *args, **kwargs):
        game = kwargs["game"]

        # Анализ бонусных карт
        self.check_bonus_cards(game)

        # Если в колоде закончились карты:
        if game.deck.get_count_cards() == 0:
            print("Компьютер пропускает ход из-за пустой колоды")
            return "pass"

        # Если заполнена колода:
        if self.get_count_cards() == 8:
            print("Компьютер пропускает ход из-за превышения количества карт")
            return "pass"

        # Если следующая карта бонусная:
        if game.deck.deck[-1].is_bonus_card():
            print("BonusCard")
            return "get"

        # Если следующая карта из колоды улучшает пложение:
        if self.is_profit(game.deck.deck[-1].get_weight() if game.deck.get_deck() else 0):
            print("Компьютер улучшает своё положение")
            return "get"

        print("Компьютер пропускает")
        return "pass"


