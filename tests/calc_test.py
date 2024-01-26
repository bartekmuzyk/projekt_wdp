import pygame

import calc


def test_clamp():
    assert calc.clamp(10, 20, 30) == 20
    assert calc.clamp(20, 10, 30) == 20
    assert calc.clamp(30, 10, 20) == 20


def test_infinite_sequence():
    seq = calc.infinite_sequence([3, 1, 53, 23, 49])
    for i in range(2):
        assert next(seq) == 3
        assert next(seq) == 1
        assert next(seq) == 53
        assert next(seq) == 23
        assert next(seq) == 49


def test_precisecoords():
    coords = calc.PreciseCoords(10.501, 35.23)
    assert coords.x == 10.501
    assert coords.y == 35.23

    rect = pygame.Rect(0, 0, 0, 0)
    coords.apply_to_rect(rect)
    assert rect.x == 11
    assert rect.y == 35

    coords = calc.PreciseCoords.from_rect(rect)
    assert coords.x == 11
    assert coords.y == 35

    coords2 = calc.PreciseCoords.clone(coords)
    assert coords2.x == coords.x
    assert coords2.y == coords.y
