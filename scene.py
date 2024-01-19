from typing import Type

import pygame

from sprites import SpritesCollection


class Scene:
    def __init__(self, screen: pygame.Surface, sprites: SpritesCollection):
        self.screen = screen
        self.sprites = sprites

    def start(self):
        pass

    def render(self, controller: 'SceneController'):
        return NotImplemented


class SceneController:
    current_scene: Scene

    def __init__(self, screen: pygame.Surface, sprites: SpritesCollection, first_scene: Type[Scene]):
        self._screen = screen
        self._sprites = sprites
        self.switch(first_scene)

    def switch(self, scene: Type[Scene]):
        self.current_scene = scene(self._screen, self._sprites)
        self.current_scene.start()

    def render(self):
        self.current_scene.render(self)
