import pygame

from sprites import Sprite


BOARD_SCALE = 3
MOVE_SPEED = 5


class Board:
    _rect: pygame.Rect
    _max: (int, int)

    def __init__(self, sprite: Sprite, screen: pygame.Surface):
        self._sprite = sprite
        self._sprite.scale(self._sprite.rect.w * BOARD_SCALE, self._sprite.rect.h * BOARD_SCALE)
        self._rect = self._sprite.rect

        self._screen = screen
        screen_rect = self._screen.get_rect()
        self._max = (-self._rect.w + screen_rect.w, -self._rect.h + screen_rect.h)

    def move(self, x: int, y: int) -> (bool, bool):
        moved_x, moved_y = False, False

        target_x = self._rect.x - (x * MOVE_SPEED)
        if self._max[0] <= target_x <= 0:
            self._rect.x = target_x
            moved_x = True

        target_y = self._rect.y - (y * MOVE_SPEED)
        if self._max[1] <= target_y <= 0:
            self._rect.y = target_y
            moved_y = True

        return moved_x, moved_y

    def render(self):
        self._screen.blit(self._sprite.surface, self._rect)
