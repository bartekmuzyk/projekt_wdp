import pygame

from fontsloader import Font
from sprite import MultiSprite, TextSprite, ColorSprite


# noinspection PyUnresolvedReferences
class WinScreen(MultiSprite):
    def __init__(self, win_reason: str, font: Font, screen_rect: pygame.Rect, *, z_index: int):
        self.contained_sprites = {
            "bg": ColorSprite((0, 0, 0), (screen_rect.w, screen_rect.h), 180, z_index=z_index),
            "label1": TextSprite("Koniec gry!", font.super_huge, screen_rect, z_index=z_index),
            "label2": TextSprite(win_reason, font.huge, screen_rect, z_index=z_index)
        }
        self.contained_sprites["label1"].rect.center = screen_rect.w // 2, screen_rect.h // 2
        self.contained_sprites["label1"].real_text.synchronize_precise_coords()
        self.contained_sprites["label2"].rect.centerx = self.contained_sprites["label1"].rect.centerx
        self.contained_sprites["label2"].rect.y = \
            self.contained_sprites["label1"].rect.y + self.contained_sprites["label1"].rect.height + 20
        self.contained_sprites["label2"].real_text.synchronize_precise_coords()
