from local import MESSAGES
from Card import Card
from WeightCard import WeightCard


class BonusCardTake(Card):
    def __init__(self, coordinates, image_id, card_weight_to_take):
        super().__init__(coordinates, image_id, bonus_card=True)
        self.card_weight_to_take = card_weight_to_take

    def activate(self, game, bonus_card_pos_id):
        game.current_mover.deck.pop(bonus_card_pos_id)
        for card_pos_id, card in enumerate(game.deck.get_deck()):
            if type(card) == WeightCard:
                if card.get_weight() == self.card_weight_to_take:
                    searched_card = game.deck.get_deck().pop(card_pos_id)
                    game.current_mover.add_card(searched_card)
                    break
        else:
            if game.current_mover is game.player:
                game.show_message(MESSAGES["no_bonus_card"], show_computer_cards=False)

