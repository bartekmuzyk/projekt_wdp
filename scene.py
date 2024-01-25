from typing import Type, Iterable

import pygame

from assetsloader import AssetsCollection
from sprite import Sprite, MultiSprite


def unpack_sprites(sprites: Iterable[Sprite | MultiSprite]) -> list[Sprite]:
    r = []

    for sprite in sprites:
        if isinstance(sprite, MultiSprite):
            sprite.pre_render_hook()
            for sprite2 in unpack_sprites(sprite.contained_sprites.values()):
                r.append(sprite2)
        else:
            r.append(sprite)

    return r


class Scene:
    sprites: list[Sprite | MultiSprite]
    fonts: dict[str, pygame.font.Font]

    def __init__(self, screen: pygame.Surface, assets: AssetsCollection, fonts: dict[str, pygame.font.Font]):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.assets = assets
        self.fonts = fonts
        self.sprites = []

    def start(self):
        pass

    def update(self, controller: 'SceneController'):
        return NotImplemented

    def render(self):
        sprites = sorted(unpack_sprites(self.sprites), key=lambda v: v.z_index)

        for sprite in sprites:
            sprite.update()
            self.screen.blit(sprite.image, sprite.rect)


class SceneController:
    current_scene: Scene

    def __init__(self, screen: pygame.Surface, assets: AssetsCollection, fonts: dict[str, pygame.font.Font],
                 first_scene: Type[Scene]):
        self._screen = screen
        self._assets = assets
        self._fonts = fonts
        self.switch(first_scene)

    def switch(self, scene: Type[Scene]):
        self.current_scene = scene(self._screen, self._assets, self._fonts)
        self.current_scene.start()

    def render(self):
        self.current_scene.update(self)
        self.current_scene.render()
