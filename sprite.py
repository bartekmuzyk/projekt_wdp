from calc import *


class Sprite(pygame.sprite.Sprite):
    pos: PreciseCoords

    def __init__(self, image: pygame.Surface, screen_rect: pygame.Rect, *, z_index: int = 0, mask: bool = False):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        if mask:
            self.mask = pygame.mask.from_surface(self.image)
        self.refresh_coords()
        self.z_index = z_index
        self.setup(screen_rect)

    def setup(self, screen_rect: pygame.Rect):
        pass

    def update(self):
        self.pos.apply_to_rect(self.rect)

    def refresh_coords(self):
        self.pos = PreciseCoords.from_rect(self.rect)


class MultiSprite:
    contained_sprites: dict[str, Sprite]
