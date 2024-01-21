from calc import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, screen_rect: pygame.Rect):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = PreciseCoords.from_rect(self.rect)
        self.setup(screen_rect)

    def setup(self, screen_rect: pygame.Rect):
        pass
