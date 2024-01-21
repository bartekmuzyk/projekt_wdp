import pygame

from sprite import MultiSprite
from sprites import BoardFragment


class CompleteBoard(MultiSprite):
    def __init__(self, board_bg: (pygame.Surface, int), board_fg: (pygame.Surface, int), screen_rect: pygame.Rect):
        self.contained_sprites = {
            "bg": BoardFragment(board_bg[0], screen_rect, z_index=board_bg[1]),
            "fg": BoardFragment(board_fg[0], screen_rect, z_index=board_fg[1])
        }

    def move(self, x: float, y: float):
        self.contained_sprites["bg"].move(x, y)
        self.contained_sprites["fg"].move(x, y)

    @property
    def bg(self) -> BoardFragment:
        return self.contained_sprites["bg"]
