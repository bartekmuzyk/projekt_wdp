import os

import pygame

import globalsettings


def load(directory: str) -> dict[str, pygame.font.Font]:
    f = {}

    for filename in os.listdir(directory):
        f[filename.replace(".ttf", "")] = pygame.font.Font(
            os.path.join(directory, filename),
            globalsettings.UI_FONT_SIZE
        )

    return f
