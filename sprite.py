from calc import *


class Sprite(pygame.sprite.Sprite):
    pos: PreciseCoords

    def __init__(self, image: pygame.Surface, screen_rect: pygame.Rect):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.refresh_coords()
        self.setup(screen_rect)

    def setup(self, screen_rect: pygame.Rect):
        pass

    def update(self):
        self.pos.apply_to_rect(self.rect)

    def refresh_coords(self):
        self.pos = PreciseCoords.from_rect(self.rect)
