from scene import Scene, SceneController
from scoreboard import Scoreboard
from sprite import ColorSprite, TextSprite
from sprites import CompleteBoard, Button


class MenuScene(Scene):
    bg1: CompleteBoard
    bg2: ColorSprite
    scoreboard_label: TextSprite
    start_btn: Button
    scoreboard: Scoreboard

    def start(self):
        self.scoreboard = Scoreboard()
        self.bg1 = CompleteBoard(self.assets["plansza"], self.screen_rect, z_index=(2, 3))
        self.sprites.append(self.bg1)
        self.bg2 = ColorSprite((41, 182, 246), (self.screen_rect.w, self.screen_rect.h), 160, z_index=4)
        self.sprites.append(self.bg2)
        self.scoreboard_label = TextSprite("Najlepsze wyniki", self.fonts["PixCon"].huge, self.screen_rect, z_index=5)
        self.scoreboard_label.pos.x, self.scoreboard_label.pos.y = self.screen_rect.w - self.scoreboard_label.rect.w - 15, 0
        self.sprites.append(self.scoreboard_label)
        self.start_btn = Button(self.assets["ui"]["button"], "Rozpocznij grę", self.fonts["PixCon"].normal, self.screen_rect, z_index=5)
        self.start_btn.set_pos(15, self.screen_rect.h - self.start_btn.rect.h - 15)
        self.sprites.append(self.start_btn)

        for i, (name, score) in enumerate(self.scoreboard.scores.items()):
            if i == 10:
                break

            name_text = TextSprite(name, self.fonts["PixCon"].normal, self.screen_rect, z_index=5)
            name_text.pos.x = self.scoreboard_label.pos.x
            score_text = TextSprite(str(score), self.fonts["PixCon"].normal, self.screen_rect, z_index=5)
            score_text.pos.x = self.screen_rect.w - score_text.rect.w - 15
            name_text.pos.y = score_text.pos.y = (i + 1) * 50 + 20
            self.sprites.append(name_text)
            self.sprites.append(score_text)

        if len(self.scoreboard.scores) == 0:
            text = TextSprite("Brak danych", self.fonts["PixCon"].small, self.screen_rect, z_index=5)
            text.pos.x, text.pos.y = self.scoreboard_label.pos.x, 70
            self.sprites.append(text)

    def update(self, controller: 'SceneController'):
        if self.start_btn.clicked:
            controller.switch("Gameplay")
