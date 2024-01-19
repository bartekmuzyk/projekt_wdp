import sys

import pygame

from board import Board
from sprites import load as load_sprites

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

sprites = load_sprites("assets")

board = Board(sprites["plansza"], screen)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))

    board.render()

    pygame.display.flip()
    clock.tick(60)
