import easygui
import pygame

from calc import PreciseCoords
from scene import Scene, SceneController
from scoreboard import Scoreboard
from sprite import ColorSprite, TextSprite, Sprite, MultiSprite
from sprites import Button


class ScoreScene(Scene):
    bg: ColorSprite
    title: TextSprite
    sprites_to_show: list[Sprite | TextSprite | MultiSprite]
    quit_btn: Button
    save_points_btn: Button
    try_again_btn: Button
    start_tick: int
    last_elapsed: int
    points_earned: int
    buttons_displayed: bool
    points_saved: bool
    scoreboard: Scoreboard

    def start(self):
        self.scoreboard = Scoreboard()
        self.bg = ColorSprite((41, 182, 246), (self.screen_rect.w, self.screen_rect.h))
        self.sprites.append(self.bg)
        self.title = TextSprite("Podsumowanie", self.fonts["PixCon"].huge, self.screen_rect)
        self.title.pos.x = 15
        self.sprites.append(self.title)
        self.points_earned = self.context["destroyed"] + self.context["time_left"]
        self.points_saved = False
        self.start_tick = pygame.time.get_ticks()
        self.last_elapsed = 0
        self.sprites_to_show = []
        self.buttons_displayed = False
        trashcan_icon = Sprite(self.assets["trashcan"]["standing"], self.screen_rect)
        trashcan_icon.pos = PreciseCoords(15, 80)
        self.sprites_to_show.append(trashcan_icon)
        trashcans_text = TextSprite(f"Rozwalone śmietniki: {self.context["destroyed"]}", self.fonts["PixCon"].normal, self.screen_rect)
        trashcans_text.real_text.pos = PreciseCoords(75, 85)
        self.sprites_to_show.append(trashcans_text)
        timer_icon = Sprite(self.assets["ui"]["timer"], self.screen_rect)
        timer_icon.pos = PreciseCoords(22, 150)
        self.sprites_to_show.append(timer_icon)
        time_text = TextSprite(f"Pozostały czas: {self.context["time_left"]} sekund", self.fonts["PixCon"].normal, self.screen_rect)
        time_text.real_text.pos = PreciseCoords(75, 155)
        self.sprites_to_show.append(time_text)
        final_points_label = TextSprite(f"Ostateczny wynik:", self.fonts["PixCon"].normal, self.screen_rect)
        final_points_label.real_text.pos = PreciseCoords(self.screen_rect.w - final_points_label.rect.w - 15, 0)
        self.sprites_to_show.append(final_points_label)
        final_points_text = TextSprite(f"{self.points_earned}", self.fonts["PixCon"].super_huge, self.screen_rect)
        final_points_text.real_text.pos = PreciseCoords(self.screen_rect.w - final_points_text.rect.w - 15, 0)
        self.sprites_to_show.append(final_points_text)

    def update(self, controller: 'SceneController'):
        if len(self.sprites_to_show) > 0:
            elapsed = (pygame.time.get_ticks() - self.start_tick) // 500

            if elapsed != self.last_elapsed:
                sprite_to_show = self.sprites_to_show.pop(0)
                self.sprites.append(sprite_to_show)

            self.last_elapsed = elapsed
            return

        if not self.buttons_displayed:
            self.quit_btn = Button(self.assets["ui"]["button"], "Wyjdź do menu", self.fonts["PixCon"].normal, self.screen_rect)
            self.quit_btn.set_pos(self.screen_rect.w - self.quit_btn.rect.w - 15, self.screen_rect.h - self.quit_btn.rect.h - 15)
            self.sprites.append(self.quit_btn)
            self.save_points_btn = Button(self.assets["ui"]["button"], "Zapisz swój wynik", self.fonts["PixCon"].normal, self.screen_rect)
            self.save_points_btn.set_pos(self.screen_rect.w - self.save_points_btn.rect.w - 15, self.screen_rect.h - self.save_points_btn.rect.h - self.quit_btn.rect.h - 30)
            self.sprites.append(self.save_points_btn)
            self.try_again_btn = Button(self.assets["ui"]["button"], "Zagraj jeszcze raz", self.fonts["PixCon"].normal, self.screen_rect)
            self.try_again_btn.set_pos(15, self.screen_rect.h - self.save_points_btn.rect.h - 15)
            self.sprites.append(self.try_again_btn)

            self.buttons_displayed = True

        if self.save_points_btn.clicked and not self.points_saved:
            name = easygui.enterbox("Wpisz swoje imię", "Zapisywanie wyniku", strip=True)
            if name:
                while len(name) > 15:
                    name = easygui.enterbox("Imię nie może być dłuższe niż 15 znaków!", "Zapisywanie wyniku", strip=True)
                self.scoreboard.scores[name] = self.points_earned
                self.scoreboard.save()
                self.save_points_btn.update_text("Zapisano wynik!")
                self.points_saved = True
        elif self.quit_btn.clicked:
            controller.switch("Menu")
        elif self.try_again_btn.clicked:
            controller.switch("Gameplay")
