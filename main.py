import sys

import pygame

from sprites import Sprites

pygame.init()
screen = pygame.display.set_mode((1024, 720))

sprites = Sprites(path_file_name="sprites.json")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    screen.blit(*sprites.get_blit("board"))

    pygame.display.flip()
