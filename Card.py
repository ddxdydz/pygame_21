import pygame

from local import IMAGE_PATHS


class Card(pygame.sprite.Sprite):
    def __init__(self, card_id, coordinates, is_closed=True):
        pygame.sprite.Sprite.__init__(self)
        self.opened_image = pygame.image.load(IMAGE_PATHS[card_id]).convert_alpha()
        self.closed_image = pygame.image.load(IMAGE_PATHS["rubachka"]).convert_alpha()
        self.rect = self.opened_image.get_rect()
        self.rect.x, self.rect.y = coordinates
        self.is_closed = is_closed
        self.weight = int(card_id)  # Ид карты соответвстует её весу

    def switch_position(self, coordinates):
        self.rect.x, self.rect.y = coordinates

    def get_weight(self):
        return self.weight

    def open(self):
        self.is_closed = False

    def close(self):
        self.is_closed = True

    def draw(self, screen_for_draw):
        if self.is_closed:
            screen_for_draw.blit(self.closed_image, self.rect)
        else:
            screen_for_draw.blit(self.opened_image, self.rect)
