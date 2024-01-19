import sys

import pygame

from sprites import load as load_sprites

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

sprites = load_sprites("assets")

board_scale = 3
board_width, board_height = sprites["plansza"].rect.w, sprites["plansza"].rect.h
sprites["plansza"].scale(board_width * board_scale, board_height * board_scale)

board_x, board_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    screen.blit(sprites["plansza"].surface)
    board_x += 1
    board_y += 1

    pygame.display.flip()
