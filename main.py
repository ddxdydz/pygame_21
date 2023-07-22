import pygame

from Game import Game
from Messanger import Messanger
from local import WINDOW_SIZE, FPS


pygame.init()
pygame.display.set_caption("21")
screen = pygame.display.set_mode(WINDOW_SIZE)


def main():
    # Главный игровой цикл:
    messanger = Messanger()
    game = Game(messanger, screen)

    clock = pygame.time.Clock()
    running = True
    while running:

        # Цикл приема и обработки сообщений:
        events = pygame.event.get().copy()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if game.is_over:
            running = False

        game.update(events, screen)

        pygame.display.flip()  # смена кадра
        clock.tick(FPS)  # временная задержка
    pygame.quit()


if __name__ == "__main__":
    main()
