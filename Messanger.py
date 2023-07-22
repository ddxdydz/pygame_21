import pygame

from local import FPS


class Messanger:
    background_screen_color = pygame.Color(20, 20, 20, 200)
    message_color = (235, 235, 235, 255)
    message_font_size = 90
    annotation_color = (200, 200, 200, 180)
    annotation_font_size = 20
    annotation_text = "Для продолжения нажмите любую кнопку..."

    def __init__(self):
        self.message_font = pygame.font.Font(None, Messanger.message_font_size)
        self.annotation_font = pygame.font.Font(None, Messanger.annotation_font_size)

    def draw_annotation(self, screen_for_draw):
        text = self.annotation_font.render(
            Messanger.annotation_text, True, Messanger.annotation_color)
        width, height = text.get_size()
        x = (screen_for_draw.get_width() - width) // 2
        y = (screen_for_draw.get_height() - height - 80)
        screen_for_draw.blit(text, (x, y))

    def draw_messange(self, message, screen_for_draw):
        message_screen = pygame.Surface(screen_for_draw.get_size()).convert_alpha()
        message_screen.fill(Messanger.background_screen_color)
        screen_for_draw.blit(message_screen, (0, 0))

        # Вывод сообщения:
        text = self.message_font.render(message, True, Messanger.message_color)
        width, height = text.get_size()
        x = (screen_for_draw.get_width() - width) // 2
        y = (screen_for_draw.get_height() - height) // 2
        screen_for_draw.blit(text, (x, y))

        # Вывод пояснения:
        self.draw_annotation(screen_for_draw)

    @staticmethod
    def enable_loop():
        running = True
        clock = pygame.time.Clock()
        while running:
            events = pygame.event.get().copy()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    running = False
            clock.tick(FPS)
            pygame.display.flip()

    def show_message(self, message, screen_for_draw):
        self.draw_messange(message, screen_for_draw)
        self.enable_loop()




