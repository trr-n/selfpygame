from trrne import Box
from vector3 import Vector3
from mathf import Math
from randomf import Random
from animation import Animation
from lottery import (Lottery, LotteryPair)


if __name__ == '__main__':
    # a = Vector3(3, 6, 5)
    # b = Vector3(4, 1, 5)

    # print(Vector3.distance(a, b))
    # anim = Animation(5, 0.5)
    # print(anim.now_count())

    # a: str = "karachankawaikunai"
    # print(a, Box.replace_lump(a, ["kawaikunai"], "kawaii"))
    # # print(a, Coturnix.delete(a, "kawaikunai"))
    # # print(a, Coturnix.delete_lump(a, ["kawai", "kunai"]))
    # for _ in range(10):
    #     print(Random.normal_char(2))

    # t = tupletest(('kara', 10), ('oko', 7), ('kuri', 7), ('goma', 6))
    # # t = test('kara', 10, 'oko', 7, 'kuri', 7, 'goma', 6)
    # print(t.pair())
    # print(t.subjects())
    # print(t.weights())

    pairs = LotteryPair(
        ('karachan', 1.3),
        ('okoge', 2.5),
        ('kuri', 5.2),
        ('goma', 5.2)
    )
    # print(Lottery.weighted(pairs=pairs))
    print(Lottery.bst(weights=pairs.weights()))
