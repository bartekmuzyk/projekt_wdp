from typing import Type

import pygame

from assetsloader import AssetsCollection
from sprite import Sprite, MultiSprite


class Scene:
    sprites: list[Sprite | MultiSprite]

    def __init__(self, screen: pygame.Surface, assets: AssetsCollection):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.assets = assets
        self.sprites = []

    def start(self):
        pass

    def update(self, controller: 'SceneController'):
        return NotImplemented

    def render(self):
        sprites = []

        for sprite in self.sprites:
            if isinstance(sprite, MultiSprite):
                for sprite2 in sprite.contained_sprites.values():
                    sprites.append(sprite2)
                continue

            sprites.append(sprite)

        sprites = sorted(sprites, key=lambda v: v.z_index)

        for sprite in sprites:
            sprite.update()
            self.screen.blit(sprite.image, sprite.rect)


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
