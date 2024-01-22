from scene import Scene, SceneController
from .utils.gameplay import *


class GameplayScene(Scene):
    board: CompleteBoard
    player: PlayerWithCollisions

    def start(self):
        self.board = CompleteBoard(self.assets["plansza"], self.screen_rect, z_index=(1, 3))
        self.sprites.append(self.board)

        self.player = PlayerWithCollisions(self.assets["kot"]["D0"], self.screen_rect, z_index=2)
        self.sprites.append(self.player)

    def update(self, controller: 'SceneController'):
        keys = pygame.key.get_pressed()
        board_move, self.player.real_sprite.direction = calculate_board_movement(keys)
        player_move = [0, 0]

        if board_move[0] != 0 or board_move[1] != 0:
            self.player.real_sprite.animate()
        else:
            self.player.real_sprite.reset_animation()

        self.player.real_sprite.image = self.assets["kot"][f"{self.player.real_sprite.direction}{self.player.real_sprite.animation_frame}"]

        redirect_board_movement_to_player(board_move, player_move, self.board, self.player, self.screen_rect)
        apply_hitboxes_to_movement(board_move, player_move, self.board, self.player)

        self.board.move(*board_move)
        self.player.move(*player_move)
