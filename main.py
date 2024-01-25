import sys

import pygame

from scene import SceneController
import assetsloader
import fontsloader
from scenes import GameplayScene, MenuScene, ScoreScene

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

assets = assetsloader.load("assets")
fonts = fontsloader.load("fonts")

scene_names = {
    "Gameplay": GameplayScene,
    "Menu": MenuScene,
    "Score": ScoreScene
}
first_scene = "Menu"
scene_controller = SceneController(screen, assets, fonts, first_scene, scene_names)


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
