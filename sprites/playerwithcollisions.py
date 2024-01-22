import math

import pygame

import globalsettings
from sprite import MultiSprite
from sprites.player import Player
from sprites.playerhitpoint import PlayerHitpoint


# noinspection PyTypeChecker
class PlayerWithCollisions(MultiSprite):
    hitpoints_group: pygame.sprite.Group
    hitpoint_thickness: int

    def __init__(self, player_asset: pygame.Surface, screen_rect: pygame.Rect, *, z_index: int):
        player = Player(player_asset, screen_rect, z_index=z_index)
        hitpoint_length = player.rect.w
        self.hitpoint_thickness = math.ceil(globalsettings.PLAYER_MOVE_SPEED)
        self.contained_sprites = {
            "player": player,
            "u": PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "h", "u"),
            "r": PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "v", "r"),
            "d": PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "h", "d"),
            "l": PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "v", "l")
        }
        self.hitpoints_group = pygame.sprite.Group(self.contained_sprites["u"], self.contained_sprites["r"], self.contained_sprites["d"], self.contained_sprites["l"])

    @property
    def real_sprite(self) -> Player:
        return self.contained_sprites["player"]

    # noinspection PyUnresolvedReferences
    def move(self, x: int, y: int):
        player = self.contained_sprites["player"]
        player.move(x, y)
        self.contained_sprites["u"].rect.x, self.contained_sprites["u"].rect.y = player.rect.x, player.rect.y - self.hitpoint_thickness
        self.contained_sprites["r"].rect.x, self.contained_sprites["r"].rect.y = player.rect.x + player.rect.width, player.rect.y
        self.contained_sprites["d"].rect.x, self.contained_sprites["d"].rect.y = player.rect.x, player.rect.y + player.rect.height
        self.contained_sprites["l"].rect.x, self.contained_sprites["l"].rect.y = player.rect.x - self.hitpoint_thickness, player.rect.y
