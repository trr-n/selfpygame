from functools import singledispatch


class OL:
    # overload
    @singledispatch
    def computer(n1: int, n2: int):
        return n1 + n2

    @computer.register
    def _computer(n1: float, n2: float):
        return n1 * n2


if __name__ == '__main__':
    ol1 = OL.computer(90, 10)
    ol2 = OL.computer(50, 20.0)
    print(f'ol1: {ol1}\nol2: {ol2}')
