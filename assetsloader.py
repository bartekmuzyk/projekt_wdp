import os
import json

import pygame


class Asset:
    surface: pygame.Surface

    def __init__(self, surface):
        self.surface = surface

    @property
    def blit(self) -> (pygame.Surface, pygame.Rect):
        return self.surface, self.rect

    @property
    def rect(self) -> pygame.Rect:
        return self.surface.get_rect()


def _load_assets_from_path(path, load_to):
    meta_file_path = os.path.join(path, "meta.json")
    meta: dict | None = None
    if os.path.isfile(meta_file_path):
        with open(meta_file_path, "r") as meta_file:
            meta = json.load(meta_file)

    for filename in os.listdir(path):
        if filename == "meta.json":
            continue

        full_path = os.path.join(path, filename)

        if ".png" in filename:
            surface = pygame.image.load(full_path).convert_alpha()
            rect = surface.get_rect()

            if meta is not None and "scale" in meta:
                surface = pygame.transform.scale(surface, (rect.width * meta["scale"], rect.height * meta["scale"]))

            load_to[filename.replace(".png", "")] = Asset(surface)
        else:
            load_to[filename] = {}
            _load_assets_from_path(full_path, load_to[filename])


AssetsCollection = dict[str, Asset | dict[str, Asset]]


def load(directory: str) -> AssetsCollection:
    memory = {}
    _load_assets_from_path(directory, memory)

    return memory