import sys
import pygame

from Game import Game
from Messanger import Messanger
from MusicManager import MusicManager
from local import WINDOW_SIZE, FPS


class GameLoader:
    def load(self, screen):
        messanger = Messanger()
        music_manager = MusicManager()
        music_manager.load_game_music()
        game = Game(messanger, screen)

        clock = pygame.time.Clock()
        running = True
        while running:
            events = pygame.event.get().copy()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        music_manager.to_pause()
                    elif event.key == pygame.K_LEFT:
                        music_manager.decrease_volume()
                    elif event.key == pygame.K_RIGHT:
                        music_manager.increase_volume()
            if game.is_over:
                running = False
            game.update(events, screen)

            pygame.display.flip()
            clock.tick(FPS)
