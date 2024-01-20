from typing import Literal, Generator

from element import Element
import globalsettings
import calc


class Player(Element):
    max_pos: (int, int)
    animation_counter: int
    animation_frame: int
    animation_frames: Generator[int, None, None]
    direction: Literal["D", "R", "L", "U"]

    def setup(self):
        screen_rect = self.screen.get_rect()
        self.max_pos = (screen_rect.w - self.rect.w, screen_rect.h - self.rect.h)
        self.animation_counter = 0
        self.animation_frame = 0
        self.animation_frames = calc.infinite_sequence([0, 1, 0, 2])
        self.direction = "D"

    def move(self, x: int, y: int):
        self.rect.x = calc.clamp(
            self.rect.x + (x * globalsettings.PLAYER_MOVE_SPEED),
            0, self.max_pos[0]
        )
        self.rect.y = calc.clamp(
            self.rect.y + (y * globalsettings.PLAYER_MOVE_SPEED),
            0, self.max_pos[1]
        )

    def reset_position(self):
        screen_rect = self.screen.get_rect()
        self.rect.center = screen_rect.w // 2, screen_rect.h // 2

    def animate(self):
        if self.animation_counter == 0:
            self.animation_frame = next(self.animation_frames)

        self.animation_counter = (self.animation_counter + 1) % globalsettings.PLAYER_ANIMATION_SPEED

    def reset_animation(self):
        self.animation_counter = 0
        self.animation_frame = 0
