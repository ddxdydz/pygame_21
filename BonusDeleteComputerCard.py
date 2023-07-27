from local import MESSAGES
from Card import Card


class BonusDeleteComputerCard(Card):
    def __init__(self, coordinates):
        super().__init__(coordinates, image_id="bonus_delete_computer_last_card", bonus_card=True)

    def activate(self, game, bonus_card_pos_id):
        game.current_mover.deck.pop(bonus_card_pos_id)
        if game.computer.get_count_cards():
            game.computer.delete_last_card()
            if game.current_mover is game.player:
                game.show_message(MESSAGES["successfully_DeleteComputerCard"], show_computer_cards=False)
        else:
            if game.current_mover is game.player:
                game.show_message(MESSAGES["failure_DeleteCard"], show_computer_cards=False)
