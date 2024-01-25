import sys

import pygame

from scene import SceneController
import scenes
import assetsloader
import fontsloader

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

assets = assetsloader.load("assets")
fonts = fontsloader.load("fonts")

first_scene = scenes.GameplayScene
scene_controller = SceneController(screen, assets, fonts, first_scene)


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    scene_controller.render()

    pygame.display.flip()
    clock.tick(75)
