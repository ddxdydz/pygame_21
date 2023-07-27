import pygame

from local import IMAGE_PATHS
from local import COUNT_OF_PIXELS_FOR_RAISING


class Card(pygame.sprite.Sprite):
    def __init__(self, coordinates, image_id, is_closed=True, bonus_card=False):
        pygame.sprite.Sprite.__init__(self)
        self.opened_image = pygame.image.load(IMAGE_PATHS[image_id]).convert_alpha()
        self.closed_image = pygame.image.load(IMAGE_PATHS["rubachka"]).convert_alpha()
        self.rect = self.opened_image.get_rect()
        self.rect.x, self.rect.y = coordinates
        self.is_closed = is_closed
        self.bonus_card = bonus_card
        self.raising = False

    def switch_position(self, coordinates):
        self.rect.x, self.rect.y = coordinates

    def is_bonus_card(self):
        return self.bonus_card

    def get_weight(self):
        return 0

    def open(self):
        self.is_closed = False

    def close(self):
        self.is_closed = True

    def enable_raising(self):
        self.raising = True

    def disable_raising(self):
        self.raising = False

    def draw(self, screen_for_draw):
        current_rect = self.opened_image.get_rect()
        current_rect.x, current_rect.y = self.rect.x, self.rect.y

        if self.raising:
            current_rect.y -= COUNT_OF_PIXELS_FOR_RAISING

        if self.is_closed:
            screen_for_draw.blit(self.closed_image, current_rect)
        else:
            screen_for_draw.blit(self.opened_image, current_rect)
