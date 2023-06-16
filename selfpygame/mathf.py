import numpy


class Mathf:
    def __init__(self) -> None:
        raise Exception('yamete-')

    def round(n, digit=1):
        return (n * 10 ** digit * 2 + 1) // 2 / 10 ** digit

    def floor(n):
        return float(numpy.floor(n))

    def clamp(target, min=0, max=1):
        if target < min:
            target = min
        elif target > max:
            target = max
        return target

    def lerp(o, p, time):
        return o + (p - o) * Mathf.clamp(time)
