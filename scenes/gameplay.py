from scene import Scene, SceneController
from sprites import CompleteBoard, PlayerWithCollisions
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
        board_move, self.player.direction = calculate_board_movement(keys)
        player_move = [0, 0]

        if board_move[0] != 0 or board_move[1] != 0:
            self.player.real_sprite.animate()
        else:
            self.player.real_sprite.reset_animation()

        self.player.image = self.assets["kot"][f"{self.player.real_sprite.direction}{self.player.real_sprite.animation_frame}"]

        redirect_board_movement_to_player(board_move, player_move, self.board, self.player, self.screen_rect)
        self.board.move(*board_move)
        self.player.move(*player_move)

        if self.board.player_collides_with_hitbox(self.player):
            board_back_move, player_back_move = [0, 0], [0, 0]
            if board_move[0] != 0 or player_move[0] != 0:
                board_back_move[0], player_back_move[0] = -board_move[0], -player_move[0]

            print(board_back_move, player_back_move)
            self.board.move(*board_back_move)
            self.player.move(*player_back_move)


