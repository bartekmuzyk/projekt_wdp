def clamp(value, min_, max_):
    return max(min(value, max_), min_)


def infinite_sequence(frames: list[int]):
    while True:
        for frame in frames:
            yield frame
