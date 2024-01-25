import pygame

from sprite import MultiSprite, Sprite, TextSprite


class HUD(MultiSprite):
    under: int

    def __init__(self, ui_assets: dict[str, pygame.Surface], ui_font: pygame.font.Font, screen_rect: pygame.Rect, *,
                 z_index: int):
        self.contained_sprites = {
            "press_e_tip_key": Sprite(ui_assets["e_key"], screen_rect, z_index=z_index),
            "press_e_tip_text": TextSprite("Rozwal śmietnik", ui_font, screen_rect, z_index=z_index)
        }
        self.under = screen_rect.height + 1

        e_key_tip_gap = 10
        # self.contained_sprites["press_e_tip_text"].real_text.synchronize_precise_coords()
        e_key_tip_width = (self.contained_sprites["press_e_tip_key"].rect.w +
                           self.contained_sprites["press_e_tip_text"].rect.w +
                           e_key_tip_gap)
        half_screen_width = screen_rect.width / 2
        self.contained_sprites["press_e_tip_key"].pos.x = half_screen_width - (e_key_tip_width / 2)
        self.contained_sprites["press_e_tip_text"].pos.x = (self.contained_sprites["press_e_tip_key"].pos.x +
                                                            self.contained_sprites["press_e_tip_key"].rect.w +
                                                            e_key_tip_gap)
        self.toggle_press_e_tip(False)

    def toggle_press_e_tip(self, visible: bool):
        self.contained_sprites["press_e_tip_key"].pos.y = self.contained_sprites["press_e_tip_text"].pos.y = \
                                                                                self.under - (100 if visible else 0)

