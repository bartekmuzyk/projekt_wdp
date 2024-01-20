import pygame.key

from elements import Board
from elements.player import Player
from scene import Scene, SceneController


class GameplayScene(Scene):
    board: Board
    player: Player
    screen_center: (int, int)

    def start(self):
        self.board = Board(self.sprites["plansza"], self.screen)
        self.player = Player(self.sprites["kot"]["D0"], self.screen)
        self.player.reset_position()

        screen_rect = self.screen.get_rect()
        self.screen_center = (screen_rect.w // 2, screen_rect.h // 2)

    def render(self, controller: 'SceneController'):
        keys = pygame.key.get_pressed()
        board_move, player_move = [0, 0], [0, 0]

        if keys[pygame.K_w]:
            board_move[1] -= 1
        if keys[pygame.K_s]:
            board_move[1] += 1
        if keys[pygame.K_a]:
            board_move[0] -= 1
        if keys[pygame.K_d]:
            board_move[0] += 1

        if board_move[0] != 0 and board_move[1] != 0:
            board_move = [board_move[0] * 0.75, board_move[1] * 0.75]

        if self.board.rect.x == 0:
            if board_move[0] < 0 or self.player.rect.centerx < self.screen_center[0]:
                player_move[0], board_move[0] = -board_move[0], 0
        elif self.board.rect.x == self.board.max_pos[0]:
            if board_move[0] > 0 or self.player.rect.centerx > self.screen_center[0]:
                player_move[0], board_move[0] = -board_move[0], 0

        if self.board.rect.y == 0:
            if board_move[1] < 0 or self.player.rect.centery < self.screen_center[1]:
                player_move[1], board_move[1] = -board_move[1], 0
        elif self.board.rect.y == self.board.max_pos[1]:
            if board_move[1] > 0 or self.player.rect.centery > self.screen_center[1]:
                player_move[1], board_move[1] = -board_move[1], 0

        self.board.move(*board_move)
        self.player.move(*player_move)

        self.board.render()
        self.player.render()
