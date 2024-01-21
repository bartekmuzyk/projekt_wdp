from typing import Type

import pygame

from assetsloader import AssetsCollection


class Scene:
    def __init__(self, screen: pygame.Surface, assets: AssetsCollection):
        self.screen = screen
        self.assets = assets

    def start(self):
        pass

    def render(self, controller: 'SceneController'):
        return NotImplemented


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
        self.current_scene.render(self)
