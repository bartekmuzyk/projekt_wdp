import pygame

from element import Element
import globalsettings
import calc
from assetsloader import Asset


class Board(Element):
    max_pos: (int, int)
    fg: Asset
    hitbox: pygame.Mask

    def setup(self):
        screen_rect = self.screen.get_rect()
        self.max_pos = (-self.rect.w + screen_rect.w, -self.rect.h + screen_rect.h)

    def move(self, x: int, y: int):
        self.rect.x = calc.clamp(
            self.rect.x - (x * globalsettings.PLAYER_MOVE_SPEED),
            self.max_pos[0], 0
        )
        self.rect.y = calc.clamp(
            self.rect.y - (y * globalsettings.PLAYER_MOVE_SPEED),
            self.max_pos[1], 0
        )
