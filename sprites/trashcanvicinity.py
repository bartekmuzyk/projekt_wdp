import pygame

import globalsettings
from sprites.trashcan import TrashCan


class TrashCanVicinity(pygame.sprite.Sprite):
    def __init__(self, trashcan: TrashCan):
        super().__init__()
        self.z_index = 10
        size = globalsettings.TRASHCAN_VICINITY_SIZE
        self.image = pygame.Surface((size, size))
        pygame.draw.rect(self.image, (0, 255, 0), (0, 0, size, size))
        self.rect = self.image.get_rect()
        self.trashcan = trashcan

    def refresh_position(self):
        self.rect.center = self.trashcan.rect.center
