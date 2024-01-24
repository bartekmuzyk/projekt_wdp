import pygame

import globalsettings
from sprite import MultiSprite
from sprites.trashcan import TrashCan


class TrashCans(MultiSprite):
    def __init__(self, trashcan_assets: dict[str, pygame.Surface], screen_rect: pygame.Rect, *, z_index: int):
        self.contained_sprites = {}

        for i, location in enumerate(globalsettings.TRASHCAN_LOCATIONS):
            trashcan = TrashCan(trashcan_assets["standing"], screen_rect, z_index=z_index)
            trashcan.id = i
            trashcan.offset = location
            self.contained_sprites[f"trashcan{i}"] = trashcan

    # noinspection PyUnresolvedReferences
    def set_pos_all(self, x: float, y: float):
        for trashcan in self.contained_sprites.values():
            trashcan.set_pos(x, y)
