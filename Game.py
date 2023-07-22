from messages import MESSAGES
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

        self.is_over = False

    def restart(self):
        self.player.restart()
        self.computer.restart()
        self.deck.restart()
        self.current_mover = self.player

    def show_message(self, message):
        self.computer.show_first_card()
        self.draw(self.screen)
        self.messanger.show_message(message, self.screen)

    def player_win(self):
        self.show_message(MESSAGES["player_win"])
        self.player.add_win()
        self.background.add_player_win()
        self.restart()

    def computer_win(self):
        self.show_message(MESSAGES["computer_win"])
        self.computer.add_win()
        self.background.add_computer_win()
        self.restart()

    def switch_mover(self):
        if type(self.current_mover) == Player:
            self.current_mover = self.computer
        else:
            self.current_mover = self.player
        self.current_mover.to_open()

    def check_wins(self):
        if self.player.get_score() > 21:
            self.show_message(MESSAGES["out_of_range"])
            self.computer_win()
        elif self.computer.get_score() > 21:
            self.player_win()
        elif self.computer.is_passed and self.player.is_passed or \
                self.deck.get_count_cards() == 0:
            if self.computer.get_win_distance() < self.player.get_win_distance():
                self.computer_win()
            elif self.computer.get_win_distance() > self.player.get_win_distance():
                self.player_win()
            else:  # Ничья
                self.show_message(MESSAGES["draw"])
                self.restart()

    def check_over(self):
        if self.computer.get_count_wins() == 3:
            self.show_message(MESSAGES["THE COMPUTER WON THE GAME"])
            self.is_over = True
        elif self.player.get_count_wins() == 3:
            self.show_message(MESSAGES["THE PLAYER WON THE GAME"])
            self.is_over = True

    def process_a_move(self, move):
        if move == "get":
            if self.current_mover.get_count_cards() == 8:
                pass
            else:
                self.deck.transfer_card_for_object(self.current_mover)
        else:
            self.current_mover.to_pass()

    def draw(self, screen_for_draw):
        self.background.draw(screen_for_draw)
        self.deck.draw(screen_for_draw)
        self.player.draw_deck(screen_for_draw)
        self.computer.draw_deck(screen_for_draw)

    def update(self, events, screen_for_draw):
        self.screen = screen_for_draw
        if not self.is_over:
            move_res = "pass"

            # Игрок может взять карту если у него неполная колода:
            if self.current_mover.get_count_cards() < 8:
                move_res = self.current_mover.get_a_move(events=events, game=self)

            if move_res != "waiting...":
                print(move_res, self.current_mover)
                self.process_a_move(move_res)
                self.check_wins()
                self.check_over()
                self.switch_mover()
            self.draw(screen_for_draw)
