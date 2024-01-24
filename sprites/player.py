from typing import Generator, Literal

import globalsettings
from calc import *
from sprite import Sprite


class Player(Sprite):
    max_pos: tuple[int, int]
    prev_pos: PreciseCoords
    animation_counter: int
    animation_frame: int
    animation_frames: Generator[int, None, None]
    direction: Literal["U", "D", "L", "R"]

    def setup(self, screen_rect: pygame.Rect):
        self.max_pos = (screen_rect.w - self.rect.w, screen_rect.h - self.rect.h)
        self.animation_counter = 0
        self.animation_frame = 0
        self.animation_frames = infinite_sequence([0, 1, 0, 2])
        self.direction = "D"

        self.rect.center = (screen_rect.w // 2, screen_rect.h // 2)
        self.synchronize_precise_coords()

    def move(self, x: int, y: int):
        self.pos.x = clamp(
            self.pos.x + (x * globalsettings.PLAYER_MOVE_SPEED),
            0, self.max_pos[0]
        )
        self.pos.y = clamp(
            self.pos.y + (y * globalsettings.PLAYER_MOVE_SPEED),
            0, self.max_pos[1]
        )

    def animate(self):
        if self.animation_counter == 0:
            self.animation_frame = next(self.animation_frames)

        self.animation_counter = (self.animation_counter + 1) % globalsettings.PLAYER_ANIMATION_SPEED

    def reset_animation(self):
        self.animation_counter = 0
        self.animation_frame = 0
