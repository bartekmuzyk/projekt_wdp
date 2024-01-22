import pygame

from sprite import MultiSprite, Sprite
from sprites import Player, PlayerHitpoint


# noinspection PyTypeChecker
class PlayerWithCollisions(MultiSprite):
    def __init__(self, player_asset: pygame.Surface, screen_rect: pygame.Rect, *, z_index: int):
        hitpoint_size = 16
        self.contained_sprites = {
            "player": Player(player_asset, screen_rect, z_index=z_index),
            "u": PlayerHitpoint(hitpoint_size, "h", (0, 0)),
            "u": PlayerHitpoint(hitpoint_size, "h", (0, 0)),
            "u": PlayerHitpoint(hitpoint_size, "h", (0, 0)),
            "u": PlayerHitpoint(hitpoint_size, "h", (0, 0))
        }

    @property
    def real_sprite(self) -> Player:
        return self.contained_sprites["player"]

    # noinspection PyUnresolvedReferences
    def move(self, x: int, y: int):
        for sprite in self.contained_sprites.values():
            sprite.move(x, y)

    @property
    def hitpoints(self) -> tuple[Sprite, Sprite, Sprite, Sprite]:
        return self.contained_sprites["u"], self.contained_sprites["r"], self.contained_sprites["d"], self.contained_sprites["l"]
