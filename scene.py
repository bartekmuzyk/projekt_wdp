from typing import Type

import pygame

from assetsloader import AssetsCollection


class Scene:
    def __init__(self, screen: pygame.Surface, assets: AssetsCollection):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.assets = assets
        self.sprites = pygame.sprite.Group()

    def start(self):
        pass

    def update(self, controller: 'SceneController'):
        return NotImplemented

    def render(self):
        self.sprites.update()
        self.sprites.draw(self.screen)


class SceneController:
    current_scene: Scene

    def __init__(self, screen: pygame.Surface, assets: AssetsCollection, first_scene: Type[Scene]):
        self._screen = screen
        self._assets = assets
        self.switch(first_scene)

    def switch(self, scene: Type[Scene]):
        self.current_scene = scene(self._screen, self._assets)
        self.current_scene.start()

    def render(self):
        self.current_scene.update(self)
        self.current_scene.render()
