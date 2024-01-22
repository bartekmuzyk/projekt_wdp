from typing import Literal

import pygame


class PlayerHitpoint(pygame.sprite.Sprite):
    def __init__(self, length: int, direction: Literal["h", "v"], pos: (int, int)):
        super().__init__()
        self.image = pygame.Surface([length, 1] if direction == "h" else [1, length])
        pygame.draw.rect(self.image, (255, 0, 0), (0, 0, length if direction == "h" else 1, length if direction == "v" else 1))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
