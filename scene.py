from typing import Iterable, Type

import pygame

from assetsloader import AssetsCollection
from fontsloader import Font
from sprite import Sprite, MultiSprite, ColorSprite


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
    sprites: list[Sprite | MultiSprite | ColorSprite]
    fonts: dict[str, Font]

    def __init__(self, screen: pygame.Surface, assets: AssetsCollection, fonts: dict[str, Font], context):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.assets = assets
        self.fonts = fonts
        self.context = context
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
                 first_scene: str, scene_names: dict[str, Type[Scene]]):
        self._screen = screen
        self._assets = assets
        self._fonts = fonts
        self._scenes = scene_names
        self.context = {}
        self.switch(first_scene)

    def switch(self, scene_name: str):
        self.current_scene = self._scenes[scene_name](self._screen, self._assets, self._fonts, self.context)
        self.current_scene.start()

    def render(self):
        self.current_scene.update(self)
        self.current_scene.render()
