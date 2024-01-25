import pygame

import globalsettings
from scene import Scene, SceneController
from sprites import CompleteBoard, Player, TrashCans, HUD, Countdown, WinScreen
from .utils import gameplay as utils


class GameplayScene(Scene):
    board: CompleteBoard
    player: Player
    trashcans: TrashCans
    hud: HUD
    countdown: Countdown
    count_start_tick: int
    block_movement: bool
    finish: bool
    remaining_seconds: int

    def start(self):
        self.board = CompleteBoard(self.assets["plansza"], self.screen_rect, z_index=(1, 4))
        self.sprites.append(self.board)
        self.player = Player(self.assets["kot"]["D0"], self.screen_rect, z_index=3)
        self.sprites.append(self.player)
        self.trashcans = TrashCans(self.assets["trashcan"], self.screen_rect, z_index=2)
        self.sprites.append(self.trashcans)
        self.hud = HUD(self.assets["ui"], self.fonts["PixCon"], self.screen_rect, z_index=5)
        self.sprites.append(self.hud)
        self.countdown = Countdown(self.fonts["PixCon"], self.screen_rect, z_index=6)
        self.sprites.append(self.countdown)
        self.count_start_tick = pygame.time.get_ticks()
        self.block_movement = True
        self.finish = False

    def do_finish(self, win_reason: str, remaining_seconds: int):
        self.block_movement = True
        self.finish = True
        self.remaining_seconds = remaining_seconds
        self.count_start_tick = pygame.time.get_ticks()
        win_screen = WinScreen(win_reason, self.fonts["PixCon"], self.screen_rect, z_index=6)
        self.sprites.append(win_screen)

    def update(self, controller: 'SceneController'):
        elapsed_seconds_since_start_tick = (pygame.time.get_ticks() - self.count_start_tick) // 1000

        if not self.block_movement:
            keys = pygame.key.get_pressed()
            board_move, self.player.direction = utils.calculate_board_movement(keys)
            player_move = [0, 0]

            if board_move[0] != 0 or board_move[1] != 0:
                self.player.animate()
            else:
                self.player.reset_animation()
            self.player.image = self.assets["kot"][f"{self.player.direction}{self.player.animation_frame}"]

            utils.redirect_board_movement_to_player(board_move, player_move, self.board, self.player, self.screen_rect)
            utils.apply_hitboxes_to_movement(board_move, player_move, self.board, self.player)
            self.board.move(*board_move)
            self.player.move(*player_move)
            self.trashcans.set_pos_all(self.board.bg.pos.x, self.board.bg.pos.y)

            trashcan_in_vicinity = self.trashcans.close_trashcan(self.player)
            if trashcan_in_vicinity is not None and not trashcan_in_vicinity.destroyed:
                self.hud.toggle_press_e_tip(True)
                if keys[pygame.K_e]:
                    self.trashcans.destroy_trashcan(trashcan_in_vicinity)
            else:
                self.hud.toggle_press_e_tip(False)

            self.hud.set_destroyed_trashcans_count(self.trashcans.destroyed_trashcans_count)
            remaining_seconds = globalsettings.GAMEPLAY_TIME - elapsed_seconds_since_start_tick

            self.hud.set_remaining_seconds(remaining_seconds)
            if remaining_seconds == 0:
                self.do_finish("Skończył Ci się czas!", remaining_seconds)
            elif self.trashcans.destroyed_trashcans_count == len(globalsettings.TRASHCAN_LOCATIONS):
                self.do_finish("Rozwalono wszystkie śmietniki!", remaining_seconds)
        elif not self.finish:
            self.hud.set_remaining_seconds(globalsettings.GAMEPLAY_TIME)
            if elapsed_seconds_since_start_tick == 3:
                self.block_movement = False
                self.count_start_tick = pygame.time.get_ticks()
                self.countdown.hide()
            else:
                self.countdown.set_count(3 - elapsed_seconds_since_start_tick)
        else:
            if elapsed_seconds_since_start_tick == 3:
                controller.context = {
                    "destroyed": self.trashcans.destroyed_trashcans_count,
                    "time_left": self.remaining_seconds
                }
                controller.switch("Score")
