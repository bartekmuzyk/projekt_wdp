import pygame.key

from elements import Board
from elements.player import Player
from scene import Scene, SceneController


class GameplayScene(Scene):
    board_bg: Board
    board_fg: Board
    player: Player
    screen_center: (int, int)

    def start(self):
        self.board_bg = Board(self.sprites["plansza_bg"], self.screen)
        self.board_fg = Board(self.sprites["plansza_fg"], self.screen)
        self.player = Player(self.sprites["kot"]["D0"], self.screen)
        self.player.reset_position()

        screen_rect = self.screen.get_rect()
        self.screen_center = (screen_rect.w // 2, screen_rect.h // 2)

    def render(self, controller: 'SceneController'):
        keys = pygame.key.get_pressed()
        board_move, player_move = [0, 0], [0, 0]

        if keys[pygame.K_a]:
            board_move[0] -= 1
            self.player.direction = "L"
        if keys[pygame.K_d]:
            board_move[0] += 1
            self.player.direction = "R"
        if keys[pygame.K_w]:
            board_move[1] -= 1
            self.player.direction = "U"
        if keys[pygame.K_s]:
            board_move[1] += 1
            self.player.direction = "D"

        if board_move[0] != 0 or board_move[1] != 0:
            if board_move[0] != 0 and board_move[1] != 0:
                board_move = [board_move[0] * 0.75, board_move[1] * 0.75]

            self.player.animate()
        else:
            self.player.reset_animation()

        self.player.sprite = self.sprites["kot"][f"{self.player.direction}{self.player.animation_frame}"]

        if (
                self.board_bg.rect.x == 0 and (board_move[0] < 0 or self.player.rect.centerx < self.screen_center[0])
        ) or (
                self.board_bg.rect.x == self.board_bg.max_pos[0] and (board_move[0] > 0 or self.player.rect.centerx > self.screen_center[0])
        ):
            player_move[0], board_move[0] = board_move[0], 0

        if (
                self.board_bg.rect.y == 0 and (board_move[1] < 0 or self.player.rect.centery < self.screen_center[1])
        ) or (
                self.board_bg.rect.y == self.board_bg.max_pos[1] and (board_move[1] > 0 or self.player.rect.centery > self.screen_center[1])
        ):
            player_move[1], board_move[1] = board_move[1], 0

        self.board_bg.move(*board_move)
        self.board_fg.move(*board_move)
        self.player.move(*player_move)

        self.board_bg.render()
        self.player.render()
        self.board_fg.render()
