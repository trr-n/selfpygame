class MathF:
    def __init__(self) -> None:
        raise Exception('yamete-')

    def floor(n, digit):
        pass

    def round(n, digit=1):
        return (n * 10 ** digit * 2 + 1) // 2 / 10 ** digit

    def digit(n):
        return len(str(n).replace('.', ''))

    def clamp(target, min=0, max=1):
        if target < min:
            target = min
        elif target > max:
            target = max
        return target

    def lerp(o, p, time):
        return o + (p - o) * MathF.clamp(time)

    def is_prime(n) -> bool:
        if not isinstance(n, int) or n < 2 or n % 2 == 0:
            # raise TypeError('n is not of int type or lower than 2')
            return False
        ns = []
        for i in range(2, n, 1):
            ns.append(False) if n % i == 0 else ns.append(True)
        return all(ns)
