import json

import pygame


class Sprites:
    _sprites = {}

    def __init__(self, path_file_name: str):
        with open(path_file_name, "r") as path_file:
            paths = json.load(path_file)

        for name, meta in paths.items():
            sprite = pygame.image.load(meta["path"])
            sprite.convert()

            sprite_rect = sprite.get_rect()

            if "position" in meta:
                sprite_rect.x, sprite_rect.y = meta["position"]

            self._sprites[name] = sprite

    def get_sprite(self, name: str) -> pygame.Surface | pygame.SurfaceType:
        return self._sprites[name]

    def get_blit(self, name: str) -> (pygame.Surface | pygame.SurfaceType, pygame.Rect):
        sprite = self.get_sprite(name)

        return sprite, sprite.get_rect()
