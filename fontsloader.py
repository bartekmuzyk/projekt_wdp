import os

import pygame

import globalsettings


class Font:
    super_huge: pygame.font.Font
    huge: pygame.font.Font
    normal: pygame.font.Font
    small: pygame.font.Font


def load(directory: str) -> dict[str, Font]:
    f = {}

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        font = Font()
        font.super_huge = pygame.font.Font(full_path, globalsettings.UI_FONT_SIZE_SUPERHUGE)
        font.huge = pygame.font.Font(full_path, globalsettings.UI_FONT_SIZE_HUGE)
        font.normal = pygame.font.Font(full_path, globalsettings.UI_FONT_SIZE_NORMAL)
        font.small = pygame.font.Font(full_path, globalsettings.UI_FONT_SIZE_SMALL)
        f[filename.replace(".ttf", "")] = font

    return f
