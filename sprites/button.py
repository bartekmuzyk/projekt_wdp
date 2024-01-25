import pygame.font

from calc import PreciseCoords
from sprite import MultiSprite, Sprite, TextSprite


# noinspection PyUnresolvedReferences
class Button(MultiSprite):
    def __init__(self, bg: pygame.Surface, text: str, font: pygame.font.Font, screen_rect: pygame.Rect, *,
                 z_index: int = 0):
        self.contained_sprites = {
            "bg": Sprite(bg, screen_rect, z_index=z_index),
            "text": TextSprite(text, font, screen_rect, z_index=z_index + 1)
        }
        self.contained_sprites["text"].real_text.rect.center = self.contained_sprites["bg"].rect.center
        self.contained_sprites["text"].real_text.synchronize_precise_coords()

    def set_pos(self, x: float, y: float):
        self.contained_sprites["bg"].pos = PreciseCoords(x, y)
        self.contained_sprites["bg"].update()
        self.contained_sprites["text"].real_text.rect.center = self.contained_sprites["bg"].rect.center
        self.contained_sprites["text"].real_text.synchronize_precise_coords()

    def update_text(self, text: str):
        self.contained_sprites["text"].update_text(text)
        self.contained_sprites["text"].real_text.rect.center = self.contained_sprites["bg"].rect.center
        self.contained_sprites["text"].real_text.synchronize_precise_coords()

    @property
    def rect(self) -> pygame.Rect:
        return self.contained_sprites["bg"].rect

    @property
    def clicked(self) -> bool:
        mouse_rect = pygame.Rect(pygame.mouse.get_pos(), (1, 1))

        return pygame.mouse.get_pressed()[0] and (
                self.rect.colliderect(mouse_rect) or self.contained_sprites["text"].rect.colliderect(mouse_rect)
        )
