import pygame

from sprite import MultiSprite, Sprite, TextSprite
from fontsloader import Font


# noinspection PyUnresolvedReferences
class HUD(MultiSprite):
    under: int

    def __init__(self, ui_assets: dict[str, pygame.Surface], ui_font: Font, screen_rect: pygame.Rect, *,
                 z_index: int):
        self.contained_sprites = {
            "press_e_tip_key": Sprite(ui_assets["e_key"], screen_rect, z_index=z_index),
            "press_e_tip_text": TextSprite("Rozwal śmietnik", ui_font.normal, screen_rect, z_index=z_index),
            "trashcan_counter_bg": Sprite(ui_assets["trashcan_counter_bg"], screen_rect, z_index=z_index),
            "trashcan_counter_icon": Sprite(ui_assets["trashcan_counter_icon"], screen_rect, z_index=z_index),
            "trashcan_counter_label1": TextSprite("Rozwalone", ui_font.small, screen_rect, z_index=z_index),
            "trashcan_counter_label2": TextSprite("śmietniki", ui_font.small, screen_rect, z_index=z_index),
            "trashcan_counter_label3": TextSprite("0", ui_font.huge, screen_rect, z_index=z_index),
            "timer_icon": Sprite(ui_assets["timer"], screen_rect, z_index=z_index),
            "timer_text": TextSprite("0:30", ui_font.normal, screen_rect, z_index=z_index)
        }
        self.under = screen_rect.height + 1

        e_key_tip_gap = 10
        e_key_tip_width = (self.contained_sprites["press_e_tip_key"].rect.w +
                           self.contained_sprites["press_e_tip_text"].rect.w +
                           e_key_tip_gap)
        half_screen_width = screen_rect.width / 2
        self.contained_sprites["press_e_tip_key"].pos.x = half_screen_width - (e_key_tip_width / 2)
        self.contained_sprites["press_e_tip_text"].pos.x = (self.contained_sprites["press_e_tip_key"].pos.x +
                                                            self.contained_sprites["press_e_tip_key"].rect.w +
                                                            e_key_tip_gap)
        self.toggle_press_e_tip(False)

        self.contained_sprites["trashcan_counter_icon"].pos.x, self.contained_sprites["trashcan_counter_icon"].pos.y = 75, 50
        self.contained_sprites["trashcan_counter_label1"].pos.x, self.contained_sprites["trashcan_counter_label1"].pos.y = 20, 120
        self.contained_sprites["trashcan_counter_label2"].pos.x, self.contained_sprites["trashcan_counter_label2"].pos.y = 32, 155
        self.contained_sprites["trashcan_counter_label3"].pos.x, self.contained_sprites["trashcan_counter_label3"].pos.y = 200, 120

        self.contained_sprites["timer_icon"].pos.x, self.contained_sprites["timer_icon"].pos.y = screen_rect.w - 180, 10
        self.contained_sprites["timer_text"].pos.x, self.contained_sprites["timer_text"].pos.y = screen_rect.w - 120, 15

    def toggle_press_e_tip(self, visible: bool):
        self.contained_sprites["press_e_tip_key"].pos.y = self.contained_sprites["press_e_tip_text"].pos.y = \
            self.under - (100 if visible else 0)

    def set_destroyed_trashcans_count(self, count: int):
        self.contained_sprites["trashcan_counter_label3"].update_text(str(count))

    def set_remaining_seconds(self, seconds: int):
        self.contained_sprites["timer_text"].update_text(f"0:{seconds:02}")
