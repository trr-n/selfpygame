import random
import sys
from functools import singledispatch
import mathf
import enum

class Random: # (random):
    #? 乱数の仕組み https://qiita.com/mk668a/items/d53515817c41e22e77f0
    #? 文字列を数値に変換 https://www.hanachiru-blog.com/entry/2019/02/01/190918
    __normal_chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    __jp_chars = 'あいうえおかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをん'

    def normal_char(self, n: int):
        '''__normal_charsからn個ランダムに取り出す'''
        chars = list(self.__normal_chars)
        ls = []
        # n = len(chars) if n > len(chars) else n
        for i in range(n := len(chars)-1 if n > len(chars) else n-1):
            ls.append(chars[Random().generator(0, n)])
        # print('n: ', n)
        return ls

    def jp_char(self):
        chars = list(self.__jp_chars)
        return chars

    def mixed_char(self) -> str:
        return self.__normal_chars + self.__jp_chars

    @singledispatch
    def generator(self, min: int, max):
        srandom = random.SystemRandom()
        return srandom.randint(int(min), int(max))

    def test_gen(self, min, max, n) -> tuple[list, list]:
        old: list[int] = []
        new: list[int] = []
        for _ in range(n):
            old.append(random.randint(min, max))
            new.append(Random.generator(min, max))
        return (old, new)