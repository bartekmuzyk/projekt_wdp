import pygame

from fontsloader import Font
from sprite import MultiSprite, TextSprite, ColorSprite


# noinspection PyUnresolvedReferences
class Countdown(MultiSprite):
    def __init__(self, font: Font, screen_rect: pygame.Rect, *, z_index: int):
        self.contained_sprites = {
            "bg": ColorSprite((0, 0, 0), (screen_rect.w, screen_rect.h), 128, z_index=z_index),
            "countdown": TextSprite("3", font.super_huge, screen_rect, z_index=z_index)
        }
        self.contained_sprites["countdown"].rect.center = screen_rect.w // 2, screen_rect.h // 2
        self.contained_sprites["countdown"].real_text.synchronize_precise_coords()

    def set_count(self, count: int):
        self.contained_sprites["countdown"].update_text(str(count))

    def hide(self):
        self.contained_sprites["countdown"].update_text("")
        del self.contained_sprites["bg"]
