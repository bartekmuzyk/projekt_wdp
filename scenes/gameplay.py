import pygame.key

from elements import Board
from scene import Scene, SceneController


# noinspection PyAttributeOutsideInit
class GameplayScene(Scene):
    def start(self):
        self.board = Board(self.sprites["plansza"], self.screen)

    def render(self, controller: 'SceneController'):
        keys = pygame.key.get_pressed()
        move = [0, 0]

        if keys[pygame.K_w]:
            move[1] -= 1
        if keys[pygame.K_s]:
            move[1] += 1
        if keys[pygame.K_a]:
            move[0] -= 1
        if keys[pygame.K_d]:
            move[0] += 1

        moved_x, moved_y = self.board.move(*move)

        self.board.render()
