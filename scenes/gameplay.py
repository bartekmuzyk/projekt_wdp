from scene import Scene, SceneController
from sprites import Player, CompleteBoard
from .utils.gameplay import *


class GameplayScene(Scene):
    board: CompleteBoard
    player: Player

    def start(self):
        self.board = CompleteBoard(self.assets["plansza"], self.screen_rect, z_index=(1, 3))
        self.sprites.append(self.board)

        self.player = Player(self.assets["kot"]["D0"], self.screen_rect, z_index=2)
        self.sprites.append(self.player)

    def update(self, controller: 'SceneController'):
        keys = pygame.key.get_pressed()
        board_move, self.player.direction = calculate_board_movement(keys)
        player_move = [0, 0]

        if board_move[0] != 0 or board_move[1] != 0:
            self.player.animate()
        else:
            self.player.reset_animation()

        self.player.image = self.assets["kot"][f"{self.player.direction}{self.player.animation_frame}"]

        redirect_board_movement_to_player(board_move, player_move, self.board.bg.rect, self.player.rect, self.screen_rect, self.board.bg.max_pos)
        self.board.move(*board_move)
        self.player.move(*player_move)
