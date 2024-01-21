import pygame

from assetsloader import Asset


class Element(pygame.sprite.Sprite):
    def __init__(self, image: Asset, screen: pygame.Surface):
        super().__init__()
        self.image = image.surface
        self.rect = image.rect
        self.screen = screen
        self.setup()

    def setup(self):
        pass

    def render(self):
        self.screen.blit(self.image.surface, self.rect)
