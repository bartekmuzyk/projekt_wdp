from dataclasses import dataclass

import pygame


def clamp(value, min_, max_):
    return max(min(value, max_), min_)


def infinite_sequence(frames: list[int]):
    while True:
        for frame in frames:
            yield frame


@dataclass
class PreciseCoords:
    x: float
    y: float

    @classmethod
    def from_rect(cls, rect: pygame.Rect):
        return cls(rect.x, rect.y)

    def apply_to_rect(self, rect: pygame.Rect):
        rect.x, rect.y = round(self.x), round(self.y)
