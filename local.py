WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1300, 800
FPS = 130
MESSAGES = {
    "player_win": "Вы выйграли раунд!",
    "computer_win": "Вы проиграли раунд!",
    "out_of_range": "Число 21 превышено",
    "draw": "Ничья",
    "THE COMPUTER WON THE GAME": "ВЫ ПРОИГРАЛИ ИГРУ",
    "THE PLAYER WON THE GAME": "ВЫ ВЫЙГРАЛИ ИГРУ",
    "card_limit": "Достигнуто максимальное \n        количество карт",
    "empty_deck": "Колода пуста",
    "no_bonus_card": "Такой карты нет в колоде",
    "successfully_DeleteComputerCard": "Последняя карта компьютера удалена",
    "successfully_PlayerComputerCard": "Последняя карта игрока удалена",
    "failure_DeleteCard": "Не удалось удалить карту"
}
COORDINATES_OF_POSITIONS = {
    "background": (0, 0),
    "computer_deck": {0: (20, 28), 1: (180, 28), 2: (340, 28), 3: (500, 28), 4: (660, 28), 5: (820, 28), 6: (980, 28), 7: (1140, 28)},
    "player_deck": {0: (20, 570), 1: (180, 570), 2: (340, 570), 3: (500, 570), 4: (660, 570), 5: (820, 570), 6: (980, 570), 7: (1140, 570)},
    "player_profile": (34, 474),
    "computer_profile": (34, 255),
    "player_defeat_marks": {0: (132, 474), 1: (230, 474), 2: (322, 474)},
    "computer_defeat_marks": {0: (132, 255), 1: (230, 255), 2: (322, 255)},
    "main_deck": (1090, 310),
    "pass_button": (921, 309)
}
COUNT_OF_PIXELS_FOR_RAISING = 20
SOUND_PATHS = {
    "menu": r"data\sounds\menu_music.mp3",
    "game": r"data\sounds\game_music.mp3"
}
IMAGE_PATHS = {
    "menu_background": r"data\menu_background.png",
    "player_profile": r"data\player.png",
    "computer_profile": r"data\comp.png",
    "player_angry": r"data\player2.png",
    "computer_angry": r"data\comp2.png",
    "win_mark": r"data\win_marker.png",
    "1": r"data\1.png",
    "2": r"data\2.png",
    "3": r"data\3.png",
    "4": r"data\4.png",
    "5": r"data\5.png",
    "6": r"data\6.png",
    "7": r"data\7.png",
    "8": r"data\8.png",
    "9": r"data\9.png",
    "10": r"data\10.png",
    "11": r"data\11.png",
    "-1": r"data\-1.png",
    "-2": r"data\-2.png",
    "-3": r"data\-3.png",
    "rubachka": r"data\rubashka.png",
    "Table3": r"data\Table3.png",
    "Table2": r"data\Table2.png",
    "Table1": r"data\Table1.png",
    "icon": r"data\icon.png",
    "lose_marker2": r"data\lose_marker2.png",
    "lose_marker1": r"data\lose_marker1.png",
    "lose_marker": r"data\lose_marker.png",
    "card_place2": r"data\card_place2.png",
    "card_place1": r"data\card_place1.png",
    "card_place": r"data\card_place.png",
    "pass": r"data\pass.png",
    "bonus_delete_computer_last_card": r"data\bonus_delete_comp.png",
    "bonus_delete_player_last_card": r"data\bonus_delete_player.png",
    "bonus_take_2": r"data\bonus_2.png",
    "bonus_take_-2": r"data\bonus_-2.png",
    "bonus_take_5": r"data\bonus_5.png",
    "bonus_take_6": r"data\bonus_6.png"
}
WEIGHT_CARDS_IDS = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "-1", "-2", "-3")
BONUS_TAKE_CARDS_IDS = ("2", "-2", "5", "6")
BUTTON_PASS_PARAMETERS = (921, 309, 138, 212)  # (x, y, width, height)
BUTTON_DECK_PARAMETERS = (1090, 310, 138, 212)
