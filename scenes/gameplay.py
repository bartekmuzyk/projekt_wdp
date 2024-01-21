import pygame

import calc
from sprites import BoardFragment, Player
from scene import Scene, SceneController


class GameplayScene(Scene):
    board_bg: BoardFragment
    board_fg: BoardFragment
    player: Player

    def start(self):
        screen_rect = self.screen.get_rect()
        self.board_bg = BoardFragment(self.assets["plansza_bg"], screen_rect)
        self.sprites.add(self.board_bg)

        self.player = Player(self.assets["kot"]["D0"], screen_rect)
        self.sprites.add(self.player)

        self.board_fg = BoardFragment(self.assets["plansza_fg"], screen_rect)
        self.sprites.add(self.board_fg)
        self.move_board((1360, 660))

    def move_board(self, move: list[int] | tuple[int, int]):
        self.board_bg.move(*move)
        self.board_fg.move(*move)

    def update(self, controller: 'SceneController'):
        keys = pygame.key.get_pressed()
        board_move, self.player.direction = calc.movement(keys)
        player_move = [0, 0]

        if board_move[0] != 0 or board_move[1] != 0:
            self.player.animate()
        else:
            self.player.reset_animation()

        self.player.image = self.assets["kot"][f"{self.player.direction}{self.player.animation_frame}"]

        calc.redirect_board_movement_to_player(board_move, player_move, self.board_bg.rect, self.player.rect, self.screen_rect, self.board_bg.max_pos)
        self.move_board(board_move)
        self.player.move(*player_move)
