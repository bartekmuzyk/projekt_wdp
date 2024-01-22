from typing import Literal

import pygame


class PlayerHitpoint(pygame.sprite.Sprite):
    def __init__(self, length: int, thickness: int, direction: Literal["h", "v"], label: str):
        super().__init__()
        self.z_index = 0
        self.image = pygame.Surface([length, thickness] if direction == "h" else [thickness, length])
        pygame.draw.rect(self.image, (0, 255, 0), (0, 0, length if direction == "h" else thickness, length if direction == "v" else thickness))
        self.rect = self.image.get_rect()
        self.label = label
