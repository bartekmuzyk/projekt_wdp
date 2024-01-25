import math
from typing import Generator, Literal

import globalsettings
from calc import *
from sprite import Sprite
from sprites.playerhitpoint import PlayerHitpoint


class Player(Sprite):
    max_pos: tuple[int, int]
    prev_pos: PreciseCoords
    animation_counter: int
    animation_frame: int
    animation_frames: Generator[int, None, None]
    direction: Literal["U", "D", "L", "R"]
    hitpoint_thickness: int
    hitpoint_u: PlayerHitpoint
    hitpoint_r: PlayerHitpoint
    hitpoint_d: PlayerHitpoint
    hitpoint_l: PlayerHitpoint
    hitpoints_group: pygame.sprite.Group

    def setup(self, screen_rect: pygame.Rect):
        self.max_pos = (screen_rect.w - self.rect.w, screen_rect.h - self.rect.h)
        self.animation_counter = 0
        self.animation_frame = 0
        self.animation_frames = infinite_sequence([0, 1, 0, 2])
        self.direction = "D"

        hitpoint_length = self.rect.w
        self.hitpoint_thickness = math.ceil(globalsettings.PLAYER_MOVE_SPEED)
        self.hitpoint_u = PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "h", "u")
        self.hitpoint_r = PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "v", "r")
        self.hitpoint_d = PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "h", "d")
        self.hitpoint_l = PlayerHitpoint(hitpoint_length, self.hitpoint_thickness, "v", "l")
        self.hitpoints_group = pygame.sprite.Group(self.hitpoint_u, self.hitpoint_r, self.hitpoint_d, self.hitpoint_l)

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
        self.hitpoint_u.rect.x, self.hitpoint_u.rect.y = self.rect.x, self.rect.y - self.hitpoint_thickness
        self.hitpoint_r.rect.x, self.hitpoint_r.rect.y = self.rect.x + self.rect.width, self.rect.y
        self.hitpoint_d.rect.x, self.hitpoint_d.rect.y = self.rect.x, self.rect.y + self.rect.height
        self.hitpoint_l.rect.x, self.hitpoint_l.rect.y = self.rect.x - self.hitpoint_thickness, self.rect.y

    def animate(self):
        if self.animation_counter == 0:
            self.animation_frame = next(self.animation_frames)

        self.animation_counter = (self.animation_counter + 1) % globalsettings.PLAYER_ANIMATION_SPEED

    def reset_animation(self):
        self.animation_counter = 0
        self.animation_frame = 0
