import pygame

from scene import Scene, SceneController
from sprites import TrashCans
from .utils.gameplay import *


class GameplayScene(Scene):
    board: CompleteBoard
    player: Player
    trashcans: TrashCans

    def start(self):
        self.board = CompleteBoard(self.assets["plansza"], self.screen_rect, z_index=(1, 4))
        self.sprites.append(self.board)

        self.player = Player(self.assets["kot"]["D0"], self.screen_rect, z_index=3)
        self.sprites.append(self.player)

        self.trashcans = TrashCans(self.assets["trashcan"], self.screen_rect, z_index=2)
        self.sprites.append(self.trashcans)

    def update(self, controller: 'SceneController'):
        keys = pygame.key.get_pressed()
        board_move, self.player.direction = calculate_board_movement(keys)
        player_move = [0, 0]

        if board_move[0] != 0 or board_move[1] != 0:
            self.player.animate()
        else:
            self.player.reset_animation()

        self.player.image = self.assets["kot"][f"{self.player.direction}{self.player.animation_frame}"]

        redirect_board_movement_to_player(board_move, player_move, self.board, self.player, self.screen_rect)
        apply_hitboxes_to_movement(board_move, player_move, self.board, self.player)

        self.board.move(*board_move)
        self.player.move(*player_move)
        self.trashcans.set_pos_all(self.board.bg.pos.x, self.board.bg.pos.y)

        trashcan_in_vicinity = self.trashcans.close_trashcan(self.player)

        if trashcan_in_vicinity is not None and not trashcan_in_vicinity.destroyed:
            print(trashcan_in_vicinity.id)
            if keys[pygame.K_e]:
                self.trashcans.destroy_trashcan(trashcan_in_vicinity)
