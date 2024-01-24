from sprite import Sprite


class TrashCan(Sprite):
    id: int
    offset: tuple[int, int]

    def set_pos(self, x: float, y: float):
        self.pos.x, self.pos.y = x + self.offset[0], y + self.offset[1]
