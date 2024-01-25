import pygame

import globalsettings
from sprite import MultiSprite
from sprites.trashcan import TrashCan
from sprites.player import Player
from sprites.trashcanvicinity import TrashCanVicinity


# noinspection PyTypeChecker,PyUnresolvedReferences
class TrashCans(MultiSprite):
    fallen_trashcan_asset: pygame.Surface

    def __init__(self, trashcan_assets: dict[str, pygame.Surface], screen_rect: pygame.Rect, *, z_index: int):
        self.contained_sprites = {}
        self.vicinities = pygame.sprite.Group()
        self.fallen_trashcan_asset = trashcan_assets["fallen"]

        for i, location in enumerate(globalsettings.TRASHCAN_LOCATIONS):
            trashcan = TrashCan(trashcan_assets["standing"], screen_rect, z_index=z_index)
            trashcan.offset = location
            vicinity = TrashCanVicinity(trashcan)
            self.contained_sprites[f"trashcan{i}"] = trashcan
            self.vicinities.add(vicinity)

    def set_pos_all(self, x: float, y: float):
        for trashcan in self.contained_sprites.values():
            trashcan.set_pos(x, y)

        for vicinity in self.vicinities:
            vicinity.refresh_position()

    def close_trashcan(self, player: Player) -> TrashCan | None:
        collisions = pygame.sprite.spritecollide(player, self.vicinities, False)

        return collisions[0].trashcan if len(collisions) > 0 else None

    def destroy_trashcan(self, trashcan: TrashCan):
        if trashcan.destroyed:
            return

        trashcan.destroyed = True
        trashcan.image = self.fallen_trashcan_asset
