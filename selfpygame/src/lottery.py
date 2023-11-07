from typing import (
    Generic,
    TypeVar,
    overload
)

from functools import (
    singledispatch
)

from random import uniform

TSubject = TypeVar('TSubject')


class LotteryPair(Generic[TSubject]):
    def __init__(self, *pairs: (list[TSubject], list[float])) -> None:
        super().__init__()
        self.__pairs = pairs
        self.__subjects = []
        self.__weights = []
        for i in range(len(pairs)):
            self.__subjects.append(pairs[i][0])
            self.__weights.append(pairs[i][1])

    def count(self) -> int:
        return len(self.__subjects)

    def pairs(self) -> tuple:
        return self.__pairs

    def subjects(self, idx: int = -1) -> TSubject | list[TSubject]:
        return self.__subjects if idx == -1 else self.__subjects[idx]

    def weights(self, idx: int = -1) -> float | list[float]:
        return self.__weights if idx == -1 else self.__weights[idx]


class Lottery(Generic[TSubject]):
    @staticmethod
    def bst(weights: list[float]) -> int:
        '''
        binary search tree
        ===
        '''
        if len(weights) <= 0:
            return -1

        totals: list[float] = []
        total = 0.0
        for i in range(len(weights)):
            total += weights[i]
            # totals[i] = total
            totals.append(total)

        random = uniform(0, total)
        _min: int = 0
        _max: int = len(totals)-1
        while _min < _max:
            _center: float = (_min+_max) / 2
            if random > totals[_center]:
                _min = _center+1
            else:
                if random >= (totals[_center-1] if _center > 0 else 0):
                    return _center
                _max = _center
        return _max

    @staticmethod
    def weighted(pairs: LotteryPair) -> TSubject:
        return pairs.subjects(idx=Lottery.bst(weights=pairs.weights())) if pairs.count() != 1 else pairs.subjects(0)
