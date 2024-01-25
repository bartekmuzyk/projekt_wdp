import pygame
from typing import Union

from calc import PreciseCoords


class Sprite(pygame.sprite.Sprite):
    pos: PreciseCoords
    rect: pygame.Rect

    def __init__(self, image: pygame.Surface, screen_rect: pygame.Rect, *, z_index: int = 0, mask: bool = False):
        super().__init__()
        self.image = image
        self.refresh_rect_based_on_image()
        if mask:
            self.mask = pygame.mask.from_surface(self.image)
        self.synchronize_precise_coords()
        self.z_index = z_index
        self.setup(screen_rect)

    def setup(self, screen_rect: pygame.Rect):
        pass

    def update(self):
        self.pos.apply_to_rect(self.rect)

    def synchronize_precise_coords(self):
        self.pos = PreciseCoords.from_rect(self.rect)

    def refresh_rect_based_on_image(self):
        self.rect = self.image.get_rect()


class MultiSprite:
    contained_sprites: dict[str, Union[Sprite, 'MultiSprite']]

    def pre_render_hook(self):
        pass


class TextSprite(MultiSprite):
    def __init__(self, text: str, font: pygame.font.Font, screen_rect: pygame.Rect, *, z_index: int = 0, color=None):
        self.font = font
        self.color = color
        self.screen_rect = screen_rect
        self.z_index = z_index
        self.contained_sprites = {
            "outline_u": Sprite(self._write_text(text, (0, 0, 0)), screen_rect, z_index=z_index),
            "outline_r": Sprite(self._write_text(text, (0, 0, 0)), screen_rect, z_index=z_index),
            "outline_d": Sprite(self._write_text(text, (0, 0, 0)), screen_rect, z_index=z_index),
            "outline_l": Sprite(self._write_text(text, (0, 0, 0)), screen_rect, z_index=z_index),
            "text": Sprite(self._write_text(text), screen_rect, z_index=z_index)
        }

    def pre_render_hook(self):
        text_pos = self.real_text.pos
        outline_thickness = 2
        self.contained_sprites["outline_u"].pos = PreciseCoords(text_pos.x, text_pos.y - outline_thickness)
        self.contained_sprites["outline_r"].pos = PreciseCoords(text_pos.x + outline_thickness, text_pos.y)
        self.contained_sprites["outline_d"].pos = PreciseCoords(text_pos.x, text_pos.y + outline_thickness)
        self.contained_sprites["outline_l"].pos = PreciseCoords(text_pos.x - outline_thickness, text_pos.y)

    def _write_text(self, text: str, override_color=None):
        color = override_color if override_color is not None else (
            self.color if self.color is not None else (255, 255, 255)
        )
        return self.font.render(text, False, color)

    def update_text(self, text: str):
        self.real_text.image = self._write_text(text)
        self.real_text.refresh_rect_based_on_image()

    @property
    def real_text(self) -> Sprite:
        return self.contained_sprites["text"]

    @property
    def pos(self) -> PreciseCoords:
        return self.real_text.pos

    @property
    def rect(self) -> pygame.Rect:
        return self.real_text.rect
