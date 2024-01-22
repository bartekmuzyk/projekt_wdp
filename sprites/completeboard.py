import pygame

from sprite import MultiSprite
from sprites import BoardFragment


# noinspection PyUnresolvedReferences
class CompleteBoard(MultiSprite):
    def __init__(self, board_assets: dict[str, pygame.Surface], screen_rect: pygame.Rect, *, z_index: tuple[int, int]):
        self.contained_sprites = {
            "bg": BoardFragment(board_assets["bg"], screen_rect, z_index=z_index[0]),
            "fg": BoardFragment(board_assets["fg"], screen_rect, z_index=z_index[1]),
            "hitbox": BoardFragment(board_assets["hitbox"], screen_rect, mask=True)
        }

    def move(self, x: float, y: float):
        for sprite in self.contained_sprites.values():
            sprite.move(x, y)

    # noinspection PyTypeChecker
    @property
    def bg(self) -> BoardFragment:
        return self.contained_sprites["bg"]

    def player_collides_with_hitbox(self, player):
        return len(pygame.sprite.spritecollide(
            self.contained_sprites["hitbox"],
            pygame.sprite.Group(player.hitpoints),
            False,
            collided=pygame.sprite.collide_mask)
        ) > 0
