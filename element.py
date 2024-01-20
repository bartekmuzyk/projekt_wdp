import pygame

from sprites import Sprite


class Element:
    def __init__(self, sprite: Sprite, screen: pygame.Surface):
        self.sprite = sprite
        self.rect = self.sprite.rect
        self.screen = screen
        self.setup()

    def setup(self):
        pass

    def render(self):
        self.screen.blit(self.sprite.surface, self.rect)
