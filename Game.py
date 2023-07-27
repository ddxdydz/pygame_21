from local import MESSAGES
from Background import Background
from Deck import Deck
from Computer import Computer
from Player import Player


class Game:
    def __init__(self, messanger, screen):
        self.messanger = messanger
        self.screen = screen

        self.player = Player()
        self.computer = Computer()
        self.deck = Deck()
        self.background = Background()

        self.current_mover = self.player
        self.add_default_cards()

        self.is_over = False

    def restart(self):
        self.player.restart()
        self.computer.restart()
        self.deck.restart()
        self.add_default_cards()
        self.current_mover = self.player

    def add_default_cards(self):
        self.deck.transfer_card_for_object(self.player)
        self.deck.transfer_card_for_object(self.computer)

    def show_message(self, message, show_computer_cards=True):
        if show_computer_cards:
            self.computer.show_cards()
        self.draw(self.screen)
        self.messanger.show_message(message, self.screen)
        self.computer.close_first_weight_card()

    def player_defeat(self):
        self.show_message(MESSAGES["computer_win"])
        self.player.add_defeat()
        self.background.add_player_defeat()

    def computer_defeat(self):
        self.show_message(MESSAGES["player_win"])
        self.computer.add_defeat()
        self.background.add_computer_defeat()

    def round_draw(self):
        self.show_message(MESSAGES["draw"])

    def switch_mover(self):
        if type(self.current_mover) == Player:
            self.current_mover = self.computer
        else:
            self.current_mover = self.player
        self.current_mover.to_open()

    def is_all_passed(self):
        if self.computer.is_passed and self.player.is_passed:
            if self.player.get_score() == self.computer.get_score() == 21:
                self.round_draw()
            elif self.player.get_score() > 21:
                self.show_message(MESSAGES["out_of_range"])
                self.player_defeat()
            elif self.computer.get_score() > 21:
                self.computer_defeat()
            elif self.computer.get_win_distance() < self.player.get_win_distance():
                self.player_defeat()
            elif self.computer.get_win_distance() > self.player.get_win_distance():
                self.computer_defeat()
            else:
                self.round_draw()
            if not self.check_over():
                self.restart()
            return True
        return False

    def check_over(self):
        if self.computer.get_count_defeats() == 3:
            self.show_message(MESSAGES["THE PLAYER WON THE GAME"])
            self.is_over = True
        elif self.player.get_count_defeats() == 3:
            self.show_message(MESSAGES["THE COMPUTER WON THE GAME"])
            self.is_over = True

    def draw(self, screen_for_draw):
        self.background.draw(screen_for_draw)
        self.deck.draw(screen_for_draw)
        self.player.draw_deck(screen_for_draw)
        self.computer.draw_deck(screen_for_draw)

    def update(self, events, screen_for_draw):
        self.screen = screen_for_draw

        move_res = self.current_mover.get_a_move(events=events, game=self)
        if move_res == "get":
            if self.deck.get_count_cards() == 0:
                self.show_message(MESSAGES["empty_deck"], show_computer_cards=False)
            elif self.current_mover.get_count_cards() == 8:
                self.show_message(MESSAGES["card_limit"], show_computer_cards=False)
            else:
                self.deck.transfer_card_for_object(self.current_mover)
                self.switch_mover()
        elif move_res == "pass":
            self.current_mover.to_pass()
            if not self.is_all_passed():
                self.switch_mover()

        self.draw(screen_for_draw)

        # FOR DEBUGS:
        if move_res == "get" or move_res == "pass":
            print(move_res, self.current_mover)
