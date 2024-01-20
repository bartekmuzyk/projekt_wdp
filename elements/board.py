from element import Element
import globalsettings
import calc


class Board(Element):
    max_pos: (int, int)

    def setup(self):
        screen_rect = self.screen.get_rect()
        self.max_pos = (-self.sprite.rect.w + screen_rect.w, -self.sprite.rect.h + screen_rect.h)

    def move(self, x: int, y: int):
        self.rect.x = calc.clamp(
            self.rect.x - (x * globalsettings.PLAYER_MOVE_SPEED),
            self.max_pos[0], 0
        )
        self.rect.y = calc.clamp(
            self.rect.y - (y * globalsettings.PLAYER_MOVE_SPEED),
            self.max_pos[1], 0
        )
