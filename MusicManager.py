import pygame

from local import SOUND_PATHS


class MusicManager:
    def __init__(self):
        self.music_volume = 0.5
        self.pause = False
        self.volume_step = 0.05

    def load_menu_music(self):
        pygame.mixer.music.load(SOUND_PATHS["menu"])
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

    def load_game_music(self):
        pygame.mixer.music.load(SOUND_PATHS["game"])
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

    def to_pause(self):
        self.pause = not self.pause
        if self.pause:
            pygame.mixer.music.pause()
            print("pause")
        else:
            pygame.mixer.music.unpause()
            print("unpause")

    def decrease_volume(self):
        self.music_volume -= self.volume_step
        if self.music_volume < 0:
            self.music_volume = 0
        pygame.mixer.music.set_volume(self.music_volume)
        print(pygame.mixer.music.get_volume())

    def increase_volume(self):
        self.music_volume += self.volume_step
        if self.music_volume > 1:
            self.music_volume = 1
        pygame.mixer.music.set_volume(self.music_volume)
        print(pygame.mixer.music.get_volume())
