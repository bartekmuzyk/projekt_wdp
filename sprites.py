import os

import pygame


class Sprite:
    surface: pygame.Surface

    def __init__(self, surface):
        self.surface = surface

    def scale(self, width, height):
        self.surface = pygame.transform.scale(self.surface, (width, height))

    @property
    def blit(self) -> (pygame.Surface, pygame.Rect):
        return self.surface, self.rect

    @property
    def rect(self) -> pygame.Rect:
        return self.surface.get_rect()


def _load_sprites_from_path(path, load_to):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        if ".png" in filename:
            surface = pygame.image.load(full_path)
            surface.convert()

            load_to[filename.replace(".png", "")] = Sprite(surface)
        else:
            load_to[filename] = {}
            _load_sprites_from_path(full_path, load_to[filename])


def load(directory: str) -> dict[str, Sprite | dict[str, Sprite]]:
    memory = {}
    _load_sprites_from_path(directory, memory)

    return memory
