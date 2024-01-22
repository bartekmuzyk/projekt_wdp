import pygame

from sprite import MultiSprite
from sprites import BoardFragment


class CompleteBoard(MultiSprite):
    def __init__(self, board_assets: dict[str, pygame.Surface], screen_rect: pygame.Rect, *, z_index: tuple[int, int]):
        self.contained_sprites = {
            "bg": BoardFragment(board_assets["bg"], screen_rect, z_index=z_index[0]),
            "fg": BoardFragment(board_assets["fg"], screen_rect, z_index=z_index[1])
        }

    def move(self, x: float, y: float):
        self.contained_sprites["bg"].move(x, y)
        self.contained_sprites["fg"].move(x, y)

    # noinspection PyTypeChecker
    @property
    def bg(self) -> BoardFragment:
        return self.contained_sprites["bg"]
