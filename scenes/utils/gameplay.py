import pygame

from sprites import PlayerWithCollisions, CompleteBoard


def calculate_board_movement(keys: pygame.key.ScancodeWrapper) -> tuple[list[int], str]:
    move = [0, 0]
    direction = "D"
    if keys[pygame.K_a]:
        move[0], direction = -1, "L"
    if keys[pygame.K_d]:
        move[0], direction = 1, "R"
    if keys[pygame.K_w]:
        move[1], direction = -1, "U"
    if keys[pygame.K_s]:
        move[1], direction = 1, "D"

    if move[0] != 0 and move[1] != 0:
        move = [move[0] * 0.75, move[1] * 0.75]

    return move, direction


def redirect_board_movement_to_player(board_move: list[int], player_move: list[int],
                                      board: CompleteBoard, player: PlayerWithCollisions, screen_rect: pygame.Rect):
    if (
        board.bg.rect.x == 0 and (
            board_move[0] < 0 or player.real_sprite.rect.centerx < screen_rect.centerx
        )
    ) or (
        board.bg.rect.x == board.bg.max_pos[0] and (
            board_move[0] > 0 or player.real_sprite.rect.centerx > screen_rect.centerx
        )
    ):
        player_move[0], board_move[0] = board_move[0], 0
    if (
        board.bg.rect.y == 0 and (
            board_move[1] < 0 or player.real_sprite.rect.centery < screen_rect.centery
        )
    ) or (
        board.bg.rect.y == board.bg.max_pos[1] and (
            board_move[1] > 0 or player.real_sprite.rect.centery > screen_rect.centery
        )
    ):
        player_move[1], board_move[1] = board_move[1], 0
