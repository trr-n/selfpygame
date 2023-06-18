class Math:
    def __init__(self) -> None:
        raise Exception('yamete-')

    def floor(n, digit):
        pass

    def round(n, digit=1) -> int | float:
        return (n * 10 ** digit * 2 + 1) // 2 / 10 ** digit

    def digit(n) -> int:
        return len(str(n).replace('.', ''))

    def clamp(target, min=0, max=1) -> int | float:
        return min if target < min else max if target > max else target

    def lerp(o, p, time):
        return o + (p - o) * Math.clamp(time)

    def is_prime(n) -> bool:
        if not isinstance(n, int):
            raise TypeError('n is not of int type or lower than 2')
        elif n < 2 or n % 2 == 0:
            return False
        ns = []
        for i in range(2, n, 1):
            ns.append(False) if n % i == 0 else ns.append(True)
        return all(ns)

    def min(a, b):
        return a if a < b else b

    def max(a, b):
        return a if a > b else b
