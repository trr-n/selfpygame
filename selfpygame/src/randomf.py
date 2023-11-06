import random


class Random:
    # ? 乱数の仕組み https://qiita.com/mk668a/items/d53515817c41e22e77f0
    # ? 文字列を数値に変換 https://www.hanachiru-blog.com/entry/2019/02/01/190918
    __normal_chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    __jp_chars = 'あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん'

    @staticmethod
    def normal_char(n: int):
        '''__normal_charsからn個ランダムに取り出す'''
        chars = list(Random.__normal_chars)
        ls = []
        # n = len(chars) if n > len(chars) else n
        for _ in range(n := len(chars)-1 if n > len(chars) else n-1):
            ls.append(chars[Random().randint(0, n)])
        # print('n: ', n)
        return ls

    @staticmethod
    def jp_char():
        chars = list(Random.__jp_chars)
        return chars

    @staticmethod
    def mixed_char() -> str:
        return Random.__normal_chars + Random.__jp_chars

    @staticmethod
    # @singledispatch
    def randint(min: int, max):
        srandom = random.SystemRandom()
        return srandom.randint(int(min), int(max))

    @staticmethod
    # @generator.register
    def uniform(min: float, max):
        srandom = random.SystemRandom()
        return srandom.uniform(min, max)

    @staticmethod
    def test_gen(min, max, n) -> tuple[list, list]:
        old: list[int] = []
        new: list[int] = []
        for _ in range(n):
            old.append(random.randint(min, max))
            new.append(Random.randint(min, max))
        return (old, new)
