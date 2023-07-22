import sys
import pygame

from Game import Game
from Messanger import Messanger
from local import WINDOW_SIZE, FPS


class GameLoader:
    def load(self, screen):
        messanger = Messanger()
        game = Game(messanger, screen)

        clock = pygame.time.Clock()
        running = True
        while running:
            events = pygame.event.get().copy()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if game.is_over:
                running = False
            game.update(events, screen)

            pygame.display.flip()
            clock.tick(FPS)
