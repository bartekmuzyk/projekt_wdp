import pygame

from assetsloader import Asset


class Element:
    def __init__(self, image: Asset, screen: pygame.Surface):
        self.image = image
        self.rect = self.image.rect
        self.screen = screen
        self.setup()

    def setup(self):
        pass

    def render(self):
        self.screen.blit(self.image.surface, self.rect)
