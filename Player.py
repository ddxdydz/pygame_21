import pygame

from local import COORDINATES_OF_POSITIONS
from local import BUTTON_DECK_PARAMETERS
from local import BUTTON_PASS_PARAMETERS
from Mover import Mover


class Player(Mover):
    def __init__(self):
        super().__init__()

        self.button_deck_rect = pygame.Rect(*BUTTON_DECK_PARAMETERS)
        self.button_pass_rect = pygame.Rect(*BUTTON_PASS_PARAMETERS)

    def add_card(self, card):
        self.deck.append(card)
        card_position = self.get_count_cards() - 1  # Получаем ид позиции карты
        card.switch_position(COORDINATES_OF_POSITIONS["player_deck"][card_position])
        card.open()

    def check_mouse_button_hover(self, *args, **kwargs):
        mouse_pos = pygame.mouse.get_pos()
        game = kwargs["game"]

        # Проверка наведения на кнопку pass
        if self.button_pass_rect.collidepoint(mouse_pos):
            game.background.pass_card.enable_raising()
        else:
            game.background.pass_card.disable_raising()

        # Проверка наведения на кнопку deck
        if game.deck.get_count_cards() != 0:
            if self.button_deck_rect.collidepoint(mouse_pos):
                game.deck.deck[-1].enable_raising()
            else:
                game.deck.deck[-1].disable_raising()

        # Проверка наведения на бонусные карты
        for card in self.deck:
            if card.is_bonus_card():
                if card.rect.collidepoint(mouse_pos):
                    card.enable_raising()
                else:
                    card.disable_raising()

    def get_a_move(self, *args, **kwargs):

        # Проверяем наведение на кнопки:
        self.check_mouse_button_hover(*args, **kwargs)

        # Проверяем нажатие на кнопки:
        events = kwargs["events"]
        game = kwargs["game"]
        if events and events[0].type == pygame.MOUSEBUTTONDOWN:
            # Если нажата кнопка для пропуска хода:
            if self.button_pass_rect.collidepoint(events[0].pos):
                return "pass"
            # Если нажата кнопка для взятия карты:
            elif self.button_deck_rect.collidepoint(events[0].pos):
                if game.deck.get_count_cards() != 0:  # опускаем взятую карту
                    game.deck.deck[-1].disable_raising()
                return "get"
            # Нажатие на бонусную карту:
            for pos_id, card in enumerate(self.deck):
                if card.is_bonus_card():
                    if card.rect.collidepoint(events[0].pos):
                        card.disable_raising()
                        card.activate(game, pos_id)
        return "waiting..."
