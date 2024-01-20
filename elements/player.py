from element import Element
import globalsettings
import calc


class Player(Element):
    max_pos: (int, int)

    def setup(self):
        screen_rect = self.screen.get_rect()
        self.max_pos = (screen_rect.w - self.rect.w, screen_rect.h - self.rect.h)

    def move(self, x: int, y: int):
        self.rect.x = calc.clamp(
            self.rect.x - (x * globalsettings.PLAYER_MOVE_SPEED),
            0, self.max_pos[0]
        )
        self.rect.y = calc.clamp(
            self.rect.y - (y * globalsettings.PLAYER_MOVE_SPEED),
            0, self.max_pos[1]
        )

    def reset_position(self):
        screen_rect = self.screen.get_rect()
        self.rect.center = screen_rect.w // 2, screen_rect.h // 2
