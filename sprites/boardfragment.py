import globalsettings
from calc import *
from sprite import Sprite


class BoardFragment(Sprite):
    max_pos: (int, int)

    def setup(self, screen_rect: pygame.Rect):
        self.max_pos = (-self.rect.w + screen_rect.w, -self.rect.h + screen_rect.h)
        self.rect.x, self.rect.y = -2722, -1340
        self.refresh_coords()

    def move(self, x: float, y: float):
        self.pos.x = clamp(
            self.pos.x - (x * globalsettings.PLAYER_MOVE_SPEED),
            self.max_pos[0], 0
        )
        self.pos.y = clamp(
            self.pos.y - (y * globalsettings.PLAYER_MOVE_SPEED),
            self.max_pos[1], 0
        )
